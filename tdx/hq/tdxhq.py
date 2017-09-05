# -*- coding: utf-8 -*-
import threading
import time
import datetime
import logging
import json
from StringIO import StringIO
from ctypes import *
import sys

class tdxhq(object):
    def __init__(self):
        pass
    
    def TdxHq_Connect(self,host,port):
        
        pass
    
    def TdxHq_Disconnect(self):
        pass
    
    def TdxHq_GetSecurityQuotes(self):
        pass

err= create_string_buffer(256)
res= create_string_buffer(1024*1024)  
Api= windll.LoadLibrary('TdxHqApi.dll')
Api.TdxHq_Disconnect()
Api.TdxHq_Connect("180.153.18.170", 7709, res, err)
print res.value.decode("gb2312")
print err.value.decode("gb2312")


market = (c_ubyte * 2)(0,1)
zqdm = (c_char_p * 2)("000001","600030")
count = (c_short*1)(2)         #取地址

Api.TdxHq_GetSecurityQuotes(market,zqdm,count,res, err )
print res.value.decode("gb2312")
print err.value.decode("gb2312")

# print (pd.read_csv(StringIO(g.res.value), sep="\t", encoding="GBK"))

if __name__ == '__main__':
    pass