#!/usr/bin/env python
#encoding:utf-8

import urllib2
import json
from pymongo import *
import conf.parseconf

class Utils:
    def __init__(self):
        pass

    def getMetrics(self, url, tag):
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

    def insertMongo(self, data, tablename, mongoconf):
        client = MongoClient(mongoconf['ip'][0], int(mongoconf['port'][0]))
        db = client.hbasestat
        collection = db[tablename]
        collection.insert(data)
        client.close()


    def upsertMongo(self, data, tablename, mongoconf):
        client = MongoClient(mongoconf['ip'][0], int(mongoconf['port'][0]))
        db = client.hbasestat
        collection = db[tablename]
        collection.update({'hostname':data['hostname']}, data, upsert=True)
        client.close()
