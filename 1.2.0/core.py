#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import GUI
import copy
import tempfile
import debug
import time
from pathlib import Path
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import Qsci


class core(GUI.mainWin):
    def __init__(self):
        super().__init__()
        self.is_save = True
        self.setConnect()

        self.file_name: str = ''

        self.os = 'linux'

        self.tool_dict: dict = dict()
        self.tool_update = False
        self.debuger = object()

    def init_os(self):
        if self.os == 'win32':
            self.tmp = '%s/SailPYE/' % os.environ['temp']
        elif self.os == 'linux':
            self.tmp = '/tmp/SailPYE/'

    def temp_file(self, suffix=''):
        if suffix == '':
            return tempfile.mktemp(dir=self.tmp)
        return tempfile.mktemp(dir=self.tmp, suffix=suffix)

    def setConnect(self):
        '''绑定槽'''
        self.A_new.triggered.connect(self.new_file)
        self.A_open.triggered.connect(self.open_file)
        self.A_save.triggered.connect(self.save_file)
        self.A_saveas.triggered.connect(self.save_as_file)
        self.A_set.triggered.connect(self.setWin_show)
        self.A_quit.triggered.connect(self.is_exit)
        self.A_undo.triggered.connect(self.undo)
        self.A_redo.triggered.connect(self.redo)
        self.A_copy.triggered.connect(self.copy)
        self.A_cut.triggered.connect(self.cut)
        self.A_paste.triggered.connect(self.paste)
        self.A_del.triggered.connect(self.delete)
        self.A_wrap.triggered.connect(self.warp)
        self.A_info_bar.triggered.connect(self.info_bar)
        self.A_run.triggered.connect(self.run)
        self.A_add_tools.triggered.connect(self.add_tool)
        self.A_pydoc.triggered.connect(self.pydoc)
        self.A_help.triggered.connect(self.app_help)
        self.A_about.triggered.connect(self.about)
        self.A_aboutQT.triggered.connect(QtWidgets.QApplication.aboutQt)

        self.editor.cursorPositionChanged.connect(self.update_status)
        self.editor.marginClicked.connect(self.set_break)
        self.editor.textChanged.connect(self.text_changed)

    def text_changed(self):
        pos = self.editor.getCursorPosition()
        pos = self.editor.positionFromLineIndex(pos[0],pos[1])
        char = self.editor.text(pos,pos+1)
        symbol = [' ','.','(','@','[','\'','"',',','\n']
        if char in symbol:
            self.editor.beginUndoAction()
            self.editor.endUndoAction()
        

    def update_status(self, line, col):

        self.status_left_label.setText('行：%d，列:%d    ' % (line+1, col+1))

    def set_break(self, margin, line, state):
        if margin == 1 or margin == 0:
            if self.editor.markersAtLine(line) == 1:
                self.editor.markerDelete(line, 0)
            elif self.editor.markersAtLine(line) == 0:
                self.editor.markerAdd(line, 0)

    def new_file(self):
        print(sys._getframe().f_code.co_name)
        opinion = self.check_save()
        if opinion != 0:
            self.editor.setText('')
        self.editor.setModified(False)

    def open_file(self, file_name=''):
        print(sys._getframe().f_code.co_name)
        if file_name != '' and type(file_name) == str:
            if not file_name.lower().endswith('.py'):
                QtWidgets.QMessageBox.critical(
                    self, '错误', '打开文件"%s"失败！该文件不是Python源代码文件！' % file_name)
                sys.exit('10 打开的文件不是Python源代码文件')
            self.file_name = file_name
            self.setWindowTitle(self.file_name+' - Sail Pyton Editor')
            if not os.path.isfile(file_name):
                return
            with open(self.file_name, 'r', encoding='UTF-8') as f:
                self.editor.setText(f.read())
            return
        opinion = self.check_save()
        if opinion != 0:
            self.file_name = str(QtWidgets.QFileDialog.getOpenFileName(
                self, '打开..', '', 'Python源文件(*.py)')[0]).strip()
            if self.file_name != '':
                with open(self.file_name, 'r', encoding='UTF-8') as f:
                    self.editor.setText(f.read())
                self.setWindowTitle(self.file_name+' - Sail Pyton Editor')
        self.editor.setModified(False)

    def save_file(self):
        self.check_save(True)

    def save_as_file(self):
        print(sys._getframe().f_code.co_name)
        self.check_save(True, True)

    def setWin_show(self):
        print(sys._getframe().f_code.co_name)
        QtWidgets.QMessageBox.information(
            self, '提示', '请打开配置文件"%s/json/config.json"，按照帮助文件修改！' % sys.path[0])

    def is_exit(self):
        self.close()

    def undo(self):
        print(sys._getframe().f_code.co_name)
        self.editor.undo()

    def redo(self):
        print(sys._getframe().f_code.co_name)
        self.editor.redo()

    def copy(self):
        self.editor.copy()

    def cut(self):
        print(sys._getframe().f_code.co_name)
        self.editor.cut()

    def paste(self):
        print(sys._getframe().f_code.co_name)
        self.editor.paste()

    def delete(self):
        print(sys._getframe().f_code.co_name)
        self.editor.removeSelectedText()

    def select_all(self):
        print(sys._getframe().f_code.co_name)
        self.editor.selectAll()

    def warp(self):
        if self.A_wrap.isChecked():
            self.editor.setWrapMode(self.editor.WrapWord)
            self.config.set_config('warp', True, False)
        else:
            self.editor.setWrapMode(self.editor.WrapNone)
            self.config.set_config('warp', False, False)

    def run(self):
        """运行Python脚本"""
        # 把运行键停用，避免多次运行
        self.A_run.setEnabled(False)

        # 调出输出栏
        if not self.A_info_bar.isChecked():
            self.dockWidget.setVisible(True)
            self.A_info_bar.toggle()
        self.dockWidget.repaint()
        self.repaint()
        self.textEdit.setText('')

        error = ''

        self.debuger = debug.Debug(self.os, self.textEdit, self.tmp)

        # 建立临时文件夹作为工作目录
        if not Path(self.tmp).is_dir():
            os.mkdir(self.tmp)

        if self.file_name == '':
            # 如果是作为临时文件运行
            temp_file = open(tempfile.mktemp(
                dir=self.tmp, suffix='.py'),
                encoding='UTF-8', mode='w')
            temp_file.write(self.editor.text())
            temp_file.close()
            error = self.debuger.start(temp_file.name)
            os.remove(temp_file.name)
        else:
            # 如果是打开的文件，那么运行之前会保存一遍
            self.save_file()
            error = self.debuger.start(self.file_name)

        self.add_log('调试完毕！')
        if error:
            self.add_log(error)

        self.A_run.setEnabled(True)

    def add_log(self, text):
        self.textEdit.append(text)
        self.textEdit.repaint()

    def add_tool(self):
        print(sys._getframe().f_code.co_name)
        tools_win = GUI.toolsWin(self, self.config, self.tool_dict.keys())
        tools_win.show()
        tools_win.exec()
        self.update_tools()

    def app_help(self):
        print(sys._getframe().f_code.co_name)

    def pydoc(self):
        print(sys._getframe().f_code.co_name)
        if self.os == 'win32':
            os.system('cmd /c start python -m pydoc -b')
        elif self.os == 'linux':
            os.system('gnome-terminal -e "pydoc3 -b"')

    def about(self):
        print(sys._getframe().f_code.co_name)
        GUI.aboutWin(self).show()

    def check_save(self, is_save=False, save_as=False):
        '''寻问文件是否需要保存，如果需要则弹出提示框\n
        返回值：0表示取消操作，1表示已经保存，2表示不保存'''
        opinion = 0
        if self.editor.isModified():
            if not is_save:
                # 寻问是否需要保存
                opinion = saveMessageBox(self).get_opinion()

        if opinion == 0 and self.editor.text() != '' or is_save == True:
            # 选择保存
            if self.file_name == '' or save_as:
                # 当文件没有保存过，需要寻问保存位置
                self.file_name = str(QtWidgets.QFileDialog.getSaveFileName(
                    self, '另存为..' if save_as else '保存', '', 'Python源文件(*.py)')[0]).strip()

            if self.file_name != '':
                with open(self.file_name, 'w', encoding='UTF-8') as f:
                    f.write(self.editor.text())
                self.setWindowTitle(self.file_name+' - Sail Pyton Editor')
                self.editor.setModified(False)
                return 1
            else:
                return 0
        elif opinion == 1:
            return 2
        elif opinion == 2:
            return 0
        else:
            self.editor.setModified(False)
            return 1

    def closeEvent(self, event):
        """改写窗口即将关闭信号"""
        if self.check_save() == 0:
            event.ignore()
        else:
            event.accept()

    def update_tools(self):
        '''更新工具
           ErrorCode-40
           ErrorCode-41
        '''
        if self.tool_update:
            for key in self.tool_dict.keys():
                self.M_tools.removeAction(self.tool_dict[key]['obj'])
        self.tool_dict.clear()
        tools = copy.deepcopy(self.config.config['tools'])
        for i in range(len(tools)):
            tool_dict = tools[i]
            if not 'name' in tool_dict:
                QtWidgets.QMessageBox.critical(
                    self, '错误', 'ErrorCode -40.%d，工具添加错误，在文件"%s"中，"tools"缺少"name"字段' % (self.config.config_file, i))
                sys.exit('ErrorCode -40.%d' % i)
            if tool_dict['name'] in self.tool_dict.keys():
                QtWidgets.QMessageBox.critical(
                    self, '错误', 'ErrorCode -41.%d，发现重复工具名"%s"，请检查文件文件"%s"，"tools"中的"name"字段！' % (i, tool_dict['name'], self.config.config_file))
                sys.exit('ErrorCode -41.%d' % i)
            if not 'command' in tool_dict:
                QtWidgets.QMessageBox.critical(
                    self, '错误', 'ErrorCode -42.%d，工具添加错误，在文件"%s"中，"tools"缺少"command"字段' % (self.config.config_file, i))
                sys.exit('ErrorCode -42.%d' % i)
            menu = QtWidgets.QAction(self)

            if self.os in tool_dict['command']:
                menu.setText(tool_dict['name'])
                tool_dict['cmd'] = tool_dict['command'][self.os]
                menu.setEnabled(True)
            else:
                menu.setText(tool_dict['name'] + '(不适用于当前操作系统)')
                menu.setEnabled(False)
            menu.setObjectName(tool_dict['name'])
            menu.triggered.connect(self.run_tool)

            if 'shortcut' in tool_dict:
                menu.setShortcut(tool_dict['shortcut'])
            tool_dict['obj'] = menu
            self.tool_dict[tool_dict['name']] = tool_dict
            self.M_tools.addAction(self.tool_dict[tool_dict['name']]['obj'])
        self.tool_update = True

    def run_tool(self):
        os.system(self.tool_dict[self.sender().objectName()]['cmd'])

    def info_bar(self):
        self.dockWidget.setVisible(self.A_info_bar.isChecked())


class saveMessageBox(QtWidgets.QMessageBox):
    """生成一个保存提问窗口"""

    def __init__(self, w):
        super().__init__(w)
        self.setIcon(QtWidgets.QMessageBox.Question)
        self.setWindowTitle('保存')
        self.setText('<font size = "5">是否保存已更改的内容？</font>')
        self.y = self.addButton('保存(&S)', QtWidgets.QMessageBox.YesRole)
        self.y = self.addButton('不保存(&N)', QtWidgets.QMessageBox.NoRole)
        self.r = self.addButton('取消', QtWidgets.QMessageBox.RejectRole)

    def get_opinion(self):
        self.show()
        return(self.exec_())
