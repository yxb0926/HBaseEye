#!/usr/bin/env python
#coding=utf8

#
# write by yxb at 2017-03-14
# email: yxb0926@163.com
#

import HbaseMonitor

def main():
    host = {"10.8.10.21","10.8.10.26","10.8.10.28","10.8.10.18"}
    port = 9095
    timeout = 10
    uri = "/jmx?qry=Hadoop:service=HBase,name=Thrift,sub=ThriftTwo"
    for h in host:
        thriftM = HbaseMonitor.HbaseMonitor(h, port, timeout, uri)
        data = thriftM.getData()
        if data == 404:
            print "Thrift Server:%s:%s Down" % (h, port)
            thriftM.alarm("Thirft Server:%s:%s Down." % (h, port))


if __name__ == "__main__":
    main()
