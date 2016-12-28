#!/usr/bin/env python
# encoding:utf-8

'''
Author: yuanxiaobin
Email:  yxb0926@163.com
'''

import multiprocessing
import sys
import util.utils
import os
import time
import serverTag
from conf.parseconf import *


class Region(multiprocessing.Process):
    hregionConf = None
    interval    = 10
    mongodbConf = None
    serverTag   = None
    
    def __init__(self):
        multiprocessing.Process.__init__(self)
        conf = ParseConf()
        self.hregionConf = conf.getHregion()
        self.mongodbConf = conf.getMongodb()
        self.interval    = (int)(self.hregionConf['interval'][0])
        self.serverTag   = serverTag.tagdict
        self.start()

    def run(self):
        p = None
        plist = []
        for server in self.hregionConf['serverlist']:
            p = multiprocessing.Process(target=self.request,\
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

            regionServer_v1 = tools.getMetrics(url, tag['RegionServer'])
            jvmMetrics_v1   = tools.getMetrics(url, tag['JvmMetrics'])
            WAL_v1          = tools.getMetrics(url, tag['WAL'])

            time.sleep(self.interval)
            regionServer_v2  = tools.getMetrics(url, tag['RegionServer'])
            jvmMetrics_v2    = tools.getMetrics(url, tag['JvmMetrics'])
            WAL_v2           = tools.getMetrics(url, tag['WAL'])

            if (regionServer_v1 is None or regionServer_v2 is None):
                pass
            else:
                self.regionServer(regionServer_v1, regionServer_v2)

            if (jvmMetrics_v2 is None):
                pass
            else:
                self.JvmMetrics(jvmMetrics_v1, jvmMetrics_v2)
            
            if (WAL_v1 is None or WAL_v2 is None):
                pass
            else:
                self.WAL(WAL_v1, WAL_v2)

    #
    # qps,tps...统计入库
    #
    def regionServer(self, v1, v2):
	    #
	    #  保存tps、qps 等数据到表regonRequest中
	    #
        t = int(1000*round(time.time()))
        mydict = {}
        mydict['timestamp'] = t
        mydict['hostname'] = v2['tag.Hostname']
        mydict['totalRequestCount'] = [t,v2['totalRequestCount']]
        mydict['writeRequestCount'] = [t,v2['writeRequestCount']]
        mydict['readRequestCount']  = [t,v2['readRequestCount']]
        mydict['qps']   = [t, round((v2['totalRequestCount'] - v1['totalRequestCount'])/self.interval)]
        mydict['write'] = [t, round((v2['writeRequestCount'] - v1['writeRequestCount'])/self.interval)]
        mydict['read']  = [t, round((v2['readRequestCount'] - v1['readRequestCount'])/self.interval)]
        	
        tools = util.utils.Utils()
        tools.insertMongo(mydict, 'regionRequest', self.mongodbConf)

	    #
	    #  保存region, store, hfile, memStore信息
	    #

        rsfmdict = {}
        rsfmdict['timestamp']      = t
        rsfmdict['hostname']       = v2['tag.Hostname']
        rsfmdict['regionCount']    = [t, v2['regionCount']]
        rsfmdict['storeCount']     = [t, v2['storeCount']]
        rsfmdict['storeFileCount'] = [t, v2['storeFileCount']]
        rsfmdict['storeFileSize']  = [t, v2['storeFileSize']]
        rsfmdict['hlogFileCount']  = [t, v2['hlogFileCount']]
        rsfmdict['hlogFileSize']   = [t, v2['hlogFileSize']]
        rsfmdict['memStoreSize']   = [t, v2['memStoreSize']]

        tools = util.utils.Utils()
        tools.insertMongo(rsfmdict, 'regionrsfmInfo', self.mongodbConf)


    def JvmMetrics(self, v1, v2):
        t = int(1000*round(time.time()))
        mydict = {}
        mydict['timestamp'] = t
        mydict['hostname']                        = v2['tag.Hostname']
        mydict['MemNonHeapUsedM']                 = [t, v2['MemNonHeapUsedM']]
        mydict['MemNonHeapCommittedM']            = [t, v2['MemNonHeapCommittedM']]
        mydict['MemNonHeapMaxM']                  = [t, v2['MemNonHeapMaxM']]
        mydict['MemHeapUsedM']                    = [t, v2['MemHeapUsedM']]
        mydict['MemHeapCommittedM']               = [t, v2['MemHeapCommittedM']]
        mydict['MemHeapMaxM']                     = [t, v2['MemHeapMaxM']]
        mydict['MemMaxM']                         = [t, v2['MemMaxM']]
        ## Young GC 累计次数
        mydict['GcCountParNew']                   = [t, v2['GcCountParNew']]
        ## Young GC 累计时间(毫秒)
        mydict['GcTimeMillisParNew']              = [t, v2['GcTimeMillisParNew']]

        mydict['GcCountConcurrentMarkSweep']      = [t, v2['GcCountConcurrentMarkSweep']]
        mydict['GcTimeMillisConcurrentMarkSweep'] = [t, (v2['GcTimeMillisConcurrentMarkSweep'] - v1['GcTimeMillisConcurrentMarkSweep'])/self.interval]
        ## Young GC 和Full GC的总和
        mydict['GcCount']                         = [t, v2['GcCount']]
        mydict['GcTimeMillis']                    = [t, v2['GcTimeMillis']]

        ## Full GC 统计
        mydict['GcFullCount']                     = [t, v2['GcCount'] - v2['GcCountParNew']]
        mydict['GcFullTimeMillis']                = [t, v2['GcTimeMillis'] -v2['GcTimeMillisParNew']]


        mydict['ThreadsNew']                      = [t, v2['ThreadsNew']]
        mydict['ThreadsRunnable']                 = [t, v2['ThreadsRunnable']]
        mydict['ThreadsBlocked']                  = [t, v2['ThreadsBlocked']]
        mydict['ThreadsWaiting']                  = [t, v2['ThreadsWaiting']]
        mydict['ThreadsTimedWaiting']             = [t, v2['ThreadsTimedWaiting']]
        mydict['ThreadsTerminated']               = [t, v2['ThreadsTerminated']]

        tools = util.utils.Utils()
        tools.insertMongo(mydict, 'reginJvmMetrics', self.mongodbConf)
	

    def WAL(self, v1, v2):
        t = int(1000*round(time.time()))
        mydict = {}
        mydict['timestamp'] = t
        mydict['hostname']  = v2['tag.Hostname']
        mydict['rollRequest']        = [t, (v2['rollRequest'] - v1['rollRequest'])/self.interval]
        mydict['SyncTime_num_ops']   = [t, (v2['SyncTime_num_ops'] - v1['SyncTime_num_ops'])/self.interval]
        mydict['SyncTime_median']    = [t, (v2['SyncTime_median'] - v1['SyncTime_median'])/self.interval]
        mydict['AppendSize_num_ops'] = [t, (v2['AppendSize_num_ops'] - v1['AppendSize_num_ops'])/self.interval]
        mydict['AppendSize_median']  = [t, (v2['AppendSize_median'] - v1['AppendSize_median'])/self.interval]
        mydict['AppendTime_num_ops'] = [t, (v2['AppendTime_num_ops'] - v1['AppendTime_num_ops'])/self.interval]
        mydict['AppendTime_median']  = [t, (v2['AppendTime_median'] - v1['AppendTime_median'])/self.interval]
        mydict['slowAppendCount']    = [t, (v2['slowAppendCount'] - v1['slowAppendCount'])/self.interval]
        mydict['appendCount']        = [t, (v2['appendCount'] - v1['appendCount'])/self.interval]
        
        tools = util.utils.Utils()
        tools.insertMongo(mydict, 'reginWALMetrics', self.mongodbConf)

