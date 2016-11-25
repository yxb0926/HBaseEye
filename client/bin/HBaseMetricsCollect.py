#!/usr/bin/env python
#encoding:utf-8

# Write by yxb at 2016-11-24

import ConfigParser

import sys
import os
import urllib2
import json
import time


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--conf", help="the confilger file.")
    args = parser.parse_args()
    
    return args


def getRequestCount():
    url='http://s-hadoop-log02:16030/jmx?qry=Hadoop:service=HBase,name=RegionServer,sub=Server'
    socket = urllib2.urlopen(url)
    v = socket.read()
    data = json.loads(v)
    print data['beans'][0]['totalRequestCount']


while True:
    getRequestCount()
    time.sleep(10)


