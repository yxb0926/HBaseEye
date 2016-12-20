#!/usr/bin/env python
# -*- coding: utf-8 -*-
# write by yxb0926@163.com at 2016-12-6

import multiprocessing
from multiprocessing import Process
import serverTag
import util.utils
import time
from conf.parseconf import *

class Master(multiprocessing.Process):
    hMasterConf = None
    interval    = 10
    mongodbConf = None
    serverTag   = None

    def __init__(self):
        multiprocessing.Process.__init__(self)
        conf = ParseConf()
        self.hMasterConf = conf.getHmaster()
        self.mongodbConf = conf.getMongodb()
        self.interval    = (int)(self.hMasterConf['interval'][0])
        self.serverTag   = serverTag.tagdict

        
    def run(self):
        p = None
        plist = []
        for server in self.hMasterConf['serverlist']:
            p = multiprocessing.Process(target=self.request, \
                                        args=(server, self.serverTag,))
            p.start()
            plist.append(p)

        for x in plist:
            x.join()

    def request(self, server, tag):
        while True:
            url  = "http://"
            url += server
            url += "/jmx?qry="
            
            tools = util.utils.Utils()
            masterServer = tools.getMetrics(url, tag['MasterServer'])
            masterJvm    = tools.getMetrics(url, tag['MasterJvm'])

            time.sleep(self.interval)

            self.masterInfo(masterServer)
            self.jvmMetrics(masterJvm)

    def masterInfo(self, value):
        tools = util.utils.Utils()
        t = int(1000*round(time.time()))

        mydict = {}
        mydict['timestamp']            = t
        mydict['serverName']           = value['tag.serverName']
        mydict['clusterId']            = value['tag.clusterId']
        mydict['hostname']             = value['tag.Hostname']
        mydict['isActiveMaster']       = value['tag.isActiveMaster']
        mydict['role']                 = value['tag.Context']
        mydict['masterActiveTime']     = value['masterActiveTime']
        mydict['masterStartTime']      = value['masterStartTime']
        mydict['numRegionServers']     = value['numRegionServers']
        mydict['numDeadRegionServers'] = value['numDeadRegionServers']
        mydict['clusterRequests']      = value['clusterRequests']

        serverdict = {}
        serverdict['timestamp']        = t
        if value['tag.isActiveMaster'] == 'true':
            liveRegionServer = value['tag.liveRegionServers'].split(";")
            for server in liveRegionServer:
                serverdict['serverName'] = server
                serverdict['hostname']   = self._getHostNameFromServerName(server)
                serverdict['liveRegionServer'] = 'Live'

                tools.upsertMongo(serverdict, 'regionInfoTmp', self.mongodbConf)

            if value['tag.deadRegionServers'] != None and value['tag.deadRegionServers'] != '':
                deadRegionserver = value['tag.deadRegionServers'].split(";")
                for server in deadRegionserver:
                    serverdict['serverName'] = server
                    serverdict['hostname']   = self._getHostNameFromServerName(server)
                    serverdict['liveRegionServer'] = 'Dead'

                    tools.upsertMongo(serverdict, 'regionInfoTmp', self.mongodbConf)

        tools.upsertMongo(mydict, 'masterInfo', self.mongodbConf)

    
    def jvmMetrics(self, value):
        t = int(1000*round(time.time()))

        mydict = {}
        mydict['timestamp']                       = t
        mydict['hostname']                        = value['tag.Hostname']
        mydict['role']                            = value['tag.ProcessName']
        mydict['MemNonHeapUsedM']                 = [t, value['MemNonHeapUsedM']]
        mydict['MemNonHeapCommittedM']            = [t, value['MemNonHeapCommittedM']]
        mydict['GcCountParNew']                   = [t, value['GcCountParNew']]
        mydict['GcTimeMillisParNew']              = [t, value['GcTimeMillisParNew']]
        mydict['GcCountConcurrentMarkSweep']      = [t, value['GcCountConcurrentMarkSweep']]
        mydict['GcTimeMillisConcurrentMarkSweep'] = [t, value['GcTimeMillisConcurrentMarkSweep']]
        mydict['GcCount']                         = [t, value['GcCount']]
        mydict['GcTimeMillis']                    = [t, value['GcTimeMillis']]
        mydict['ThreadsNew']                      = [t, value['ThreadsNew']]
        mydict['ThreadsRunnable']                 = [t, value['ThreadsRunnable']]
        mydict['ThreadsBlocked']                  = [t, value['ThreadsBlocked']]
        mydict['ThreadsWaiting']                  = [t, value['ThreadsWaiting']]
        mydict['ThreadsTimedWaiting']             = [t, value['ThreadsTimedWaiting']]
        mydict['ThreadsTerminated']               = [t, value['ThreadsTerminated']]
        
        tools = util.utils.Utils()
        tools.insertMongo(mydict, 'masterJvmMetrics', self.mongodbConf)


    def _getHostNameFromServerName(self, serverName):
        server = serverName.split(",")
        hostname = server[0]+".niceprivate.com"
        return  hostname

