from config import Config
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import Qsci
from mainWin import Ui_MainWindow
from aboutWin import Ui_aboutWin
from toolsWin import Ui_toolsWin


class editor(Qsci.QsciScintilla):
    completion_p = False
    completion_b = False
    completion_s = False
    completion_d = False
    open_file = QtCore.pyqtSignal(str)
    message = QtCore.pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)

    '''
    def keyPressEvent(self, event):
        ex = [3,4,6,7,13,16,17,18,19]
        key = event.key()
        line = self.getCursorPosition()[0]
        col = self.getCursorPosition()[1]
        previous_style = 0
        if self.positionFromLineIndex(line, col) > 0:
            previous_style = self.SendScintilla(
                self.SCI_GETSTYLEAT, self.positionFromLineIndex(line, col)-1)
        if previous_style in ex:
            self.completion_p = False
            self.completion_b = False
            self.completion_s = False
            self.completion_d = False
            super().keyPressEvent(event)
            return
        elif key == QtCore.Qt.Key_ParenLeft:
            self.insert(')')
            self.completion_p = True
            self.completion_b = False
            self.completion_s = False
            self.completion_d = False
        elif key == QtCore.Qt.Key_ParenRight and self.completion_p:
            self.setCursorPosition(line, col+1)
            self.completion_p = False
            return
        elif key == QtCore.Qt.Key_BracketLeft:
            self.insert(']')
            self.completion_p = False
            self.completion_b = True
            self.completion_s = False
            self.completion_d = False
        elif key == QtCore.Qt.Key_BracketRight and self.completion_b:
            self.setCursorPosition(line, col+1)
            self.completion_b = False
            return
        elif key == QtCore.Qt.Key_QuoteDbl:
            if self.completion_d:
                self.completion_d = False
                self.setCursorPosition(line, col+1)
                return
            else:
                if self.selectedText() != '':
                    text = '"'+self.selectedText()+'"'
                    self.replaceSelectedText(text)
                    return
                else:
                    
                    self.insert('"')

                    self.completion_p = False
                    self.completion_b = False
                    self.completion_s = False
                    self.completion_d = True

        elif key == QtCore.Qt.Key_Apostrophe:
            if self.completion_s:
                self.completion_s = False
                self.setCursorPosition(line, col+1)
                return
            else:
                if self.selectedText() != '':
                    print('y')
                    text = "'"+self.selectedText()+"'"
                    self.replaceSelectedText(text)
                    return
                else:
                    
                    self.insert("'")

                    self.completion_p = False
                    self.completion_b = False
                    self.completion_s = True
                    self.completion_d = False

        else:
            self.completion_p = False
            self.completion_b = False
            self.completion_s = False
            self.completion_d = False
        super().keyPressEvent(event)'''

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):
        super().dragEnterEvent(event)
        data: QtCore.QMimeData = event.mimeData()
        if data.hasUrls() and len(data.urls()) > 0:
            url = data.urls()[0].toString().replace('file:///', '', 1)
            if url.lower().endswith('.py') or url.lower().endswith('.pyw') or url.lower().endswith('.json'):
                event.accept()
                return
        elif data.hasText():
            event.accept()
            return

        event.ignore()

    def dropEvent(self, event):
        super().dropEvent(event)
        data: QtCore.QMimeData = event.mimeData()
        if data.hasUrls() and len(data.urls()) > 0:
            url = data.urls()[0].toString().replace('file:///', '', 1)
            self.open_file.emit(url)


class mainWin(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.set_editor(self.config.lexer)
        self.set_info_bar()

    def setupUi(self, MainWindow):
        super().setupUi(self)
        self.setWindowTitle('Sail Python Editor')

        self.editor = editor(self)
        self.setCentralWidget(self.editor)

        self.config = Config(self, self.editor)

        # 设置状态栏

        self.status_left = QtWidgets.QLabel(self)
        self.statusBar.addWidget(self.status_left)

        self.status_right_label = QtWidgets.QLabel(self)
        self.status_right_label.setText('行：1，列:1    ')
        self.statusBar.addPermanentWidget(self.status_right_label)
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

    def set_editor(self, lexer):
        # 设置词法分析器
        self.editor.setLexer(lexer)
        self.config.set_lexer()
        # 设置utf-8编码
        self.editor.setUtf8(True)

        # 设置行尾模式为unix模式
        self.editor.setEolMode(Qsci.QsciScintilla.EolUnix)

        # 设置缩放
        self.editor.zoomTo(self.config.zoom)

        # 设置指示器颜色
        self.editor.setIndicatorForegroundColor(QtCore.Qt.red)

        # 设置括号匹配
        self.editor.setBraceMatching(Qsci.QsciScintilla.StrictBraceMatch)

        self.editor.setMatchedBraceBackgroundColor(QtGui.QColor(
            self.config.theme['other']['matchedBraceBackgroundColor']))
        self.editor.setMatchedBraceForegroundColor(QtGui.QColor(
            self.config.theme['other']['matchedBraceForegroundColor']))

        self.editor.setUnmatchedBraceIndicator(0)
        self.editor.setUnmatchedBraceBackgroundColor(QtGui.QColor(
            self.config.theme['other']['unmatchedBraceBackgroundColor']))
        self.editor.setUnmatchedBraceForegroundColor(QtGui.QColor(
            self.config.theme['other']['unmatchedBraceForegroundColor']))

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
        self.editor.setSelectionForegroundColor(
            QtGui.QColor(
                self.config.theme['other']['selectionForegroundColor']))
        # 设置旁注栏
        self.editor.setMarginsBackgroundColor(
            QtGui.QColor(self.config.theme['margins'][1]))
        self.editor.setMarginsForegroundColor(
            QtGui.QColor(self.config.theme['margins'][0]))
        self.editor.setMarginSensitivity(1, True)
        self.editor.setMarginSensitivity(0, True)
        self.editor.setMarginLineNumbers(0, False)
        self.editor.setMarginWidth(0, 20)
        font = QtGui.QFont(self.config.theme['margins'][2],self.config.theme['margins'][3])
        font.setBold(self.config.theme['margins'][4])
        font.setItalic(self.config.theme['margins'][5])
        self.editor.setMarginsFont(font)

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
        # 设置拖放组件
        self.editor.setAcceptDrops(True)
        #self.drag = QtGui.QDrag(self.editor)
        # self.drag.setDragCursor(QtGui.QPixmap(),QtCore.Qt.ActionMask)

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

        # 去掉焦点框
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)

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
        #self.setWindowFlags(self.windowFlags() &~ QtCore.Qt.WindowContextHelpButtonHint)


class toolsWin(QtWidgets.QDialog, Ui_toolsWin):
    def __init__(self, parent, config, keys):
        super().__init__(parent)
        self.setupUi(self)
        self.config: Config = config
        self.keys = keys
        self.buttonBox.accepted.connect(self.ok)
        self.setFixedSize(self.width(), self.height())
        #self.setWindowFlags(self.windowFlags() &~ QtCore.Qt.WindowContextHelpButtonHint)

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
