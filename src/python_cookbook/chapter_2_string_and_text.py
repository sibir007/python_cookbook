from chapter_0 import *

count_print = 0


def get_plach():
    global count_print
    count_print += 1
    return str_templat.format(count_print)


prn_tem('2.1. Splitting Strings on Any of Multiple Delimiters')

line = 'asdf fjdk; afed, fjek,asdf,foo'
import re

print(line)
print('[;,\\s]\\s*', re.split(r'[;,\s]\s*', line))
fields = re.split(r'(;|,|\s)\s*', line)
print('fields', fields)

values = fields[::2]
delimetres = fields[1::2]
print("values", values)
print('delimetres', delimetres)
comdo = ' '.join(v + d for v, d in zip(values, delimetres))
print(comdo)
print(re.split(r'(?:,|;|\s)\s*', line))

prn_tem('2.2. Matching Text at the Start or End of a String')
import os

filenames = os.listdir('/home/dima')
print(filenames)
fn1 = [fn for fn in filenames if fn.startswith('.')]
print(fn1)
fn2 = [fn for fn in filenames if fn.startswith(('.', 'Y', "D"))]
print(fn2)
print(any(fn for fn in filenames if fn.endswith('.py')))

from urllib.request import urlopen


def read_data(name: str):
    if name.startswith(('http', 'https', 'ftp')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


url = 'https://www.python.org'
# respons = read_data(url)
# print()
# resp1 = re.split(r'[\s\n]\s*', str(respons, 'UTF-8'))
# print(resp1[:20])

prn_tem('2.3. Matching Strings Using Shell Wildcard Patterns')
from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
names1 = [name for name in names if fnmatch(name, 'Dat?.csv')]
print(names)
print("[name for name in names if fnmatch(name, 'Dat?.csv')]", names1)
print("[name for name in names if fnmatch(name, 'Dat?.csv')]", names1)
print("fnmatchcase('foo.txt', '*.txt')", fnmatchcase('foo.txt', '*.txt'))
print("fnmatchcase('foo.txt', '*.TXT')", fnmatchcase('foo.txt', '*.TXT'))

prn_tem("2.4.Matching and Searching for Text Patterns")
text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re


def print_match(regular, text):
    if re.match(regular, text):
        print('yes')
    else:
        print('no')


print_match(r'\d+/\d+/\d+', text1)
print_match(r'\d+/\d+/\d+', text2)

compile_regular = re.compile(r'\d+/\d+/\d+')
print('compile_regular.match(text1)', compile_regular.match(text1).group(0))
# print('compile_regular.match(text2)', compile_regular.match(text2).group(0))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(compile_regular.findall(text))
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.findall(text)
print(m)
for y, m, d in m:
    print('{}-{}-{}'.format(y, m, d))
for m in datepat.finditer(text):
    y, mo, d = m.groups()
    print('{}-{}-{}'.format(y, mo, d))

prn_tem('2.5. Searching and Replacing Text')
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re

print(text)
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{}-{}-{}'.format(m.group(2), mon_name, m.group(3))


print(datepat.sub(change_date, text))

prn_tem('2.6. Searching and Replacing Case-Insensitive Text')

text = 'UPPER PYTHON, lower python, Mixed Python'
print(text)
print(re.findall('python', text, flags=re.IGNORECASE))

m_iter = re.finditer('python', text, flags=re.IGNORECASE)
for math in m_iter:
    print(math.group())
print(re.sub('python', 'shake', text, flags=re.IGNORECASE))


def matchcase(word: str):
    def replase(m):
        text: str = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word


# print(re.sub('python', matchcase('shake'), text, flags=re.IGNORECASE))

prn_tem('2.7. Specifying a Regular Expression for the Shortest Match')
import re

str_pat = re.compile(r'"(.*)"')
txt1 = 'cpmputer says "no. "'
print(str_pat.findall(txt1))

prn_tem('2.13. Aligning Text Strings')
text = 'Hello World'
t2 = text.ljust(20, '-')
print('t2', t2)
t3 = t2.rjust(20, '-')
print('t3', t3)
print(text.center(20, '*'))
print('{:>10s}-{:<10s}'.format('Hello', 'World'))

prn_tem('2.14. Combining and Concatenating Strings')

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(', '.join(parts))
data = ['ACME', 50, 91.1]
print(' '.join(str(w) for w in data))


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago'


print(' '.join(sample()))

prn_tem('2.15. Interpolating Variables in Strings')
s = '{name} has {n} massages'
map = {'name': 'Guido',
       'n': 37}
print(map)
sf = s.format_map(map)
print(sf)
print(s.format(name='DIma', n=40))
print(vars())
s2 = '__name__: {__name__} __package__: {__package__}'
print(s2.format_map(vars()))


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


s3 = ('__name__: {__name__} '
      '__package__: {__package__} '
      'missing: {missimg}')
print(s3.format_map(safesub(vars())))

prn_tem('2.16. Reformatting Text to a Fixed Number of Columns')

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap

print(textwrap.fill(s, 40))
print(textwrap.fill(s, 35, initial_indent='     '))
print(textwrap.fill(s, 35, subsequent_indent='     '))
# import os
# columns_sizw = os.get_terminal_size().columns
# print(textwrap.fill(s, columns_sizw))

prn_tem('2.17. Handling HTML and XML Entities in Text')

s = 'Elements are written as "<tag>text</tag>".'
import html

print(s)
print(html.escape(s))

prn_tem('2.18. Tokenizing Text')
text = 'foo = 23 + 42 * 10'
import re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_path = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
# match = master_path.match(text)
# match_iter = master_path.finditer(text)
# for mat in match_iter:
#     print(mat.lastgroup, mat.group())


import collections as cl

Token = cl.namedtuple('Token', ['type', 'value'])


def get_token(matcher, text):
    for math in matcher.finditer(text):
        yield Token(math.lastgroup, math.group())


for token in get_token(master_path, text):
    print(token)

prn_tem('2.19. Writing a Simple Recursive Descent Parser')
import re
import collections

# Token specification
tokens = [r'(?P<NUM>\d+)',
          r'(?P<PLUS>\+)',
          r'(?P<MINUS>-)',
          r'(?P<TIMES>\*)',
          r'(?P<DIVIDE>/)',
          r'(?P<LPAREN>\()',
          r'(?P<RPAREN>\))',
          r'(?P<WS>\s+)'
          ]

master_path = re.compile('|'.join(tokens))
Token = collections.namedtuple('Token', ['type', 'value'])
# def generate_tokens()
