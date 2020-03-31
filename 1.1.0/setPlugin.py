import sys
import os
import core
import copy
import importlib
from PyQt5 import QtCore
from PyQt5 import QtWidgets


class plugin():
    def __init__(self, sailpye: core.core, app: QtWidgets.QApplication,verstion):
        self.core = sailpye
        self.app = app
        self.plugins = list()
        self.show_init_list = list()
        self.verstion = verstion

    def install(self):
        # 遍历插件目录
        dirs = os.listdir('plugin')
        single = dict()
        for f in dirs:
            if os.path.isfile('plugin/' + f) and f[-3:] == '.py':
                single['file'] = f
                print('正在加载插件%s'%f)
                try:
                    single['obj'] = importlib.import_module('plugin.' + f[:-3])
                except:
                    return('ErrorCode -03.0，将文件"%s"用于添加插件时，出现错误!' % f)
                # 初始化插件
                try:
                    if single['obj'].init(self.core, self.app,self.verstion):
                        self.show_init_list.append(single['obj'].show_init)
                except:
                    return('ErrorCode -03.2，将文件"%s"用于添加插件时，出现错误!，init对象错误！' % f)
                self.plugins.append(single.copy())
        return ''
