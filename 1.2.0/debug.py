import sys
import os
import tempfile
import socket
import threading
import time
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import Qsci


class Debug(object):
    def __init__(self, os, text_edit: QtWidgets.QTextEdit, temp_path):
        self.text_edit = text_edit
        self.break_list: list = list()
        self.os = os
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.time = 0

        self.tmp = temp_path

    def start_server(self):
        print('正在启动服务...')
        host = socket.gethostname()
        self.server.settimeout(1)
        port = 6520

        while True:
            try:
                self.server.bind((host, port))
                self.server.listen(3)
            except OSError:
                port += 1
            else:
                break
        return port

    def started(self):
        print('开始运行！')

    def state_changed(self, state: QtCore.QProcess.ProcessState):
        print('状态：%d' % state)
        self.state_flag = state

    def start(self, name):

        # 准备错误输出文件
        error_file = tempfile.mktemp(dir=self.tmp)
        with open(error_file, 'w+') as f:
            ...
        # 用时间戳作为验证码
        self.key = int(time.time() * 100)

        # 准备启动器
        self.launcher = tempfile.mktemp(
            dir=self.tmp, suffix='.py')
        with open(self.launcher, 'w', encoding='UTF-8') as f:
            f.write('port = %d\n' % self.start_server())
            f.write('key = %d\n' % self.key)
            f.write('name = r"%s"\n' % name)
            f.write('error_file = r"%s"\n' % error_file)
            with open('launcher.py', 'r', encoding='UTF-8') as lf:
                f.write(lf.read())

        # 启动脚本
        self.add_log('正在启动...')
        if self.os == 'win32':
            os.system('cmd /c start "%s" /b python %s' % (name, self.launcher))
        elif self.os == 'linux':
            os.system('gnome-terminal -x sh python ' + self.launcher)
        self.add_log('启动成功！')

        try_num = 0

        no_exit = True
        cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        QtCore.QCoreApplication.processEvents()
        while True:
            QtCore.QCoreApplication.processEvents()
            try:
                cl = self.server.accept()[0]
            except Exception:
                if try_num < 2:
                    try_num += 1
                else:
                    no_exit = False
                    break
            else:
                break

        # 心跳'
        print('开始心跳')
        while no_exit:
            QtCore.QCoreApplication.processEvents()
            # 发送心跳信号
            while no_exit:
                QtCore.QCoreApplication.processEvents()
                try:
                    cl.send('hb'.encode('UTF-8'))
                except Exception:
                    no_exit = False
                    break
                else:
                    break
            # 接收心跳信号
            while no_exit:
                QtCore.QCoreApplication.processEvents()
                try:
                    if cl.recv(1024).decode('UTF-8') == str(self.key):
                        break
                except Exception:
                    no_exit = False
                    break
                else:
                    break
        QtCore.QCoreApplication.processEvents()
        cl.close()
        self.server.close()
        print('运行完毕，已退出服务！')
        time.sleep(0.1)
        if self.os == 'linux':
            os.remove(sh)
        os.remove(self.launcher)

        return self.find_error(error_file)

    def find_error(self, error_file):

        errorf = open(error_file, 'r', encoding='UTF-8')
        error = errorf.read()
        errorf.close()
        os.remove(error_file)
        return error

    def add_log(self, text):
        self.text_edit.append(text)
        self.text_edit.repaint()
