#!/usr/bin/env python
#coding=utf8

#
# write by yxb at 2017-03-14
# email: yxb0926@163.com
#


import HbaseMonitor
import json

class HdfsMonitor(HbaseMonitor.HbaseMonitor):
    def checkHealth(self, data):
        liveNodes  = data['LiveNodes']
        deadNodes  = data['DeadNodes']
        decomNodes = data['DecomNodes']

        listLive = json.loads(liveNodes)
        error = ""
        for k in listLive:
            blockPoolUsedPercent = listLive[k]['blockPoolUsedPercent']
            volfails             = listLive[k]['volfails']

            if int(blockPoolUsedPercent) >=90:
                error = error + k + " block used >= 90%."
                print error

            if int(volfails) > 0:
                error = error + " " + k + " failed volumes > 0"
                print error

        # dead nodes
        if len(json.loads(deadNodes)) > 0:
            error = error + "HDFS deadnode: "
            for k in json.loads(deadNodes):
                error = error + k + " "
            print error

        if len(json.loads(decomNodes)) > 0:
            error = erorr +"HDFS decomnode: " + decomNodes
            print error

        if len(error)>0:
            return error


def main():
    # 改成你的master的ip
    host = "10.8.10.21"

    # 改成你的master对应的端口
    port = 50070
    timeout = 100
    uri = "/jmx?qry=Hadoop:service=NameNode,name=NameNodeInfo"

    hdfsM = HdfsMonitor(host, port, timeout, uri)
    data = hdfsM.getData()
    msg = hdfsM.checkHealth(data)
    hdfsM.alarm(msg)


if __name__ == "__main__":
    main()
