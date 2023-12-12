from chapter_0 import *
count_print = 0
def get_plach():
    global count_print
    count_print += 1
    return str_templat.format(count_print)


# 1.1. Unpacking a Sequence into Separate Variables
p = 4, 5
x, y = p
print(get_plach1(1), x, y)

data = ['ACEM', 50, 91.1, (2012, 12, 21)]
name, shared, price, date = data
print(get_plach1(2), name, shared, price, date)
_, shared, price, _ = data
print(get_plach1(3), shared, price)

s = 'Hello'
a, b, s1, *d = s
print(get_plach1(4), a, b, s1, d)


# 1.2. Unpacking Elements from Iterables of Arbitrary Length
def drop_first_last(grades):
    first, *middle, last = grades
    return middle


record = 'Dave', 'dave@mail.com', '7777777', '6748-38383-9393'
print(get_plach1(5), drop_first_last(record))

*trailing, current = [10, 9, 8, 7, 7, 3, 2, 4, 5, 8]
print(get_plach1(6), 'trailing: ', trailing)
print(get_plach1(7), 'current: ', current)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print(get_plach1(8), 'foo', x, y)


def do_bar(s):
    print(get_plach1(9), 'bsr', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, hs = line.split(':')
print(get_plach1(10), 'uname:', uname)
print(get_plach1(11), 'fields:', fields)
print(get_plach1(12), 'homedir:', homedir)
print(get_plach1(13), 'sh:', hs)

record = 'ACME', 50, 123.45, (12, 18, 2012)
name, *_, (*_, year) = record
print(get_plach1(14), 'record:', record)
print(get_plach1(15), 'name:', name)
print(get_plach1(16), 'year:', year)

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


with open('test_files/some_text.text') as f:
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
print(get_plach1(22), q.pop(), q.pop(), q.pop(), q.pop(), q.pop(), q.pop())

prn_tem('1.6. Mapping Keys to Multiple Values in a Dictionary')

d = {
    'a': [1, 2, 3],
    'b': [4, 5, 6]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5, 6}
}
print(get_plach(), d, e)
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
print(get_plach(), d, e)

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
print(get_plach(), d)
for key in d:
    print(key, ':', d[key], '; ', end='')
import json

print(get_plach(), json.dumps(d))

prn_tem('1.8. Calculating with Dictionaries')
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
zip_prices = zip(prices.values(), prices.keys())
print(get_plach(), zip_prices)
print(get_plach(), min(zip_prices))
zip_prices = zip(prices.values(), prices.keys())
print(get_plach(), max(zip_prices))
zip_prices = zip(prices.values(), prices.keys())
print(get_plach(), sorted(zip_prices))

print(get_plach(), min(prices))
print(max(prices))
print(get_plach(), min(prices.values()))
print(max(prices.values()))
print(get_plach(), min(prices, key=lambda s: prices[s]))
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
print('set(a.items()):', set(a.items()))
print('a.items():', a.items())

print(get_plach(), 'a.keys() & b.keys();', a.keys() & b.keys())
print(get_plach(), 'a.keys() - b.keys():', a.keys() - b.keys())
print(get_plach(), 'a.items() & b.items():', a.items() & b.items())
print(get_plach(), 'a.items() - b.items():', a.items() - b.items())

c = {key: a[key] for key in a.keys() - {'a', 'z'}}
print(get_plach(), c)

prn_tem('1.10. Removing Duplicates from a Sequence while Maintaining Order')


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

print(get_plach(), list(dedupe(a, key=lambda i: ((i['x']), i['y']))))

prn_tem('1.11. Naming a Slice')
###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100      .......513.25         ..........'
print('record.index("100")', record.index('100'))
print('record.index("513")', record.index('513'))
SHARES = slice(20, 32)
PRICE = slice(36, 42)
print(get_plach(), record[SHARES], record[PRICE])

