import sys
import os
import keyword
import re
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import Qsci

# 造轮子，自己写一个Python词法分析器
class lexer(Qsci.QsciLexerCustom):
    class Sequence:
        def __init__(self,
                     start,
                     stop_sequences,
                     stop_characters,
                     style,
                     add_to_style):
            self.start = start
            self.stop_sequences = stop_sequences
            self.stop_characters = stop_characters
            self.style = style
            self.add_to_style = add_to_style

    # 这个是风格字典，切记不可以改变顺序
    styles = {
        "Default": 0,
        "Comment": 1,
        "Number": 2,
        "DoubleQuotedString": 3,
        "SingleQuotedString": 4,
        "Keyword": 5,
        "TripleSingleQuotedString": 6,
        "TripleDoubleQuotedString": 7,
        "ClassName": 8,
        "FunctionMethodName": 9,
        "Operator": 10,
        "Identifier": 11,
        "CommentBlock": 12,
        "UnclosedString": 13,
        "HighlightedIdentifier": 14,
        "Decorator": 15
    }

    keyword = keyword.kwlist
    keyword.append('super')

    functions = ['abs', 'all', 'any', 'ascii', 'bin', 'bool',
                 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr',
                 'classmethod', 'compile', 'complex', 'copyright',
                 'credits', 'delattr', 'dict', 'dir', 'divmod',
                 'enumerate', 'eval', 'exec', 'exit', 'filter',
                 'float', 'format', 'frozenset', 'getattr', 'globals',
                 'hasattr', 'hash', 'help', 'hex', 'id',
                 'input', 'int', 'isinstance', 'issubclass',
                 'iter', 'len', 'license', 'list', 'locals', 'map',
                 'max', 'memoryview', 'min', 'next', 'object', 'oct',
                 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range',
                 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
                 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple',
                 'type', 'vars', 'zip']

    def __init__(self, parent, theme):
        super().__init__(parent)
        self.theme = theme

    def keywords(self, _set):
        if _set == 1:
            return ' '.join(self.keyword)
        elif _set == 2:
            return ' '.join(self.functions)
        else:
            return ''

    def description(self, style):
        if style < 21:
            return self.styles[style]
        else:
            return ''

    def set_style(self):
        '''设置样式'''
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

    def styleText(self, start, end):
        self.startStyling(start)
        splitter = re.compile(r"(\{\.|\.\}|\#|\'|\"\"\"|\n|\s+|\w+|\W)")
        text = self.parent().text()[start:end]
        tokens = [(token, len(bytearray(token, "utf-8")))
                  for token in splitter.findall(text)]
        # (单词，长度)
        # Style the text in a loop
        for i, token in enumerate(tokens):
            if token[0] in self.keyword:
                print(token)
                # Keyword
                self.setStyling(token[1], self.styles['keyword'])
