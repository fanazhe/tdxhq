# -*- coding: utf-8 -*-
import threading
import time
import datetime
import logging
import json
from StringIO import StringIO
from ConfigParser import ConfigParser
from ctypes import *
import os,sys

class tdxhq(object):
    def __init__(self,):
        dllfile = os.path.join(os.path.dirname(sys.argv[0]),"../../modules/TdxHqApi.dll")
        self.tdxapi= windll.LoadLibrary(dllfile)
        self.err= create_string_buffer(256)
        self.res= create_string_buffer(1024*1024) 
        logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(levelname)-6s %(message)s')
        self.logger = logging.getLogger()
    
    def TdxHq_Connect(self,host=None,port=None):
        if not host:
            hostfile = os.path.join(os.path.dirname(sys.argv[0]),"../../etc/host.conf")
            cf = ConfigParser()
            cf.read(hostfile)
            for _, v in cf.items("HOST"):
                self.tdxapi.TdxHq_Connect("180.153.18.170", 7709, self.res, self.err)
                print (self.res.value.decode("GBK"))
                print (111)
                if not self.res.value.decode("GBK"):
                    self.logger.info(u"".format(self.err.value.decode("GBK")))
        else:
            pass
        
        pass
    
    def TdxHq_Disconnect(self):
        pass
    
    def TdxHq_GetSecurityQuotes(self):
        pass
# 
# err= create_string_buffer(256)
# res= create_string_buffer(1024*1024)  
# Api= windll.LoadLibrary('TdxHqApi.dll')
# Api.TdxHq_Disconnect()
# Api.TdxHq_Connect("180.153.18.170", 7709, res, err)
# print res.value.decode("gb2312")
# print err.value.decode("gb2312")
# 
# 
# market = (c_ubyte * 2)(0,1)
# zqdm = (c_char_p * 2)("000001","600030")
# count = (c_short*1)(2)         #取地址
# 
# Api.TdxHq_GetSecurityQuotes(market,zqdm,count,res, err )
# print res.value.decode("gb2312")
# print err.value.decode("gb2312")

# print (pd.read_csv(StringIO(g.res.value), sep="\t", encoding="GBK"))

if __name__ == '__main__':
    tdxhq = tdxhq()
    tdxhq.TdxHq_Connect()
    
    
    