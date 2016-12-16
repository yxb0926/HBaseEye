#!/usr/bin/env python
# encoding:utf-8

'''
Author: yuanxiaobin
Email:  yxb0926@163.com
'''

import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

import conf.parseconf
import hregion.region
import hmaster.master
import util.utils
import cron.cron


def main():
    confile = os.getcwd() + "/conf/client.conf"

    parseConf = conf.parseconf.ParseConf(confile)
    parseConf.parse()

    parseConf.getHregion()


    threadRegion = hregion.region.Region(parseConf.getHregion(),  parseConf.getMongodb())
    threadMaster = hmaster.master.Master(parseConf.getHmaster(),  parseConf.getMongodb())
    
    threadCron   = cron.cron.Cron(parseConf.getMongodb())

    threadRegion.daemon = True
    threadRegion.start()

    threadMaster.daemon = True
    threadMaster.start()

    threadCron.daemon   = True
    threadCron.start()

    threadRegion.join()
    threadMaster.join()
    threadCron.join()
    

if __name__ == "__main__":
    main()

