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

	    regionServer_v2 = self._getValue(url, tag['RegionServer'])
	    #jvmMetrics_v2   = self._getValue(url, tag['JvmMetrics'])
	    WAL_v2          = self._getValue(url, tag['WAL'])

            self.regionServer(regionServer_v1, regionServer_v2)
	    self.JvmMetrics(jvmMetrics_v1)
	    self.WAL(WAL_v1, WAL_v2)

    def regionServer(self, v1, v2):
        t = int(1000*round(time.time()))
	hostname = v2['tag.Hostname']
	
	print t, hostname


    def JvmMetrics(self, v1):
        t = int(1000*round(time.time()))
	hostname = v1['tag.Hostname']
	
	print t, hostname, v1['MemNonHeapUsedM']

    def WAL(self, v1, v2):
        pass

    def _saveMongo(self, servername, kpidata):
        client = MongoClient(self.mongodbConf['ip'][0], int(self.mongodbConf['port'][0]))
	db = client.hbasestat
	collection = db.stat
	mydict = {}
	mydict['servername'] = servername
	mydict['timestamp']  = int(round(time.time()))
	mydict['kpi']        = kpidata
	collection.insert(mydict)
	

    def _getValue(self, url, tag):
        url = url + tag
        socket = urllib2.urlopen(url)
	v = socket.read()
	data = json.loads(v)
	socket.close()

	return data['beans'][0]

