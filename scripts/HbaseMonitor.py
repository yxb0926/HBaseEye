#!/usr/bin/env python
#coding=utf8

#
# write by yxb at 2017-03-14
# email: yxb0926@163.com
#

import httplib
import sys,os
import time
import json
import urllib
import smtplib
from email.mime.text import MIMEText

class HbaseMonitor:
    def __init__(self, host, port, timeout, uri):
        self.host    = host
        self.port    = port
        self.timeout = timeout
        self.uri     = uri

    # get data from java jmx, use http protocol
    def _getStat(self):
        httpClient = None
        try:
            httpClient = httplib.HTTPConnection(self.host, self.port, timeout=self.timeout)
            httpClient.request('GET', self.uri)
            rep = httpClient.getresponse()

            status  = rep.status
            reason  = rep.reason
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

    # return the data from _getStat()
    def getData(self):
        code, data = self._getStat()
        if code == 1:
            for i in range(1, 3):
                print "The %s times for check" % i
                time.sleep(30)
                code, data = self._getStat()
                if code == 1:
                    continue
                else:
                    return data
            errmsg = "Get The Hadoop HDFS Status Failed."
            print errmsg

            self.alerm(errmsg)
            os._exit(404)
        else:
            return data


    # check service whether health with the give data
    def checkHealth(self, data):
        pass

    # alerm: sedMsg and sedEmail
    def alarm(self, msg):
        self.sedMsg(msg)
        self.sedEmail(msg)

    # alerm: sed err msg to staff
    # 每个短信接口可能不一样，改成你的可用的短信接口即可
    def sedMsg(self, msg):
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

    # alerm: sed err msg use email to staff
    def sedEmail(self, msg):
        mailSub = "Hbase Monitor"
        content = msg

        #  改成你的邮箱smtp server地址
        smtpHost = 'smtp.exmail.qq.com:465'

        # 改成你的邮件地址及对应的密码
        mailUser = 'yuanxiaobin@oneniceapp.com'
        mailPass = 'xxxxxxxxxxxxxx'

        # 改成你的邮箱地址
        mailTo = ['op@oneniceapp.com']

        ##Setting MIMEText
        message = MIMEText(content.encode('utf8'), _subtype = 'html', _charset = 'utf8')
        message['From']    = mailUser
        message['Subject'] = u'%s' % mailSub
        message['to']      = ",".join(mailTo)

        try:
            # connect to smtp Server
            s = smtplib.SMTP_SSL(smtpHost)
            s.set_debuglevel(0)

            # login smtp Server
            s.login(mailUser, mailPass)

            # send mail
            s.sendmail(message['From'], mailTo, message.as_string())

            # close connection
            s.close()

        except Exception as e:
            print e
