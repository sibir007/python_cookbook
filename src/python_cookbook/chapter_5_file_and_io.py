from __future__ import annotations

import io
import mmap
from os import PathLike

from src.python_cookbook.chapter_0 import prn_tem

prn_tem('5.1. Reading and Writing Text Data')
with open('test1.py', 'rt') as f:
    data = f.read()
    print(data)

with open('test1.py', 'rt') as f:
    line = f.readline()
    print(line)

with open('test1.py', 'wt') as f:
    f.write('slkdfjslkdfjslkdfjlskdjfslkdfj')
    f.write('slkdfjslkdfjslkdfjlskdjfslkdfj')
    f.write('slkdfjslkdfjslkdfjlskdjfslkdfj')
    f.write('slkdfjslkdfjslkdfjlskdjfslkdfj')
    f.write('slkdfjslkdfjslkdfjlskdjfslkdfj')

# with open('test1.py', 'at') as f:
#     print('sdkljflskdfj\n', file=f)
#     print('sdkljflskdfj\n', file=f)
#     print('sdkljflskdfj\n', file=f)
#     print('sdkljflskdfj\n', file=f)

with open('test1.py', 'rt', newline='') as f:
    print(f.read())

prn_tem('5.2. Printing to a File')
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')
print('ACME', 50, 91.5)

row = ('ACME', 50, 91.5)

print(','.join(str(i) for i in row), end='~~', sep=', ')
print(*row, sep=', ')

prn_tem('5.4. Reading and Writing Binary Data')
print(hex(4234))
data
with open('test1.py', 'rb') as f:
    data = f.read()
print(data)

with open('test1.py', 'wb') as f:
    f.write(b'hello World')
for b in b'sjdlfkjsldkfjlsk':
    print(b)

import array

nums = array.array('i', [1, 2, 3, 4, 5, ])
with open('test_files/test_data.bin', 'wb') as f:
    f.write(nums)

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ])
with open('test_files/test_data.bin', 'rb') as f:
    print(f.read(10))
    # a = [(a.append(b) for b in f.read())]

print(a)

prn_tem('5.6. Performing I/O Operations on a String')
s = io.StringIO()
print(s.write('sdkfjslkfjslkfjlskfjlskfjslkdfjlskfj\n'))
print('this is a test', file=s)
print(s)
f = open('test_files/some_text.text', 'tw')

print('this is test print', file=f)
f.close()
with open('test_files/some_text.text', 'rt') as f:
    data = f.read()
    print(data)
print(s.getvalue())
s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())

b = io.BytesIO(b'this is byte string')
print(b.getvalue())

prn_tem('5.7. Reading and Writing Compressed Datafiles')
import gzip

with gzip.open('/var/log/apport.log.2.gz', 'rt') as f:
    # data = f.read()
    # print(data)
    for line in f.readlines():
        print(line, end='')

with gzip.open('test_files/some_gzip_file.gzip', 'wt') as f:
    f.write('sljflsdkfjlsdfjksjfs\n')
    f.write('sljflsdkfjlsdfjksjfs\n')
    f.write('sljflsdkfjlsdfjksjfs\n')
    f.write('sljflsdkfjlsdfjksjfs\n')
    f.write('sljflsdkfjlsdfjksjfs\n')
with gzip.open('test_files/some_gzip_file.gzip', 'rt') as f:
    for line in f.readlines():
        print(line, end='')

prn_tem('5.8. Iterating Over Fixed-Sized Records')
from functools import partial

RECORD_SIZE = 5
with open('test_files/some_text.text', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)

prn_tem('5.9. Reading Binary Data into a Mutable Buffer')
import os.path


def read_into_buffer(filename: str) -> bytearray:
    buf = bytearray()
    with open(filename, 'rb') as f:
        data = f.read()
        # print(data)
        for b in data:
            buf.append(b)
    return buf


with open('test_files/test_file3', 'bw') as f:
    f.write(b'Hello World')

buf: bytearray = read_into_buffer('test_files/test_file2.bin')
print(buf)
# print(buf[0:5])

prn_tem('5.10. Memory Mapping Binary Files')


def memory_map(filename: str, access=mmap.ACCESS_WRITE) -> mmap.mmap:
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


