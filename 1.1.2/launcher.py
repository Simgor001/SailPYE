import socket
import threading
import subprocess
import os
import io
import sys
import time
from PyQt5 import QtCore
socket.setdefaulttimeout(1)
cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cl.connect_ex((socket.gethostname(), port))
cl.settimeout(1)


class launcher(object): 

    def __init__(self):

        self.process = QtCore.QProcess()
        self.process.setInputChannelMode(QtCore.QProcess.ForwardedInputChannel)
        self.process.setProcessChannelMode(self.process.ForwardedOutputChannel)
        self.process.readyReadStandardError.connect(
            self.ready_read_standard_error)
        self.error = ''

    def ready_read_standard_error(self):
        error = self.process.readAllStandardError()
        try:
            self.error = str(error, encoding='utf-8')
        except UnicodeDecodeError:
            self.error = str(error, encoding='gbk')
        sys.stdout.write(self.error)
        sys.stdout.flush()

    def start(self):
 
        self.process.setProgram('python')
        self.process.setArguments([name])

        self.process.start()
        # 等待启动
        if not self.process.waitForStarted(3000):
            return
        self.process.waitForFinished()
        if self.process.exitCode() != 0 and self.process.exitStatus() == 0:
            with open(error_file,'w+b') as f:
                f.write(bytes(self.error.encode('utf-8')))
        return
def hb():
    no_exit = True
    # 心跳
    while no_exit:
        # 接收心跳信号
        while no_exit:
            try:
                cmd = cl.recv(1024).decode('UTF-8')
                if cmd == 'hb':
                    break
            except socket.timeout:
                no_exit = False
                break
            else:
                break
        # 发送心跳信号
        while True and no_exit:
            try:
                cl.send(str(key).encode('UTF-8'))
            except Exception:
                no_exit = False
                break
            else:
                break
    cl.close()
    sys.exit(0)
threading.Thread(target=hb,daemon=True).start()
launcher().start()
cl.close()
sys.exit(0)