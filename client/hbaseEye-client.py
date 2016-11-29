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
import util.utils


def main():
    confile = os.getcwd() + "/conf/client.conf"
    parseConf = conf.parseconf.ParseConf(confile)
    parseConf.parse()

    parseConf.getHregion()

    threadRegion = hregion.region.Region(10000, "hregion", parseConf.getHregion())
    
    threadRegion.daemon = True
    threadRegion.start()
    threadRegion.join()
    print "end"
    

if __name__ == "__main__":
    main()

