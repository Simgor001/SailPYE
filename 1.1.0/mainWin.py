# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SailPYE-EDU\3-22\mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.M_file = QtWidgets.QMenu(self.menubar)
        self.M_file.setObjectName("M_file")
        self.M_edit = QtWidgets.QMenu(self.menubar)
        self.M_edit.setObjectName("M_edit")
        self.M_build = QtWidgets.QMenu(self.menubar)
        self.M_build.setObjectName("M_build")
        self.M_tools = QtWidgets.QMenu(self.menubar)
        self.M_tools.setObjectName("M_tools")
        self.M_help = QtWidgets.QMenu(self.menubar)
        self.M_help.setObjectName("M_help")
        self.M_view = QtWidgets.QMenu(self.menubar)
        self.M_view.setObjectName("M_view")
        self.M_task = QtWidgets.QMenu(self.menubar)
        self.M_task.setObjectName("M_task")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.A_new = QtWidgets.QAction(MainWindow)
        self.A_new.setObjectName("A_new")
        self.A_open = QtWidgets.QAction(MainWindow)
        self.A_open.setObjectName("A_open")
        self.A_save = QtWidgets.QAction(MainWindow)
        self.A_save.setObjectName("A_save")
        self.A_saveas = QtWidgets.QAction(MainWindow)
        self.A_saveas.setObjectName("A_saveas")
        self.A_quit = QtWidgets.QAction(MainWindow)
        self.A_quit.setObjectName("A_quit")
        self.A_undo = QtWidgets.QAction(MainWindow)
        self.A_undo.setObjectName("A_undo")
        self.A_redo = QtWidgets.QAction(MainWindow)
        self.A_redo.setObjectName("A_redo")
        self.A_cut = QtWidgets.QAction(MainWindow)
        self.A_cut.setObjectName("A_cut")
        self.A_copy = QtWidgets.QAction(MainWindow)
        self.A_copy.setObjectName("A_copy")
        self.A_paste = QtWidgets.QAction(MainWindow)
        self.A_paste.setObjectName("A_paste")
        self.A_all = QtWidgets.QAction(MainWindow)
        self.A_all.setObjectName("A_all")
        self.A_run = QtWidgets.QAction(MainWindow)
        self.A_run.setObjectName("A_run")
        self.A_compile = QtWidgets.QAction(MainWindow)
        self.A_compile.setObjectName("A_compile")
        self.A_pack = QtWidgets.QAction(MainWindow)
        self.A_pack.setObjectName("A_pack")
        self.A_content = QtWidgets.QAction(MainWindow)
        self.A_content.setCheckable(False)
        self.A_content.setEnabled(True)
        self.A_content.setObjectName("A_content")
        self.A_task = QtWidgets.QAction(MainWindow)
        self.A_task.setEnabled(False)
        self.A_task.setObjectName("A_task")
        self.A_work = QtWidgets.QAction(MainWindow)
        self.A_work.setEnabled(False)
        self.A_work.setObjectName("A_work")
        self.A_add_tools = QtWidgets.QAction(MainWindow)
        self.A_add_tools.setObjectName("A_add_tools")
        self.A_pydoc = QtWidgets.QAction(MainWindow)
        self.A_pydoc.setObjectName("A_pydoc")
        self.A_help = QtWidgets.QAction(MainWindow)
        self.A_help.setObjectName("A_help")
        self.A_about = QtWidgets.QAction(MainWindow)
        self.A_about.setObjectName("A_about")
        self.A_set = QtWidgets.QAction(MainWindow)
        self.A_set.setObjectName("A_set")
        self.A_del = QtWidgets.QAction(MainWindow)
        self.A_del.setObjectName("A_del")
        self.A_wrap = QtWidgets.QAction(MainWindow)
        self.A_wrap.setCheckable(True)
        self.A_wrap.setObjectName("A_wrap")
        self.A_p = QtWidgets.QAction(MainWindow)
        self.A_p.setObjectName("A_p")
        self.A_m = QtWidgets.QAction(MainWindow)
        self.A_m.setObjectName("A_m")
        self.A_font = QtWidgets.QAction(MainWindow)
        self.A_font.setObjectName("A_font")
        self.A_rest = QtWidgets.QAction(MainWindow)
        self.A_rest.setObjectName("A_rest")
        self.A_add_plugin = QtWidgets.QAction(MainWindow)
        self.A_add_plugin.setObjectName("A_add_plugin")
        self.A_info_bar = QtWidgets.QAction(MainWindow)
        self.A_info_bar.setCheckable(True)
        self.A_info_bar.setObjectName("A_info_bar")
        self.M_file.addAction(self.A_new)
        self.M_file.addAction(self.A_open)
        self.M_file.addAction(self.A_save)
        self.M_file.addAction(self.A_saveas)
        self.M_file.addSeparator()
        self.M_file.addAction(self.A_set)
        self.M_file.addSeparator()
        self.M_file.addAction(self.A_quit)
        self.M_edit.addAction(self.A_undo)
        self.M_edit.addAction(self.A_redo)
        self.M_edit.addSeparator()
        self.M_edit.addAction(self.A_cut)
        self.M_edit.addAction(self.A_copy)
        self.M_edit.addAction(self.A_paste)
        self.M_edit.addAction(self.A_del)
        self.M_edit.addSeparator()
        self.M_edit.addAction(self.A_all)
        self.M_build.addAction(self.A_run)
        self.M_tools.addAction(self.A_add_tools)
        self.M_tools.addSeparator()
        self.M_help.addAction(self.A_pydoc)
        self.M_help.addAction(self.A_help)
        self.M_help.addSeparator()
        self.M_help.addAction(self.A_about)
        self.M_view.addAction(self.A_wrap)
        self.M_view.addAction(self.A_info_bar)
        self.M_task.addAction(self.A_task)
        self.M_task.addAction(self.A_work)
        self.menubar.addAction(self.M_file.menuAction())
        self.menubar.addAction(self.M_edit.menuAction())
        self.menubar.addAction(self.M_view.menuAction())
        self.menubar.addAction(self.M_task.menuAction())
        self.menubar.addAction(self.M_build.menuAction())
        self.menubar.addAction(self.M_tools.menuAction())
        self.menubar.addAction(self.M_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sail Python Editor"))
        self.M_file.setTitle(_translate("MainWindow", "文件(&F)"))
        self.M_edit.setTitle(_translate("MainWindow", "编辑(&E)"))
        self.M_build.setTitle(_translate("MainWindow", "构建(&B)"))
        self.M_tools.setTitle(_translate("MainWindow", "工具(&T)"))
        self.M_help.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.M_view.setTitle(_translate("MainWindow", "视图(&V)"))
        self.M_task.setTitle(_translate("MainWindow", "任务(&S)"))
        self.A_new.setText(_translate("MainWindow", "新建(&N)"))
        self.A_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.A_open.setText(_translate("MainWindow", "打开(&O)..."))
        self.A_open.setToolTip(_translate("MainWindow", "打开"))
        self.A_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.A_save.setText(_translate("MainWindow", "保存(&S)"))
        self.A_save.setToolTip(_translate("MainWindow", "保存"))
        self.A_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.A_saveas.setText(_translate("MainWindow", "另存为(&A)..."))
        self.A_saveas.setToolTip(_translate("MainWindow", "另存为"))
        self.A_saveas.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.A_quit.setText(_translate("MainWindow", "退出(&X)"))
        self.A_quit.setToolTip(_translate("MainWindow", "退出"))
        self.A_undo.setText(_translate("MainWindow", "撤销(&U)"))
        self.A_undo.setToolTip(_translate("MainWindow", "撤销"))
        self.A_undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.A_redo.setText(_translate("MainWindow", "重做(&R)"))
        self.A_redo.setToolTip(_translate("MainWindow", "重做"))
        self.A_redo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.A_cut.setText(_translate("MainWindow", "剪切(&T)"))
        self.A_cut.setToolTip(_translate("MainWindow", "剪切"))
        self.A_cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.A_copy.setText(_translate("MainWindow", "复制(C&)"))
        self.A_copy.setToolTip(_translate("MainWindow", "复制"))
        self.A_copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.A_paste.setText(_translate("MainWindow", "粘贴(&P)"))
        self.A_paste.setToolTip(_translate("MainWindow", "粘贴"))
        self.A_paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.A_all.setText(_translate("MainWindow", "全选(&A)"))
        self.A_all.setToolTip(_translate("MainWindow", "全选"))
        self.A_all.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.A_run.setText(_translate("MainWindow", "运行(&R)"))
        self.A_run.setToolTip(_translate("MainWindow", "运行"))
        self.A_run.setShortcut(_translate("MainWindow", "F5"))
        self.A_compile.setText(_translate("MainWindow", "编译为PYC文件(&C)"))
        self.A_compile.setToolTip(_translate("MainWindow", "编译为PYC文件"))
        self.A_compile.setShortcut(_translate("MainWindow", "F7"))
        self.A_pack.setText(_translate("MainWindow", "打包成EXE文件(&P)"))
        self.A_pack.setShortcut(_translate("MainWindow", "Ctrl+F7"))
        self.A_content.setText(_translate("MainWindow", "本节课的学习内容(&C)"))
        self.A_content.setToolTip(_translate("MainWindow", "本节课的学习内容"))
        self.A_task.setText(_translate("MainWindow", "任务内容(&T)"))
        self.A_task.setToolTip(_translate("MainWindow", "任务内容"))
        self.A_work.setText(_translate("MainWindow", "提交作业(&U)"))
        self.A_work.setToolTip(_translate("MainWindow", "提交作业"))
        self.A_add_tools.setText(_translate("MainWindow", "添加工具(&A)..."))
        self.A_add_tools.setToolTip(_translate("MainWindow", "添加工具"))
        self.A_pydoc.setText(_translate("MainWindow", "Python文档(&H)"))
        self.A_pydoc.setToolTip(_translate("MainWindow", "Python文档"))
        self.A_pydoc.setShortcut(_translate("MainWindow", "F1"))
        self.A_help.setText(_translate("MainWindow", "软件帮助(&S)"))
        self.A_help.setToolTip(_translate("MainWindow", "软件帮助"))
        self.A_about.setText(_translate("MainWindow", "关于 Sail Python Editor(&A)"))
        self.A_about.setToolTip(_translate("MainWindow", "关于 Sail Python Editor"))
        self.A_set.setText(_translate("MainWindow", "首选项(&S)"))
        self.A_set.setToolTip(_translate("MainWindow", "首选项"))
        self.A_del.setText(_translate("MainWindow", "删除(&L)"))
        self.A_del.setToolTip(_translate("MainWindow", "删除"))
        self.A_del.setShortcut(_translate("MainWindow", "Del"))
        self.A_wrap.setText(_translate("MainWindow", "自动换行(&W)"))
        self.A_wrap.setToolTip(_translate("MainWindow", "自动换行"))
        self.A_p.setText(_translate("MainWindow", "放大视图(&I)"))
        self.A_p.setToolTip(_translate("MainWindow", "放大视图"))
        self.A_p.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.A_m.setText(_translate("MainWindow", "缩小视图(&O)"))
        self.A_m.setToolTip(_translate("MainWindow", "缩小视图"))
        self.A_m.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.A_font.setText(_translate("MainWindow", "字体(&F)..."))
        self.A_font.setToolTip(_translate("MainWindow", "字体"))
        self.A_rest.setText(_translate("MainWindow", "还原视图"))
        self.A_rest.setToolTip(_translate("MainWindow", "还原视图"))
        self.A_rest.setShortcut(_translate("MainWindow", "Ctrl+0"))
        self.A_add_plugin.setText(_translate("MainWindow", "添加插件(&P)..."))
        self.A_info_bar.setText(_translate("MainWindow", "调试输出"))
