import sys
import os
import keyword
import re
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import Qsci


class lexer(Qsci.QsciLexerPython, Qsci.QsciLexerCustom):

    # 这个是风格列表，切记不可以改变顺序
    styles = [
        'default',
        'comment',
        'number',
        'doubleQuotedString',
        'singleQuotedString',
        'keyword',
        'tripleSingleQuotedString',
        'tripleDoubleQuotedString',
        'className',
        'functionMethodName',
        'operator',
        'identifier',
        'commentBlock',
        'unclosedString',
        'highlightedIdentifier',
        'decorator',
        'doubleQuotedFString',
        'singleQuotedFString',
        'tripleSingleQuotedFString',
        'tripleDoubleQuotedFString',
    ]

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

    def __init__(self, parent):
        super().__init__(parent)

    def keywords(self, _set):
        if _set == 1:
            return ' '.join(self.keyword)
        elif _set == 2:
            return ' '.join(self.functions)
        else:
            return ''

    def description(self, style):
        if style < 20:
            return self.styles[style]
        else:
            return ''

    def styleText(self, start, end):
        self.startStyling(start)
        self.setStyling()
        splitter = re.compile(r"(\{\.|\.\}|\#|\'|\"\"\"|\n|\s+|\w+|\W)")
        text = self.parent().text()[start:end]
        tokens = [(token, len(bytearray(token, "utf-8")))
                  for token in splitter.findall(text)]
        # (单词，长度)
        # Style the text in a loop
        for i, token in enumerate(tokens):
            if token[0] in self.keywords:
                # Keyword
                self.setStyling(token[0], self.styles["Keyword"])


class lexer_json(Qsci.QsciLexerJSON, Qsci.QsciLexerCustom):

    # 这个是风格列表，切记不可以改变顺序
    styles = [
        'json_default',
        'json_number',
        'json_string',
        'json_unclosedString',
        'json_property',
        'json_escapeSequence',
        'json_commentLine',
        'json_commentBlock',
        'json_operator',
        'json_IRI',
        'json_IRICompact',
        'json_keyword',
        'json_keywordLD',
        'json_error',
    ]

    keyword = ['false', 'true', 'null']
    keywordLD = ['@id', '@context', '@type', '@value', '@language', '@container',
                 '@list', '@set', '@reverse', '@index', '@base', '@vocab', '@graph']

    def __init__(self, parent):
        super().__init__(parent)

    def keywords(self, _set):
        if _set == 1:
            return ' '.join(self.keyword)
        elif _set == 2:
            return ' '.join(self.keywordLD)
        else:
            return ''

    def description(self, style):
        if style < 14:
            return self.styles[style]
        else:
            return ''
