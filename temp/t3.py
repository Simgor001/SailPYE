import sys
import os
import keyword
import re
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import Qsci
app = QtWidgets.QApplication(sys.argv)

ed = Qsci.QsciScintilla()
#lp = Qsci.QsciLexerCPP(ed)
lp = Qsci.QsciLexerCustom()
ed.setLexer(lp)
ed.show()
lp.setEditor(ed)
lp.setParent(ed)
ed.SendScintilla(Qsci.QsciScintilla.SCI_SETCODEPAGE,1)
ed.setText('//啊')
for i in range(0,128):
    
    ed.SendScintilla(Qsci.QsciScintilla.SCI_STYLESETCHARACTERSET,i, 134)
app.exec()