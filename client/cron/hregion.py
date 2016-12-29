#!/usr/bin/env python
# -*- coding: utf-8 -*-
# write by yxb0926@163.com at 2016-12-15

import time
from pymongo import *

class HRegion():
    mongoconf = None
    def __init__(self, mongoconf):
        self.mongoconf = mongoconf
        self.run()


    def run(self):
        while True:
            self.calculate()
            time.sleep(10)
    
    def calculate(self):
        try:
            client = MongoClient(self.mongoconf['ip'][0], int(self.mongoconf['port'][0]))
            db = client.hbasestat
            collection1 = db["regionInfoTmp"]
            collection3 = db["regionInfo"]
            regionInfo = collection1.find()
            for item in regionInfo:
                mydict = {}
                collection2 = db["regionRequest"]
                collection4 = db["regionrsfmInfo"]
                data = collection2.find({"hostname":item['hostname']},{"_id":0, "read":1, "write":1, "totalRequestCount":1, "timestamp":1}).sort("timestamp", -1).limit(1)
                data4 = collection4.find({"hostname":item['hostname']},{"_id":0, "regionCount":1, "memStoreSize":1, "storeFileCount":1, "storeFileSize":1}).sort("timestamp", -1).limit(1)

                for v in data:
                    mydict['hostname'] = item['hostname']
                    mydict['read']     = v['read'][1]
                    mydict['write']    = v['write'][1]
                    mydict['totalRequestCount'] = v['totalRequestCount'][1]
                    mydict['serverName']  = item['serverName']
                    mydict['liveRegionServer']  = item['liveRegionServer']
                    mydict['timestamp'] = item['timestamp']

                for v4 in data4:
                    mydict['regionCount'] = v4['regionCount'][1]
                    mydict['memStoreSize'] = v4['memStoreSize'][1]/1024/1024
                    mydict['storeFileCount'] = v4['storeFileCount'][1]
                    mydict['storeFileSize']  = v4['storeFileSize'][1]/1024/1024/1024
                    collection3.update({'hostname':item['hostname']}, mydict, upsert=True)

            client.close() 
        except:
            print "get data failed"



