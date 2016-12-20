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

from hregion.region import *
from hmaster.master import *
from cron.cron import *
import util.utils


def main():
    threadMaster = Master()
    threadRegion = Region()
    threadCron   = Cron()

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