prn_tem('1.12. Determining the Most Frequently Occurring Items in a Sequence')
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(get_plach(), 'top_three', top_three)
print(get_plach(), 'word_counts.items()', word_counts.items())
print(get_plach(), "word_counts['look']", word_counts['look'])
print(get_plach(), "word_counts['my']", word_counts['my'])

for word in word_counts:
    word_counts[word] += 1
print(get_plach(), 'word_counts.items()', word_counts.items())
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts.update(morewords)
print(get_plach(), word_counts)

prn_tem('1.13. Sorting a List of Dictionaries by a Common Key')

rows = [
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print("rows_by_fname", rows_by_uid)
print('rows_by_uid', rows_by_uid)

prn_tem('1.14. Sorting Objects Without Native Comparison Support')
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(id) for id in range(30, 10, -1)]
print(get_plach(), 'users before sorting', users)
users.sort(key=attrgetter('user_id'))
print(get_plach(), 'users past sorting', users)
print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))

prn_tem('1.15. Grouping Records Together Based on a Field')
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for item in items:
        print(item)

from collections import defaultdict

rows_by_date = defaultdict(list)
for d in rows:
    rows_by_date[d['date']].append(d)
print('rows_by_date', rows_by_date)
print(get_plach(), 'rows groups by date:')
for date in rows_by_date:
    print(date, rows_by_date[date])

prn_tem('1.16. Filtering Sequence Elements')
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
fmylist = [n for n in mylist if n > 0]
print('flist >0:', fmylist)
fmylist = [n for n in mylist if n < 0]
print('flist <0:', fmylist)

# generator
pos = (n for n in mylist if n > 0)
for n in pos:
    print(n)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(n):
    try:
        val = int(n)
        return True
    except ValueError:
        return False


f_gen = (n for n in values)

filtred_values = [n for n in filter(is_int, f_gen)]
print('not filtered value:', values)
print('filtered value:', filtred_values)
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math

my_sqrt_list1 = [math.sqrt(n) for n in mylist if n > 0]
my_sqrt_list2 = [math.sqrt(n) if n > 0 else 0 for n in mylist]
print('not filtered mylist:', mylist)
print('filtered 1 mylist:', my_sqrt_list1)
print('filtered 2 mylist:', my_sqrt_list2)

prn_tem('1.17. Extracting a Subset of a Dictionary')
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 200}
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
gen1 = ((key, value) for key, value in prices.items() if key in prices.keys() & tech_names)
p3 = dict(gen1)
print(get_plach())
print(prices)
print(p1)
print(tech_names)
print(p2)
print(p3)

prn_tem('1.18. Mapping Names to Sequence Elements')
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('sibiriakoff2006#yandex.ru', '2010-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))
adr, joined = sub
print((adr, joined))
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
Stock = namedtuple('Stack', ['name', 'shares', 'price'])


def convert_stock(record):
    return Stock(**record)


print(convert_stock(a))

Stock2 = namedtuple('Stock2', ['name', 'shares', 'price', 'date', 'tame'])
stock_template = Stock2(name=None, shares=None, price=None, date=None, tame=None)
print(stock_template)


def use_tempate(rec):
    return stock_template._replace(**rec)


b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(use_tempate(a))
print(use_tempate(b))

prn_tem('1.19. Transforming and Reducing Data at the Same Time')
nums = [1, 2, 3, 4, 5]
print(sum(x * x for x in nums))

s = ('ACME', 50, 125, 45)
print(','.join(str(x) for x in s))

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
print(min(s.__getitem__('shares') for s in portfolio))
print(min(portfolio, key=itemgetter('shares')))
print(min(portfolio, key=lambda i: i['shares']))

prn_tem('1.20. Combining Multiple Mappings into a Single Mapping')
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b)
print(c.items())
print(c.keys())
print(c.values())
print(c['x'])
print(c['y'])
print(c['z'])
print(c['x'])
print(len(c))
print(list(c.keys()))
print(list(c.values()))
del c['z']
print(c)
merged = dict(a)
merged.update(b)
print(merged)

