import sys
import os
import keyword
import re
from PyQt5 import QtCore
from PyQt5 import QtGui
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

    # 这个是风格字典，不可以改变顺序
    styles = {
        'default': 0,
        'comment': 1,
        'number': 2,
        'operator': 3,
        'decorator': 4,
        'constants': 5,
        'keyword': 6,
        'functions': 7,
        'otherKeyword': 8,
        'className': 9,
        'funName': 10,
        'unclosedString': 11,
        'doubleQuotedString': 12,
        'singleQuotedString': 13,
        'tripleSingleQuotedString': 14,
        'tripleDoubleQuotedString': 15
    }
    styles_keys = list(styles.keys())

    operator = ['!', '%', '^', '&', '+', '-', '*', '\\', '/', '|']

    constants = ['False', 'True', 'None', 'NotImplemented', 'Ellipsis']

    keyword = keyword.kwlist

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

    otherKeyword = ['self']

    def __init__(self, parent, theme):
        super().__init__(parent)
        self.theme = theme
        self.set_style()

    def keywords(self, _set):
        if _set == 1:
            return ' '.join(self.keyword)
        elif _set == 2:
            return ' '.join(self.functions)
        elif _set == 3:
            return ' '.join(self.styles_keys)
        else:
            return ''

    def language(self):
        return "Python"

    def description(self, style):
        if style < len(self.styles):
            return self.styles_keys[style]
        else:
            return ''

    def set_style(self):
        '''设置样式'''
        if 'default' in self.theme:

            self.setDefaultColor(
                QtGui.QColor(self.theme['default'][0]))
            self.setDefaultPaper(
                QtGui.QColor(self.theme['default'][1]))
            font = QtGui.QFont(self.theme['default'][2],
                               self.theme['default'][3])
            font.setBold(self.theme['default'][4])
            font.setItalic(self.theme['default'][5])
            self.setDefaultFont(font)
        else:
            self.setDefaultColor(self.defaultColor())
            self.setDefaultPaper(self.defaultPaper())

        for i in range(len(self.styles)):

            if self.styles_keys[i] in self.theme:
                styles = self.theme[self.styles_keys[i]]
                self.setColor(QtGui.QColor(styles[0]), i)
                self.setPaper(QtGui.QColor(styles[1]), i)
                font = QtGui.QFont(styles[2], styles[3])
                font.setBold(styles[4])
                font.setItalic(styles[5])
                self.setFont(font, i)
                #self.parent().SendScintilla(
                #    Qsci.QsciScintilla.SCI_STYLESETCHARACTERSET,
                #    i, Qsci.QsciScintilla.SC_CHARSET_SYMBOL)
            else:
                self.setColor(self.defaultColor(), i)
                self.setPaper(self.defaultPaper(), i)
                self.setFont(self.defaultFont(), i)

    def styleText(self, start, end):
        flag = {
            'tripleSingleQuotedString': False,
            'tripleDoubleQuotedString': False,
            's_unclosedString': False,
            'd_unclosedString': False
        }
        self.startStyling(start)
        splitter = re.compile(
            r"(\"\"\"|'''|'.*?'|\".*?\"|#.*$|@.*$|\.|\w+\(|\n|\s+|\w+|\W)")
        text = self.parent().text()[start:end]
        tokens = [(token, len(bytearray(token,'utf-8')))
                  for token in splitter.findall(text)]
        editor = self.parent()
        num = 0
        # 检查是否是多行样式
        if start != 0:
            previous_style = editor.SendScintilla(
                editor.SCI_GETSTYLEAT, start - 1)
            if previous_style == self.styles['tripleSingleQuotedString']:
                flag['tripleSingleQuotedString'] = True
            elif previous_style == self.styles['tripleDoubleQuotedString']:
                flag['tripleDoubleQuotedString'] = True
        # (单词，长度)
        for i, token in enumerate(tokens):
            if token[0] == "'''":
                # 三单引号
                if flag['tripleSingleQuotedString']:
                    # 关三单引号
                    print('关闭三单引号')
                    self.setStyling(
                        token[1], self.styles['tripleSingleQuotedString'])
                    flag['tripleSingleQuotedString'] = False
                else:
                    # 判断能不能开三单引号
                    if flag['tripleDoubleQuotedString']:
                        # 三单引号作为三双引号的为注释
                        self.setStyling(
                            token[1], self.styles['tripleDoubleQuotedString'])
                    else:
                        # 开三单引号
                        print('打开三单引号')
                        self.setStyling(
                            token[1], self.styles['tripleSingleQuotedString'])
                        flag['tripleSingleQuotedString'] = True
            elif token[0] == '"""':
                # 三双引号
                if flag['tripleDoubleQuotedString']:
                    # 关三双引号
                    self.setStyling(
                        token[1], self.styles['tripleDoubleQuotedString'])
                    flag['tripleDoubleQuotedString'] = False
                else:
                    # 判断能不能开三双引号
                    if flag['tripleSingleQuotedString']:
                        # 三双引号作为三单引号的为注释
                        self.setStyling(
                            token[1], self.styles['tripleSingleQuotedString'])
                    else:
                        # 开三双引号
                        self.setStyling(
                            token[1], self.styles['tripleDoubleQuotedString'])
                        flag['tripleDoubleQuotedString'] = True
            elif flag['tripleSingleQuotedString']:
                self.setStyling(
                    token[1], self.styles['tripleSingleQuotedString'])
            elif flag['tripleDoubleQuotedString']:
                self.setStyling(
                    token[1], self.styles['tripleDoubleQuotedString'])
            elif token[0] == "'":
                # 未关闭的单引号
                if not flag['d_unclosedString']:
                    flag['s_unclosedString'] = True
                self.setStyling(token[1], self.styles['unclosedString'])
            elif token[0] == '"':
                # 未关闭的双引号
                if not flag['s_unclosedString']:
                    flag['d_unclosedString'] = True
                self.setStyling(token[1], self.styles['unclosedString'])
            elif flag['s_unclosedString']:
                self.setStyling(token[1], self.styles['unclosedString'])
            elif flag['d_unclosedString']:
                self.setStyling(token[1], self.styles['unclosedString'])
            elif token[0][0] == '#':
                # comment,注释
                self.setStyling(token[1], self.styles['comment'])
            elif token[0][0] == '@':
                # decorator,装饰器
                self.setStyling(token[1], self.styles['decorator'])
            elif token[0][0] == "'":
                # singleQuotedString,单引号字符串
                self.setStyling(token[1], self.styles['singleQuotedString'])
            elif token[0][0] == '"':
                # doubleQuotedString,双引号字符串
                self.setStyling(token[1], self.styles['doubleQuotedString'])
            elif token[0] == '(':
                self.refreshProperties()
            elif token[0].isdigit():
                # number,数字
                self.setStyling(token[1], self.styles['number'])
            elif token[0] in self.operator:
                # operator,运算符
                self.setStyling(token[1], self.styles['operator'])
            elif token[0] in self.constants:
                # constants,常量
                self.setStyling(token[1], self.styles['constants'])
            elif token[0][-1] == '(':

                # funName,函数
                name = token[0][0:-1].strip()
                if name in self.keyword:
                    # keyword,关键字
                    self.setStyling(token[1] - 1, self.styles['keyword'])
                elif name in self.functions:
                    # functions,内置函数
                    self.setStyling(token[1] - 1, self.styles['functions'])
                elif name in self.otherKeyword:
                    # otherKeyword,其他关键字
                    self.setStyling(token[1] - 1, self.styles['otherKeyword'])
                else:
                    self.setStyling(token[1] - 1, self.styles['funName'])
                self.setStyling(1, self.styles['default'])
            elif token[0] in self.keyword:
                # keyword,关键字
                self.setStyling(token[1], self.styles['keyword'])
            elif token[0] in self.functions:
                # functions,内置函数
                self.setStyling(token[1], self.styles['functions'])
            elif token[0] in self.otherKeyword:
                # otherKeyword,其他关键字
                self.setStyling(token[1], self.styles['otherKeyword'])
            else:
                # default,默认值
                self.setStyling(token[1], self.styles["default"])

    def blockStart(self):
        return (b':', 10)

    def foldCompact(self):
        return True

    def autoCompletionWordSeparators(self):
        return ['.']

    def blockLookback(self):
        return 0

    def braceStyle(self):
        return self.styles['operator']

    def indentationGuideView(self):
        return Qsci.QsciScintillaBase.SC_IV_LOOKFORWARD

    def defaultEolFill(self, style):
        if style > len(self.styles_keys):
            return False
        if self.styles_keys[style] == 'unclosedString':
            return True
        return False
