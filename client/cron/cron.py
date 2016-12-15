#!/usr/bin/env python
# -*- coding: utf-8 -*-
# write by yxb0926@163.com at 2016-12-15

#from hregion import *
import hregion

class Cron():
    mongoconf = None
    def __init__(self, mongoconf):
        self.mongoconf = mongoconf
        self.start()

    def start(self):
        threadRegion = hregion.HRegion(self.mongoconf)
        threadRegion.daemon = True
        threadRegion.start()

        threadRegion.join()

