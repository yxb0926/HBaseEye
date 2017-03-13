#!/usr/bin/env python

import httplib
import json
import os, sys
import urllib


def getStat(host, port, timout, uri):
    httpClient = None
    try:
        httpClient = httplib.HTTPConnection(host, port, timeout=timout)
        httpClient.request('GET', uri)
        rep = httpClient.getresponse()

        status = rep.status
        reason = rep.reason
        content = rep.read()

        if status == 200 and reason == "OK" and len(content)>0:
            data =  json.loads(content)
            return 0, data['beans'][0]
        else:
            out = "Get The Hadoop HDFS Status Failed."
            print out
            return 1, out

    except Exception, e:
        print e
        return 1, e

    finally:
        if httpClient:
            httpClient.close()


def checkHealth(data):
    liveNodes  = data['LiveNodes']
    deadNoes   = data['DeadNodes']
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

    if len(json.loads(deadNoes)) > 0:
        error = error + "HDFS deadnode: "
        for k in json.loads(deadNoes):
            error = error + k + " "
        print error

    if len(json.loads(decomNodes)) > 0:
        error = erorr +"HDFS decomnode: " + decomNodes
        print error

    if len(error)>0:
        sedMsg(error)


def sedMsg(msg):
    gid = "11"
    gpass = "jqYgH2OhDk"
    content = msg
    url = "http://smscenter.niceprivate.com/smscenter.php?g="
    url += gid
    url += "&p="
    url += gpass
    url += "&desc="
    url += "[Hbase][Disaster]"
    url += content
    url += "&deploy_path="
    url += "hdfsMonitor.py"
    url += "&type=1"

    urllib.urlopen(url)


def main():
    #host = "10.8.10.26"
    host = "10.10.10.51"
    port = 50070
    timeout = 100
    uri = "/jmx?qry=Hadoop:service=NameNode,name=NameNodeInfo"
    code , data = getStat(host, port, timeout, uri)

    ## code == 1 ,check 2 times more, and sleep 30s for every time.
    if code == 1:
        for i in range(1, 3):
            print "The %s times for check" % i
            sys.sleep(30)
            code, data = getStat(host, port, timeout, uri)
            if code == 1:
                continue
            else:
                checkHealth(data)
    else:
        checkHealth(data)



if __name__ == "__main__":
    main()
