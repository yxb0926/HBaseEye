#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: yuanxiaobin
Email: yxb0926@163.com
Date:  2016-11-25
'''

import os
import ConfigParser


class ParseConf:
    confile  = ""
    hmaster  = {}
    hregion  = {}
    thrift2  = {}
    conflist = {}

    def __init__(self, confile):
        self.confile = confile

    def parse(self):
        if self.__is_file_exist(self.confile):
            conf = ConfigParser.ConfigParser()
            conf.read(self.confile)
            self.__set_conf("hmaster", conf, self.hmaster)
            self.__set_conf("hregion", conf, self.hregion)
            self.__set_conf("thrift2", conf, self.thrift2)

    def __set_conf(self, sections, conf, confdict):
        if conf.options(sections):
            for attr in conf.options(sections):
                #confdict[attr] = conf.get(sections, attr)
                attrarr = conf.get(sections, attr).split(",")
                tmparr = []
                for k in attrarr:
                    tmparr.append(k.strip())

                confdict[attr] = tmparr


    def __is_file_exist(self, filename):
        isexist = False
        if os.path.exists(filename):
            isexist = True
        else:
            print "The confige file %s not exist" % filename
            os._exit(2)
        return isexist

    def getHmaster(self):
        return self.hmaster

    def getHregion(self):
        return self.hregion

    def getThrift2(self):
        return self.thrift2


