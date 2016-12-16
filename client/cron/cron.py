#!/usr/bin/env python
# -*- coding: utf-8 -*-
# write by yxb0926@163.com at 2016-12-15

import hregion
import multiprocessing
from multiprocessing import Process

class Cron(multiprocessing.Process):
    mongoconf = None
    def __init__(self, mongoconf):
        multiprocessing.Process.__init__(self)
        self.mongoconf = mongoconf

    def run(self):
        hregion.HRegion(self.mongoconf)


