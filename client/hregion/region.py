#!/usr/bin/env python
# encoding:utf-8

'''
Author: yuanxiaobin
Email:  yxb0926@163.com
'''

import multiprocessing
from multiprocessing import Process
import sys
import util.utils
import os
import time
import serverTag
import urllib2
import json
from pymongo import *


class Region(multiprocessing.Process):
    hregionConf = None
    interval    = 10
    mongodbConf = None
    serverTag   = None
    
    def __init__(self, hregionConf, mongodbconf):
        multiprocessing.Process.__init__(self)
        self.hregionConf = hregionConf
        self.mongodbConf = mongodbconf
        self.interval    = (int)(hregionConf['interval'][0])
        self.serverTag = serverTag.tagdict

    def run(self):
        p = None
        plist = []
        for server in self.hregionConf['serverlist']:
            p = multiprocessing.Process(target=self.request,\
                                        args=(server, self.serverTag, self.interval,))
            p.start()
            plist.append(p)
        for x in plist:
            x.join()

    def request(self, server, tag, interval):
        while True:
            url  = "http://"
            url += server
            url += "/jmx?qry="

            tools = util.utils.Utils()

            regionServer_v1 = tools.getMetrics(url, tag['RegionServer'])
            #jvmMetrics_v1   = tools.getMetrics(url, tag['JvmMetrics'])
            WAL_v1          = tools.getMetrics(url, tag['WAL'])

            time.sleep(interval)
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
                self.JvmMetrics(jvmMetrics_v2)
            
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


    def JvmMetrics(self, v):
        t = int(1000*round(time.time()))
        mydict = {}
        mydict['timestamp'] = t
        mydict['hostname']                        = v['tag.Hostname']
        mydict['MemNonHeapUsedM']                 = [t, v['MemNonHeapUsedM']]
        mydict['MemNonHeapCommittedM']            = [t, v['MemNonHeapCommittedM']]
        mydict['MemNonHeapMaxM']                  = [t, v['MemNonHeapMaxM']]
        mydict['MemHeapUsedM']                    = [t, v['MemHeapUsedM']]
        mydict['MemHeapCommittedM']               = [t, v['MemHeapCommittedM']]
        mydict['MemHeapMaxM']                     = [t, v['MemHeapMaxM']]
        mydict['MemMaxM']                         = [t, v['MemMaxM']]
        mydict['GcCountParNew']                   = [t, v['GcCountParNew']]
        mydict['GcTimeMillisParNew']              = [t, v['GcTimeMillisParNew']]
        mydict['GcCountConcurrentMarkSweep']      = [t, v['GcCountConcurrentMarkSweep']]
        mydict['GcTimeMillisConcurrentMarkSweep'] = [t, v['GcTimeMillisConcurrentMarkSweep']]
        mydict['GcCount']                         = [t, v['GcCount']]
        mydict['GcTimeMillis']                    = [t, v['GcTimeMillis']]
        mydict['ThreadsNew']                      = [t, v['ThreadsNew']]
        mydict['ThreadsRunnable']                 = [t, v['ThreadsRunnable']]
        mydict['ThreadsBlocked']                  = [t, v['ThreadsBlocked']]
        mydict['ThreadsWaiting']                  = [t, v['ThreadsWaiting']]
        mydict['ThreadsTimedWaiting']             = [t, v['ThreadsTimedWaiting']]
        mydict['ThreadsTerminated']               = [t, v['ThreadsTerminated']]

        tools = util.utils.Utils()
        tools.insertMongo(mydict, 'reginJvmMetrics', self.mongodbConf)
	

    def WAL(self, v1, v2):
        pass

