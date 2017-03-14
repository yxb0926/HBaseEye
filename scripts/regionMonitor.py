#!/usr/bin/env python
#coding=utf8

#
# write by yxb at 2017-03-14
# email: yxb0926@163.com
#



import HbaseMonitor
import os

class RegionMonitor(HbaseMonitor.HbaseMonitor):
    def checkHealth(self, data):
        if len(data['tag.deadRegionServers']) > 0:
            deadnodes = "Dead RegionServers:"
            for k in data['tag.deadRegionServers'].split(";"):
                deadlist   = k.split(",")
                deadnodes += deadlist[0] + ":" +deadlist[1] + " "
            print deadnodes
            return deadnodes
        else:
            os._exit(0)



def main():
    # 改成你的master的ip
    host = "10.8.10.21"

    # 改成你的master web server的端口
    port = 16010
    timeout = 100
    uri = "/jmx?qry=Hadoop:service=HBase,name=Master,sub=Server"

    regionM = RegionMonitor(host, port, timeout, uri)
    data = regionM.getData()
    msg  = regionM.checkHealth(data)
    regionM.alarm(msg)

if __name__ == "__main__":
    main()
