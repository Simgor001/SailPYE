#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: 某不明生物
# @since: 2020-02-22 19:27
# @lastTime: 2020-02-26 17:56
# @FilePath: /SailPYE/GUI.py
# @Description:


from config import Config
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import Qsci
from mainWin import Ui_MainWindow
from aboutWin import Ui_aboutWin
from toolsWin import Ui_toolsWin


class mainWin(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.set_editor()
        self.set_info_bar()

    def setupUi(self, MainWindow):
        super(mainWin, self).setupUi(self)
        self.setWindowTitle('Sail Pyton Editor')

        self.editor = Qsci.QsciScintilla(self)
        self.setCentralWidget(self.editor)

        self.config = Config(self, self.editor)

        # 设置状态栏
        self.status_left_label = QtWidgets.QLabel(self)
        self.status_left_label.setText('行：1，列:1    ')
        self.statusBar.addPermanentWidget(self.status_left_label)

        palette = QtGui.QPalette()
        palette.setBrush(palette.Background,
                         QtGui.QColor(self.config.theme['other']
                                      ['statusBarBackgroundColor']))
        palette.setColor(palette.Foreground,
                         QtGui.QColor(self.config.theme['other']
                                      ['statusBarForegroundColor']))
        self.statusBar.setAutoFillBackground(True)
        self.statusBar.setPalette(palette)

        if self.config.config['warp'] ^ self.A_wrap.isChecked():
            self.A_wrap.toggle()
            # 设置自动换行
            self.editor.setWrapMode(Qsci.QsciScintilla.WrapWord)
        if self.A_info_bar.isChecked():
            self.A_info_bar.toggle()

    def set_editor(self):
        # 设置词法分析器
        self.editor.setLexer(self.config.lexer)

        # 设置utf-8编码
        self.editor.setUtf8(True)

        # 设置缩放
        self.editor.zoomTo(self.config.zoom)

        # 设置光标
        self.editor.setCaretForegroundColor(
            QtGui.QColor(self.config.theme['other']['cursorColor']))
        self.editor.setCaretLineBackgroundColor(
            QtGui.QColor(self.config.theme['other']['cursorLineColor']))
        self.editor.setCaretLineVisible(True)
        self.editor.setCaretWidth(2)

        self.editor.setSelectionBackgroundColor(
            QtGui.QColor(
                self.config.theme['other']['selectionBackgroundColor']))

        # 设置旁注栏
        self.editor.setMarginsBackgroundColor(
            QtGui.QColor(self.config.theme['other']['marginsBackgroundColor']))
        self.editor.setMarginsForegroundColor(
            QtGui.QColor(self.config.theme['other']['marginsForegroundColor']))
        self.editor.setMarginSensitivity(1, True)
        self.editor.setMarginSensitivity(0, True)
        self.editor.setMarginLineNumbers(0, False)
        self.editor.setMarginWidth(0, 20)

        self.editor.setMarginType(1, self.editor.SymbolMargin)
        self.editor.setMarginWidth(1, 11)
        '''
        self.editor.markerDefine(self.editor.Circle, 0)
        self.editor.setMarkerForegroundColor(
            QtGui.QColor(self.config.theme['other']
                         ['breakpointBackgroundColor']), 0)
        self.editor.setMarkerBackgroundColor(
            QtGui.QColor(self.config.theme['other']
                         ['breakpointForegroundColor']), 0)
        '''
        self.editor.setMarginType(2, self.editor.NumberMargin)
        self.editor.setMarginWidth(2, "000")

        # 设置缩进
        self.editor.setIndentationsUseTabs(False)
        self.editor.setTabWidth(4)
        self.editor.setAutoIndent(True)

        self.editor.setTabIndents(True)
        self.editor.setBackspaceUnindents(True)

        self.editor.setIndentationGuides(True)
        self.editor.setIndentationGuidesBackgroundColor(
            QtGui.QColor(self.config.theme['other']
                         ['indentationGuidesBackgroundColor']))
        self.editor.setIndentationGuidesForegroundColor(
            QtGui.QColor(self.config.theme['other']
                         ['indentationGuidesForegroundColor']))

        # 去掉焦点框
        self.editor.setFrameShape(QtWidgets.QFrame.NoFrame)

    def set_info_bar(self):
        self.dockWidget = dockWidget('  调试输出', self)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.dockWidget)
        self.textEdit = QtWidgets.QTextEdit(self.dockWidget)
        self.dockWidget.setWidget(self.textEdit)
        palette = QtGui.QPalette()

        palette.setBrush(palette.Background,
                         QtGui.QColor(self.config.theme['other']
                                      ['dockBarBackgroundColor']))
        palette.setColor(palette.Foreground,
                         QtGui.QColor(self.config.theme['other']
                                      ['dockBarForegroundColor']))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        palette.setColor(palette.Text,
                         QtGui.QColor(self.config.theme['outText'][0]))
        palette.setColor(palette.Base,
                         QtGui.QColor(self.config.theme['outText'][1]))
        font = QtGui.QFont(self.config.theme['outText'][2],
                           self.config.theme['outText'][3])
        font.setBold(self.config.theme['outText'][4])
        font.setItalic(self.config.theme['outText'][5])
        self.textEdit.setFont(font)

        self.textEdit.setPalette(palette)
        self.textEdit.setReadOnly(True)

        self.textEdit.textChanged.connect(self.auto_scroll)

    def auto_scroll(self):
        self.textEdit.moveCursor(QtGui.QTextCursor.End)


class aboutWin(QtWidgets.QDialog, Ui_aboutWin):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        pix = QtGui.QPixmap('img/logo.png')
        self.label_2.setPixmap(pix.scaled(
            self.label_2.size(),
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.FastTransformation))
        self.setFixedSize(self.width(), self.height())


class toolsWin(QtWidgets.QDialog, Ui_toolsWin):
    def __init__(self, parent, config, keys):
        super().__init__(parent)
        self.setupUi(self)
        self.config: Config = config
        self.keys = keys
        self.buttonBox.accepted.connect(self.ok)
        self.setFixedSize(self.width(), self.height())

    def ok(self):
        if not self.T_name.text():
            QtWidgets.QMessageBox.warning(self, "提示", '请输入工具名称！')
            return

        if self.T_name.text() in self.keys:
            QtWidgets.QMessageBox.warning(self, "提示", '该工具名已使用，请重新输入工具名！')
            self.T_name.selectAll()
            return
        if self.T_win32.text() or self.T_linux.text():
            tool = {
                'name': self.T_name.text(),
                'shortcut': self.keySequenceEdit.keySequence().toString(),
                'command': {
                    'win32': self.T_win32.text(),
                    'linux': self.T_linux.text()
                }

            }
            self.config.set_config('tools', tool, True)
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "提示", '请至少输入一种操作系统的命令！')
            return


class dockWidget(QtWidgets.QDockWidget):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.parent = parent
        self.setVisible(False)

    def closeEvent(self, event):
        """改写窗口即将关闭信号"""
        self.setVisible(False)
        self.parent.A_info_bar.toggle()
        event.ignore()
