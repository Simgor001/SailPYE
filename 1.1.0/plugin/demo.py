'''标准Sial Python Editor插件模板'''
import os
import sys
sys.path.append("..")
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
'''如果有需要用到到某个主模块，可以把注释去掉。'''
import core
#import config
#import GUI
#import debug

'''每个插件必须有一个init类'''
class init():
    def __init__(self,sailpye,app):
        self.core = sailpye
        self.app = app

        '''填写模块信息'''
        #模块名：
        self.name = 'demo'
        #作者：
        self.author = '作者'
        #版本：
        self.var = '1.0'
        #描述：
        self.msg = '描述'

        '''在这下面开始插件代码'''