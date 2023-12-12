from typing import Iterator, Any, Iterable

from src.python_cookbook.chapter_0 import prn_tem

prn_tem('4.1. Manually Consuming an Iterator')

with open('chapter_2_string_and_text.py') as f:
    counter = 0
    try:
        while counter <= 20:
            line = next(f)
            print(line, end='')
            counter += 1
    except StopIteration:
        pass

prn_tem('4.2. Delegating Iteration')


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


my_node = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
my_node.add_child(n2)
my_node.add_child(n3)
my_node.add_child(n4)
my_node.add_child(n6)
for nod in my_node:
    print(nod)

prn_tem('4.3. Creating New Iteration Patterns with Generators')


def frange(start, stop, inc: int):
    while start < stop:
        yield start
        start += inc


for x in frange(23, 45, 3):
    print(x)

print(list(frange(0.3, 1.7, .2)))


def countdown(n: int):
    while n:
        yield n
        n = n - 1
    print('done')


gen = countdown(10)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break

prn_tem('4.4. Implementing the Iterator Protocol')


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def add_child(self, node):
        self._children.append(node)

    def __repr__(self):
        return 'Nede({!r})'.format(self._value)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for nod in self:
            yield from nod.depth_first()


root = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
root.add_child(n1)
root.add_child(n2)
root.add_child(n3)
root.add_child(n4)
root.add_child(n5)
root.add_child(n6)
root.add_child(n7)
gen = root.depth_first()
while True:
    try:
        print(next(gen))
    except StopIteration:
        break


class Node:
    def __init__(self, value):
        self._value: int = value
        self._children: [Node] = []

    def add_child(self, node: Node):
        self._children.append(node)

    def __repr__(self):
        return 'Nede({!r})'.format(self._value)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DeepFirstIterator(self)


class DeepFirstIterator():
    def __init__(self, node: Node):
        self._start_node: Node = node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter is None:
            self._children_iter = iter(self._start_node)
            return self._start_node
        elif self._child_iter:
            try:
                curent_node = next(self._child_iter)
                return curent_node
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


prn_tem('4.5. Iterating in Reverse')
a = [1, 2, 3, 4, 5]
for x in reversed(a):
    print(x, end=', ')
print()


class Countdown:

    def __init__(self, n: int) -> None:
        self._n = n

    # forward iterator
    def __iter__(self) -> Iterator[int]:
        n = self._n
        while n > 0:
            yield n
            n -= 1

    # reverse iterator
    def __reversed__(self) -> Iterator[int]:
        n = self._n
        x = 0
        while x <= n:
            yield x
            x += 1


fi = Countdown(11)
ri = Countdown(9)
for num in fi:
    print(num, end=', ')
print()
for num in reversed(ri):
    print(num, end=', ')
print()

prn_tem('4.6. Defining Generator Functions with Extra State')

from collections import deque


class linehistory:
    def __init__(self, lines: Iterator[str], histlen=3) -> None:
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self) -> Iterator[str]:
        for linenum, line in enumerate(self.lines, 1):
            self.history.append((linenum, line))
            yield line

    def clear(self) -> None:
        self.history.clear()


with open('chapter_2_string_and_text.py') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, line in lines.history:
                print(f'{lineno}:{line}')

prn_tem('4.7. Taking a Slice of an Iterator')


def count(n):
    while True:
        yield n
        n += 1


import itertools

for x in itertools.islice(count(2), 10, 20):
    print(x, end=' ')

prn_tem('4.8. Skipping the First Part of an Iterable')
from itertools import dropwhile

with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: 'root' not in line, f):
        print(line, end='')

from itertools import islice

item = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(item, 3, None):
    print(x, end=', ')

prn_tem('4.9. Iterating Over All Possible Combinations or Permutations')

item = ['a', 'b', 'c', 1, 4, 10, 15]
from itertools import permutations

for p in permutations(item):
    print(p)
for p in permutations(item, 2):
    print(p)

from itertools import combinations

for p in combinations(item, 2):
    print(p)

prn_tem('4.10. Iterating Over the Index-Value Pairs of a Sequence')
item = ['a', 'b', 'c', 1, 4, 10, 15]
for ind, val in enumerate(item, 1):
    print(ind, val)

