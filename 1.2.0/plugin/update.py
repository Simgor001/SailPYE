'''自动更新模块'''
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import os
import sys
import requests
sys.path.append("..")
import core

class init(object):
    def __init__(self,sailpye, app, verstion):
        # 模块名：
        self._name = 'update'
        # 作者：
        self._author = 'Simgor001'
        # 版本：
        self._ver = '1.0.0'
        # 描述：
        self._msg = 'Sail Python Editor自动更新模块'

        self._core = sailpye
        self._app = app
        self._verstion = verstion


    def show_init(self):
        self.get_update()

    def get_update(self):
        print('正在获取更新...')
        try:
            ver = requests.get('http://sailpye.eace.top/Version').text
            
            print('最新版本：%s,当前版本：%s' %(ver,self._verstion))
            if int(self._verstion.replace('.', '')) >= int(ver.replace('.', '')):
                return
            print('正在更新...')
            update_file = self._core.temp_file('.py')

            with open(update_file, 'w+', encoding='UTF-8') as f:
                f.write(requests.get('http://sailpye.eace.top/update/%s.py' % ver).text)
            print('正在安装更新...')
            os.system('python %s' % update_file)
        except:
            print('更新失败！')