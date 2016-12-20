#!/usr/bin/env python
# -*- coding: utf-8 -*-
# write by yxb0926@163.com at 2016-12-15


from hregion import *
import multiprocessing
from conf.parseconf import *

class Cron(multiprocessing.Process):
    mongoconf = None
    def __init__(self):
        multiprocessing.Process.__init__(self)
        conf = ParseConf()
        self.mongoconf = conf.getMongodb()

    def run(self):
        HRegion(self.mongoconf)


