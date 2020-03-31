import sys
import os
from PyQt5 import QtCore


class Debug(object):

    def __init__(self):
        self.process = QtCore.QProcess()
        self.process.setInputChannelMode(QtCore.QProcess.ForwardedInputChannel)
        self.process.setProcessChannelMode(self.process.ForwardedOutputChannel)
        self.process.readyReadStandardError.connect(
            self.ready_read_standard_error)

    def ready_read_standard_error(self):
        self.error = str(self.process.readAllStandardError(), encoding='utf-8')
        sys.stdout.write(self.error)
        sys.stdout.flush()

    def start(self):

        self.process.setProgram('python')
        self.process.setArguments([r'temp.py'])

        self.process.start()
        # 等待启动
        if not self.process.waitForStarted(6000):
            return
        self.process.waitForFinished()
        if self.process.exitCode() != 0:
            print('发生错误')


Debug().start()
