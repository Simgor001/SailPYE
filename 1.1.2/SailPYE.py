import core
import sys
import os
import ctypes
import setPlugin
import threading
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from pathlib import Path
verstion = '1.1.1'

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    app.setWindowIcon(QtGui.QIcon('img/logo.png'))
    app.setAttribute(QtCore.Qt.AA_DisableWindowContextHelpButton)
    print('正在启动...')
    SailPYE = core.core()

    if sys.platform.startswith('win'):
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "Sail Python Editor")
        SailPYE.os = 'win32'
    SailPYE.init_os()

    # 建立临时文件夹作为工作目录
    if not Path(SailPYE.tmp).is_dir():
        os.mkdir(SailPYE.tmp)

    print('正在启动插件...')
    plugin = setPlugin.plugin(SailPYE, app, verstion)

    error_info = plugin.install()
    error_widget = QtWidgets.QMessageBox(
        QtWidgets.QMessageBox.Critical, '错误', error_info)

    if error_info != '':
        SailPYE.close()
        error_widget.show()
        sys.exit(app.exec_())

    SailPYE.update_tools()

    if len(sys.argv) > 1:
        
        SailPYE.open_file(sys.argv[1])
    
    SailPYE.show()

    print('启动成功！')

    def show_init():
        for fun in plugin.plugins:
            fun['obj'].show_init()


    threading.Thread(target=show_init).start()

    sys.exit(app.exec_())


if __name__ == "__main__":
    os.chdir(sys.argv[0] + '/../')
    main()
