import sys
import os
import keyword
import re
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import Qsci
app = QtWidgets.QApplication(sys.argv)

ed = Qsci.QsciScintilla()
lp = Qsci.QsciLexerPython(ed)

print(lp.wordCharacters())
Qsci.QsciScintilla.fold