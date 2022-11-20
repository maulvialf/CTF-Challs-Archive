#!/usr/bin/env python
import re
import os
import sys
import enum

class A(enum.Enum):
    attr = None
class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas + '\n')
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

charBanned = re.escape('"!#$&\'()*+-/:<=>?@\^`{|}~')
wordBanned = [
    'import', 'enum', 'word', 'char', 'eval', 'fork',
    'exec', 'open', 'locals', 'globals', 'banned', 'dir',
    'print', 'compile', 'input', 'exit', 'quit',
    'unicode', 'setattr', 'getattr', 'repr', 'len',
    'file', 'builtins', 'name', 'doc', 'base',
    'class', 'subclasses', 'mro', 'init', 'main'
]

charBanned = '[%s]' % (charBanned)
wordBanned = '|'.join('(%s)' % (_) for _ in wordBanned)

stdout = Unbuffered(sys.stdout)
stdout.write('>>> ')
lines = raw_input()

if re.findall(charBanned, lines):
    raise Exception('Bad character detected!')

if re.findall(wordBanned, lines, re.I):
    raise Exception('Bad word detected!')

try:
    exec(lines)
except:
    pass