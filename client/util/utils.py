#!/usr/bin/env python
#encoding:utf-8


import os
import time
from subprocess import Popen, PIPE
from ctypes import pythonapi, c_int, c_char_p, POINTER, addressof, pointer, CDLL, memmove, memset
from ctypes.util import find_library

"""
  Attempt to set the process name with ctypes
"""
class SetPname:
    name = ""
    def __init__(self, name):
        self.name = name

        Py_GetArgcArgv = pythonapi.Py_GetArgcArgv

        c_lib = CDLL(find_library("c"))
        PR_SET_NAME = 15                        # linux specific

        argc_t = POINTER(c_char_p)
        Py_GetArgcArgv.restype = None
        Py_GetArgcArgv.argtypes = [POINTER(c_int), POINTER(argc_t)]

	self.__setPname()

    def __setPname(self):
        argv = c_int(0)
        argc = argc_t()
        Py_GetArgcArgv(argv, pointer(argc))
        name0 = self.name+"\0"
        memset(argc.contents, 0, 256)       # could do this better!
        memmove(argc.contents, name0, len(name0))
        # prctl doesn't seem to be needed on linux?
        c_lib.prctl(PR_SET_NAME, self.name+"\0", 0, 0, 0)



