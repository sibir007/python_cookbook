str_plasholder = '-'
str_plasholder_count = 5
plasholder = str_plasholder * str_plasholder_count
str_templat = plasholder + '{}' + plasholder + '\n'
count_print: int = 20


def get_plach(num):
    return str_templat.format(num)


def get_plach1():
    global count_print
    count_print += 1
    return str_templat.format(count_print)


def prn_tem(tem):
    print('\n\n--------------', tem, '--------------\n\n')


# 1.1. Unpacking a Sequence into Separate Variables
p = 4, 5
x, y = p
print(get_plach(1), x, y)

data = ['ACEM', 50, 91.1, (2012, 12, 21)]
name, shared, price, date = data
print(get_plach(2), name, shared, price, date)
_, shared, price, _ = data
print(get_plach(3), shared, price)

s = 'Hello'
a, b, s1, *d = s
print(get_plach(4), a, b, s1, d)


# 1.2. Unpacking Elements from Iterables of Arbitrary Length
def drop_first_last(grades):
    first, *middle, last = grades
    return middle


record = 'Dave', 'dave@mail.com', '7777777', '6748-38383-9393'
print(get_plach(5), drop_first_last(record))

*trailing, current = [10, 9, 8, 7, 7, 3, 2, 4, 5, 8]
print(get_plach(6), 'trailing: ', trailing)
print(get_plach(7), 'current: ', current)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print(get_plach(8), 'foo', x, y)


def do_bar(s):
    print(get_plach(9), 'bsr', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, hs = line.split(':')
print(get_plach(10), 'uname:', uname)
print(get_plach(11), 'fields:', fields)
print(get_plach(12), 'homedir:', homedir)
print(get_plach(13), 'sh:', hs)

record = 'ACME', 50, 123.45, (12, 18, 2012)
name, *_, (*_, year) = record
print(get_plach(14), 'record:', record)
print(get_plach(15), 'name:', name)
print(get_plach(16), 'year:', year)

items = [1, 10, 7, 4, 5, 9]


def my_sum(items):
    head, *tail = items
    return head + my_sum(tail) if tail else head


print('items:', items)
print('sum:', my_sum(items))

print('\n\n1.3. Keeping the Last N Items\n\n')
from collections import deque
from io import StringIO


def search(lines, pattern, history=5):
    prevlines = deque(maxlen=history)
    for line in lines:
        if pattern in line or pattern.capitalize() in line:
            yield line, prevlines
        prevlines.append(line)


with open('some_text.text') as f:
    for line, prevlines in search(f, 'python', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-' * 20)

prn_tem('1.4. Finding the Largest or Smallest N Items')
import heapq

nums = [1, 8, 2, 23, 7, 18, 23, 42, 37, 2]
print(heapq.nsmallest(3, nums))
print(heapq.nlargest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print('cheap:', cheap)
print('expensive:', expensive)

nums = [1, 8, 2, 23, -4, 7, 18, 23, 42, 37, 2]
heap = list(nums)
print('heap', heap)
heapq.heapify(heap)
print('heap', heap)
print('heappop:', heapq.heappop(heap))
print('heappop:', heapq.heappop(heap))
print('heappop:', heapq.heappop(heap))
print('heappop:', heapq.heappop(heap))
print('heappop:', heapq.heappop(heap))
print('heappop:', heapq.heappop(heap))
heap = []
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 19)
heapq.heappush(heap, -4)
heapq.heappush(heap, -10)
heapq.heappush(heap, 1)
heapq.heappush(heap, -2)
heapq.heappush(heap, -3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 4)
print(str_templat.format(10), 'heap', heap)

prn_tem('1.5. Implementing a Priority Queue')

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('stam'), 4)
q.push(Item('fjjfjf'), 1)
q.push(Item('jdjdj'), 7)
q.push(Item('fgro'), 3)
print(get_plach(22), q.pop(), q.pop(), q.pop(), q.pop(), q.pop(), q.pop())

prn_tem('1.6. Mapping Keys to Multiple Values in a Dictionary')

d = {
    'a': [1, 2, 3],
    'b': [4, 5, 6]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5, 6}
}
print(get_plach1(), d, e)
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(4)
d['b'].append(6)
d['c'].append(0)
e = defaultdict(set)
e['a'].add(2)
e['a'].add(3)
e['a'].add(5)
e['c'].add(2)
e['t'].add(6)
e['ad'].add(2)
e['af'].add(2)
print(get_plach1(), d, e)

prn_tem('1.7. Keeping Dictionaries in Order')

from collections import OrderedDict

d = OrderedDict()
d['fo'] = 0
d['f'] = 2
d['uo'] = 79
d['dfjk'] = 4
d['fdf'] = 5
d['sld'] = 3
d['mvd'] = 8
d['orti'] = 41
d[']['] = 10
print(get_plach1(), d)
for key in d:
    print(key, ':', d[key], '; ', end='')
import json

print(get_plach1(), json.dumps(d))

prn_tem('1.8. Calculating with Dictionaries')
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
zip_prices = zip(prices.values(), prices.keys())
print(get_plach1(), zip_prices)
print(get_plach1(), min(zip_prices))
zip_prices = zip(prices.values(), prices.keys())
print(get_plach1(), max(zip_prices))
zip_prices = zip(prices.values(), prices.keys())
print(get_plach1(), sorted(zip_prices))

print(get_plach1(), min(prices))
print(max(prices))
print(get_plach1(), min(prices.values()))
print(max(prices.values()))
print(get_plach1(), min(prices, key=lambda s: prices[s]))
print(max(prices, key=lambda s: prices[s]))

prn_tem('1.9. Finding Commonalities in Two Dictionaries')
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}
print('a:', a)
print('b:', b)
print('set(a.items()):',set(a.items()))
print('a.items():',a.items())

print(get_plach1(), 'a.keys() & b.keys();', a.keys() & b.keys())
print(get_plach1(), 'a.keys() - b.keys():', a.keys() - b.keys())
print(get_plach1(), 'a.items() & b.items():', a.items() & b.items())
print(get_plach1(), 'a.items() - b.items():', a.items() - b.items())

c = {key:a[key] for key in a.keys() - {'a','z'}}
print(get_plach1(), c)

prn_tem('1.10. Removing Duplicates from a Sequence while Maintaining Order')
