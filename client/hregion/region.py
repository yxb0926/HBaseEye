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


'''
class RegionMeta(threading.Thread):
    def __init__(self):
	threading.Thread.__init__(self)
'''


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
	    kpidata = {}
	    mydict  = {}
	    url  = "http://"
	    url += server
	    url += "/jmx?qry="

	    regionServer_v1 = self._getValue(url, tag['RegionServer'])
	    jvmMetrics_v1   = self._getValue(url, tag['JvmMetrics'])
	    WAL_v1          = self._getValue(url, tag['WAL'])

	    time.sleep(self.interval)

	    regionServer_v2  = self._getValue(url, tag['RegionServer'])
	    jvmMetrics_v2   = self._getValue(url, tag['JvmMetrics'])
	    WAL_v2           = self._getValue(url, tag['WAL'])

            if (regionServer_v1 is None or regionServer_v2 is None):
	        pass
	    else:
                self.regionServer(regionServer_v1, regionServer_v2)

            if (jvmMetrics_v1 is None or jvmMetrics_v2 is None):
	        pass
	    else:
	        self.JvmMetrics(jvmMetrics_v1)
		
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
        	
	self._saveMongo(mydict, 'regionRequest')

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

	self._saveMongo(rsfmdict, 'rsfmInfo')


    def JvmMetrics(self, v1):
        t = int(1000*round(time.time()))
	hostname = v1['tag.Hostname']
	
	#print t, hostname, v1['MemNonHeapUsedM']

    def WAL(self, v1, v2):
        pass

    def _saveMongo(self, data, tablename):
        client = MongoClient(self.mongodbConf['ip'][0], int(self.mongodbConf['port'][0]))
	db = client.hbasestat
	collection = db[tablename]
	collection.insert(data)
	client.close()
	

    def _getValue(self, url, tag):
        url = url + tag

	try:
            socket = urllib2.urlopen(url)
	    v = socket.read()
	    data = json.loads(v)
	    socket.close()
        
	    if 'beans' not in data.keys():
	        data = {}
	        data['beans'] = []
	        data['beans'].append(None)
	    if not len(data['beans']):
	        data = {}
	        data['beans'] = []
	        data['beans'].append(None)

	except:
	    print "Error!"
	    data = {}
	    data['beans'] = []
	    data['beans'].append(None)
	finally:
	    pass

	return data['beans'][0]