size: int = 100000
with open('test_files/test_file3', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

mm = memory_map('test_files/test_file3')
print(len(mm))
print(mm[0:10])
bs = b'Hello World'
print(len(bs))
mm[0:11] = bs
print(mm[0:11])
mm.close()
with memory_map('test_files/test_file3') as mm:
    print(len(mm))
    print(mm[0:11])

prn_tem('5.11. Manipulating Pathnames')
import os

path = '/home/dima/Downloads/wallpaperflare.com_wallpaper.jpg'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.abspath('chapter_0.py'))
print(os.path.join('tmp', 'data', os.path.basename(path)))
print(os.path.expanduser('~/python/projects/test1/src/example_package/__init__.py'))
print(os.path.split(path))

prn_tem('5.12. Testing for the Existence of a File')
import os

print(os.path.exists('slkdjfsklf'))
print(os.path.exists('chapter_0.py'))
print(os.path.isdir('test_files'))
print(os.path.isfile('./test_files/test_file3'))
print(os.path.getsize('chapter_4_lterators_and_generators.py'))
print(os.path.getatime('test1.py'))
import time

print(time.ctime(os.path.getatime('test1.py')))

prn_tem('5.13. Getting a Directory Listing')

import os

names = os.listdir(os.path.expanduser('~/'))
print(names)
files = [file for file in os.listdir('.') if os.path.isfile(file)]
for file in files: print(file)
from fnmatch import fnmatch

pylist = [file for file in os.listdir('.') if fnmatch(file, '*.py')]
for e in pylist:
    print(e)

import os
import os.path
import glob
import time

pyfiles = glob.glob('*.py', recursive=True)
name_sz_date = [(name, os.path.getsize(name), os.path.getatime(name))
                for name in pyfiles]
for name, sz, date in name_sz_date:
    print(f'name: {name}, sz: {sz}, date: {time.ctime(date)}')

print(os.listdir(b'test_files'))

with open(
        b'test_files/\xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb_\xd0\xbd\xd0\xb0_\xd0\xba\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb5',
        'tw') as f:
    f.write('запись в файл на кирилице')

prn_tem('5.16. Adding or Changing the Encoding of an Already Open File')
import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
# print(text)
print(f)
print(f.buffer)
# print(f.buffer.mode)
f = open('test1.py', 'tw')
print(f)
print(f.mode)
# print(f.buffer)
# print()
f.close()
prn_tem('5.17. Writing Bytes to a Text File')

import sys

sys.stdout.write('Hello')
sys.stdout.buffer.write(b'Hello')
f = open('test_files/some_text.text', 'rt')
data = f.buffer.read()
print(repr(data))
f.close()
prn_tem('5.18. Wrapping an Existing File Descriptor As a File Object')

import os

fd = os.open('test_files/some_text.text', os.O_WRONLY | os.O_CREAT)
f = open(fd, 'wt')
print(f.write("hello wordl\n"))
f.close()
import sys

b_stdeout = open(sys.stdout.fileno(), 'wb', closefd=False)
b_stdeout.write(b'hello world')
b_stdeout.flush()

prn_tem('5.19. Making Temporary Files and Directories')

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    f.write('Hello World')
    f.write('Testing\n')
    f.seek(0)
    data = f.read()
    print(data)

from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print(f.name)

from tempfile import TemporaryDirectory

with TemporaryDirectory() as tempdir:
    print(tempdir)

import tempfile

# tf = tempfile.mkstemp()
# print(tf)
td = tempfile.mkdtemp()
print(td)
print(tempfile.gettempdir())

prn_tem('5.20. Communicating with Serial Ports')

import serial

# ser = serial.SerialI

prn_tem('5.21. Serializing Python Objects')

import pickle

list_data = [x for x in range(10)]
gen_data = (x for x in range(10))

with open('test_files/pickle_file', 'wb') as f:
    pickle.dump(list_data, f)

s = pickle.dumps(list_data)
print(s)
print(len(s))

with open('test_files/pickle_file', 'rb') as f:
    data = pickle.load(f)
    print(data)

import pickle

f = open('test_files/pickle_file', 'wb')
pickle.dump([1, 2, 3, 4, 5, ], f)
pickle.dump('hello world', f)
pickle.dump({'aple', 'pea', 'banana'}, f)
f.close()
f = open('test_files/pickle_file', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
# print(pickle.load(f))
f.close()
print(len(pickle.dumps(list)))

import threading


class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, state):
        self.__init__(state)


# c = Countdown(10)
