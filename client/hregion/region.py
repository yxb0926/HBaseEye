#!/usr/bin/env python
# encoding:utf-8

'''
Author: yuanxiaobin
Email:  yxb0926@163.com
'''

import multiprocessing
from multiprocessing import Process
import multiprocessing.pool
import sys
import util.utils
import os
import time
import serverTag
import urllib2
import json

'''
class RegionMeta(threading.Thread):
    def __init__(self):
	threading.Thread.__init__(self)
'''


class Region(multiprocessing.Process):
    processId   = ""
    processName = ""
    hregionConf = {}
    interval    = 10
    
    def __init__(self, processId, name, hregionConf):
        multiprocessing.Process.__init__(self)
        self.processId   = processId
	self.processName = name
	self.hregionConf = hregionConf
	self.interval    = (int)(hregionConf['interval'][0])
	#util.utils.SetPname(self.processName)


    def run(self):
        pool = multiprocessing.Pool(4)
	plist = []
	p = None
	for server in self.hregionConf['serverlist']:
	    #tmplist = []
	    #tmplist = [server, serverTag.HBase_RegionServer_Server_Tag, self.interval] 
	    #plist.append(tmplist)
	    p = multiprocessing.Process(target=req, args=(server, serverTag.HBase_RegionServer_Server_Tag, self.interval,))

	    p.start()
	p.join()
	#pool.map(req,plist)
	#pool.close()
	#pool.join()

    def getQps(self):
        pass



    def request(self, server, tag, interval):
        while True:
	    kpidata = {}
	    url  = "http://"
	    url += server
	    url += "/jmx?qry="
	    v1    = self.getValue(url, tag)
	    time.sleep(self.interval)
	    v2    = self.getValue(url, tag)
	    kpidata['read_qps']  = int(round(v2['readRequestCount'] - v1['readRequestCount'])/interval)
	    kpidata['write_qps'] = int(round(v2['writeRequestCount'] - v1['writeRequestCount'])/interval)
	    
	    print kpidata


    def __qps(self, server, tag, interval):
        url  = "http://"
	url += server
	url += "/jmx?qry="

        v1 = self.__getValue(url, tag)
	time.sleep(interval)
	#v2 = self.__getValue(url, tag)
	#qps = (v2-v1)/interval
	
	return v1

    def getValue(self, url, tag):
        url = url + tag
        socket = urllib2.urlopen(url)
	v = socket.read()
	data = json.loads(v)
	socket.close()

	return data['beans'][0]



def req(server,tag,interval):
    while True:
        print server
	time.sleep(2)
        #kpidata = {}
	#url  = "http://"
	#url += server
	#url += "/jmx?qry="
	#v1    = self.getValue(url, tag)
	#time.sleep(self.interval)
	#v2    = self.getValue(url, tag)
	#kpidata['read_qps']  = int(round(v2['readRequestCount'] - v1['readRequestCount'])/interval)
	#kpidata['write_qps'] = int(round(v2['writeRequestCount'] - v1['writeRequestCount'])/interval)
	#   
	#print kpidata