data = [(1, 2), (3, 4), (5, 6), (7, 8)]
for n, (x, y) in enumerate(data):
    print(n, x, y)

prn_tem('4.11. Iterating Over Multiple Sequences Simultaneously')

xpts = [1, 2, 3, 4, 5, 6, 7]
ypts = [100, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for x, y in zip(a, b):
    print(x, y)
from itertools import zip_longest

for i in zip_longest(a, b):
    print(i)
for i in zip_longest(a, b, fillvalue=0):
    print(i)

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

s = dict(zip(headers, values))
print(s)

a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)

print(list(zip(a, b)))

prn_tem('4.12. Iterating on Items in Separate Containers')
from itertools import chain

a = [1, 2, 3, 4, ]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x, end=', ')

prn_tem('4.13. Creating Data Processing Pipelines')
import os, fnmatch, gzip, bz2, re


def gen_find(filepat: str, top: str) -> Iterator[str]:
    """
    find all filenames in a directory tree that match a shell wildcard pattern
    :param filepat: file name
    :param top: directory for search
    :return: iterator filepath
    """
    for path, dirlist, filelist in os.walk(top):
        for name in (fnmatch.filter(filelist, filepat)):
            if ('boot' not in name) \
                    and ('ubuntu' not in name) \
                    and ('casper' not in name):
                    # and ('eipp' not in name):
                # if 'ubuntu' not in name:
                #     if 'casper' not in name:
                #         if 'eipp' not in    name:
                yield os.path.join(path, name)


# for e in gen_find('*.log*', '/var/log'):
#     print(e)

def gen_open_file(filenames: Iterator[str]) -> Iterator[Iterator[str]]:
    """
    принимает Iteranor[str] итаратор с именами файлов,
    возвращает открытый файл в виде итератора
    :param filenames: имя файла
    :return: итератор сторок в файле / открытый файл
    """
    for name in filenames:
        # print(name)
        if name.endswith('gz'):
            f = gzip.open(name, 'rt', errors='replace')
        elif name.endswith('bz2'):
            f = bz2.open(name, 'rt', errors='replace')
        else:
            f = open(name, 'rt', errors='replace')
        yield f
        f.close()


def gen_concatenate(iterators: Iterator[Iterator[Any]]) -> Iterator[Any]:
    """
    Chain a sequence of irerators
    :param iterators:
    :return: Any
    """

    for ite in iterators:
        yield from ite


def gen_greep(pattern: str, lines: Iterator[str]) -> Iterator[str]:
    """
    Look for a regex pattern in seaquence of lines
    :param pattern: regex pattern
    :param lines: strings
    :return: mathc string
    """
    pat = re.compile(pattern)
    for line in lines:
        try:
            if pat.search(line):
                yield line
        except UnicodeDecodeError:
            print('err')


log_dir_name: str = '/var/log'
name_match: str = '*.log*'

math_files: Iterator[str] = gen_find(name_match, log_dir_name)
# for line in math_files:
#     print(line)

open_files: Iterator[Iterator[str]] = gen_open_file(math_files)
# for file in open_files:
#     print(file)

concat_gen: Iterator[str] = gen_concatenate(open_files)
# for file in concat_gen:
#     try:
#         print(file)
#     except UnicodeDecodeError:
#         print('error')

math_line: Iterator[str] = gen_greep(r'info', concat_gen)
for line in math_line:
    try:
        print(line)
    except UnicodeDecodeError:
        print('error')

prn_tem('4.14. Flattening a Nested Sequence')
from typing import Iterable


def flatten(items: Iterable) -> Iterable:
    for item in items:
        if isinstance(item, (str, bytes)) or not isinstance(item, Iterable):
            yield item
        else:
            yield from flatten(item)


items = [1, 2, [3, 4, [5, 6], 7], 8]
for item in flatten(items):
    print(item, end=' ')
print()
items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for item in flatten(items):
    print(item)

prn_tem('4.15. Iterating in Sorted Order Over Merged Sorted Iterables')
import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for x in heapq.merge(a, b):
    print(x)

prn_tem('4.16. Replacing Infinite while Loops with an Iterator')
import  sys
f = open('/etc/passwd')
for s in iter(lambda : f.read(10), ''):
    n = sys.stdout.write(s)
f.close()