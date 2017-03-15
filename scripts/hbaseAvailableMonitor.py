#!/usr/bin/env python
#coding=utf8

#
# write by yxb at 2017-03-14
# email: yxb0926@163.com
#

import HbaseMonitor
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase import THBaseService
from hbase.ttypes import *
import time


class HbaseAvailableMonitor(HbaseMonitor.HbaseMonitor):
    hClient    = None
    hTransport = None
    rowkey     = "hbaseMonitor"
    def __init__(self, host, tablename, column, port=9090, timeout=60000, family="fa"):
        self.host      = host
        self.tablename = tablename
        self.port      = port
        self.timeout   = timeout
        self.family    = family
        self.column    = column
        self.hClient, self.hTransport = self._hbaseClient()

    def __del__(self):
        self.hTransport.close()

    def _hbaseClient(self):
        transport = TSocket.TSocket(self.host, self.port)
        transport.setTimeout(self.timeout)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = THBaseService.Client(protocol)
        transport.open()

        return client, transport

    def checkHealth(self):
        resSet = self.checkSet()
        resGet = self.checkGet()

        errMsg = ""
        if resSet == 1:
            errMsg += "Hbase Set Failed. "
        if resGet == 1:
            errMsg += "Hbase Get Faild. "

        return errMsg

    def checkGet(self):
        try:
            get = TGet()
            get.row = self.rowkey
            result = self.hClient.get(self.tablename, get)
            #print result.columnValues[0].value
            # 0 => ok; 1 => failed
            if len(result.columnValues) > 0:
                return 0
            else:
                return 1
        except Exception as e:
            print e
            return 1


    def checkSet(self):
        value  = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            put = TPut(row=self.rowkey, columnValues=[TColumnValue(family=self.family,qualifier=self.column,value=value)])
            self.hClient.put(self.tablename, put)

            # 0 => ok; 1 => failed
            return 0
        except Exception as e:
            print e
            return 1


def main():
    host = "10.8.10.18"
    port = 9090
    timeout = 60000 #60s
    tablename = "monitor:heartbeat"
    family    = "cf"
    column    = "updateTime"

    hAvaliM = HbaseAvailableMonitor(host, tablename, column,  port, timeout, family)
    data = hAvaliM.checkHealth()
    if len(data) > 0:
        hAvaliM.alarm(data)


if __name__ == "__main__":
    main()
