'''标准Sial Python Editor插件模板'''
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import os
import sys
import time
sys.path.append("..")
import core
'''如果有需要用到到某个主模块，可以把注释去掉。'''
#import config
#import GUI
#import debug

'''填写模块信息'''
# 模块名：
_name = 'tesk'
# 作者：
_author = '作者'
# 版本：
_var = '插件版本号'
# 描述：
_msg = '描述'
_core: core.core = object()
_app: QtWidgets.QApplication = object()


def init(sailpye, app):
    '''每个插件必须有一个init函数，该函数于show函数之前调用'''
    _core = sailpye
    _app = app

    '''在这下面开始插件代码'''

    '''如果该插件有show_init函数，请返回True'''
    return False


def show_init():
    '''
    可选的函数，该函数于show之后调用，
    如果需要用到这个函数，请在init函数中返回True
    '''
    ...
    
