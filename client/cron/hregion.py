#!/usr/bin/env python
# -*- coding: utf-8 -*-
# write by yxb0926@163.com at 2016-12-15

import time
import multiprocessing
from pymongo import *


class HRegion(multiprocessing.Process):
    mongoconf = None
    def __init__(self, mongoconf):
        multiprocessing.Process.__init__(self)
        self.mongoconf = mongoconf


    def run(self):
        while True:
            self.calculate()
            time.sleep(10)
    
    def calculate(self):
        client = MongoClient(self.mongoconf['ip'][0], int(self.mongoconf['port'][0]))
        db = client.hbasestat
        tablename1 = "regionRequest"
        collection = db[tablename1]
        print "xxxx"



