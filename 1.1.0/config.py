import sys
import json
import os
import lexer
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import Qsci


class Config(object):
    def __init__(self, parent: QtWidgets.QWidget, editor: Qsci.QsciScintilla):

        self.parent = parent
        self.file_list = [
            'main.pyw',
            'core.py',
            'GUI.py',
            'config.py',
            'mainWin.py',
            'aboutWin.py',
            'img/logo.png',
            'img/logo.ico',
            'json/config.json']
        self.cheak_file_integrity()

        self.config_file: str = 'json/config.json'
        self.load_config()

        self.lexer = lexer.lexer(editor)
        
        self.set_lexer()

    def cheak_file_integrity(self):
        '''检查文件完整性
           ErrorCode-20
        '''
        for i in range(len(self.file_list)):
            if not os.path.isfile(self.file_list[i]):
                QtWidgets.QMessageBox.critical(self.parent, '错误',
                                               'ErrorCode -20.%d，内容不完整,缺少%s' % (i, self.file_list[i]))
                sys.exit('ErrorCode -20%d' % i)

    def load_config(self):
        '''加载配置文件
           ErrorCode-30
        '''
        with open(self.config_file, 'r', encoding='UTF-8') as f:
            self.config = json.load(f)

        theme_file = 'json/'+self.config["theme"]

        if os.path.isfile(theme_file) == False:
            QtWidgets.QMessageBox.critical(
                self.parent, "错误", "ErrorCode -30.0，主题文件%s不存在" % theme_file)
            sys.exit('ErrorCode -30.0')

        with open(theme_file, 'r', encoding='UTF-8') as f:
            self.theme = json.load(f)

        self.zoom = self.config['zoom']

    def set_lexer(self):
        '''设置词法分析器'''
        self.lexer.setDefaultPaper(
            QtGui.QColor(self.theme['theme']['default'][1]))
        self.lexer.setDefaultColor(
            QtGui.QColor(self.theme['theme']['default'][0]))

        for i in range(len(self.lexer.styles)):
            styles = self.theme['theme'][self.lexer.styles[i]]
            self.lexer.setColor(QtGui.QColor(styles[0]), i)
            self.lexer.setPaper(QtGui.QColor(styles[1]), i)
            font = QtGui.QFont(styles[2], styles[3])
            font.setBold(styles[4])
            font.setItalic(styles[5])
            self.lexer.setFont(font, i)

    def set_config(self, key: str, obj, append: bool = False):
        if key:
            if append:
                self.config[key].append(obj)
            else:
                self.config[key] = obj
            
            with open(self.config_file, 'w', encoding='UTF-8') as f:
                json.dump(self.config,f,ensure_ascii=False,indent=4)
            self.load_config()