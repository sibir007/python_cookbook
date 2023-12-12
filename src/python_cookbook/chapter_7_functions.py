from typing import Tuple, Any, Iterable

from chapter_0 import prn_tem

prn_tem('CHAPTER 7 Functions')


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


nem = avg(1, 2, 3, 45, 5, 6, 76, 78, 8, )
print(nem)
import html


def make_element(name, value, **attrs):
    keyvals = ['{key}={value}'.format(key=k, value=v) for k, v in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attr}>{value}</{name}>'.format(
        name=name,
        attr=attr_str,
        value=html.escape(value))
    return element


el = make_element('item', 'Albatross', size='larg', quantity=6)
print(el)

prn_tem('7.2. Writing Functions That Only Accept Keyword Arguments')


def recv(maxsize, *, block):
    pass


recv(124, block=None)


def minimum(*value, clip=None):
    m = min(value)
    if clip is not None:
        m = clip if clip > m else m
    return m


print(minimum(1, 2, 4, 56, 7))
print(minimum(1, 2, 4, 56, 7, clip=0))

prn_tem('7.8. Making an N-Argument Callable Work As a Callable with Fewer Arguments')


def spam(a, b, c, d):
    print(a, b, c, d)


from functools import partial

part_spam = partial(spam, 1, 2, d=42)
part_spam(3)
part_spam(333)
part_spam(32)

point = [(1, 2), (3, 4), (5, 6), (7, 8)]
import math


def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


pt1 = (12, 3)
point.sort(key=partial(distance, pt1))
# ''.join(point)
# print(', '.join(point))
print(point)
import logging


def output_result(result: Any, log: logging.Logger = None):
    if log is not None:
        log.debug(f'Got: {result}')


def func_for_async_call(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')
    p = Pool()
    p.apply_async(func_for_async_call, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()

    from socketserver import StreamRequestHandler, TCPServer

prn_tem('7.9. Replacing Single Method Classes with Functions')
from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template: str) -> None:
        self.template = template

    def open(self, **kwargs) -> Iterable[bytes]:
        return urlopen(self.template.format_map(kwargs))


# yahoo = UrlTemplate('https://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
#     print(line.decode('UTF-8'))


def url_template(url_template: str):
    def open_templat(**kwargs):
        urlopen(url_template.format_map(kwargs))

    return open_templat


import typing

prn_tem('7.10. Carrying Extra State with Callback Functions')


def apply_async(func: typing.Callable, args: Tuple, *, callback: typing.Callable):
    result = func(*args)
    callback(result)


def print_rez(rezule):
    print(rezule)


def add(a, b):
    return a + b


apply_async(add, (100, 120), callback=print_rez)
apply_async(add, ("hell", 'world'), callback=print_rez)
from random import random


class ResultHandler:
    def __init__(self) -> None:
        self.counter = 0

    def hanlde(self, result: Any) -> None:
        self.counter += 1
        print('[{}] Got: {}'.format(self.counter, result))
        return


call_back = ResultHandler()

for n in range(15):
    apply_async(add,
                (int(random() * 1000), int(random() * 1000)),
                callback=call_back.hanlde
                )


def make_handle() -> typing.Callable:
    siquens = 0

    def handle(res: Any):
        nonlocal siquens
        siquens += 1
        print(f'[{siquens}] Got: {res}')

    return handle


handler = make_handle()
for n in range(15):
    apply_async(add,
                (int(random() * 1000), int(random() * 1000)),
                callback=handler
                )


def corutine(fun: typing.Callable) -> typing.Callable:
    gen = fun()
    next(gen)
    return gen


@corutine
def make_handler() -> typing.Callable:
    counter = 0
    while True:
        counter += 1
        res = yield
        print(f'Gen [{counter}] Got: {res}')


for n in range(15):
    apply_async(add, (int(random() * 1000), int(random() * 1000)), callback=make_handler.send)

prn_tem('7.11. Inlining Callback Functions')


def apply_async(func: typing.Callable, args: typing.Tuple, *, callback: typing.Callable):
    print("------------im aply afjsldfkjsldfj")
    res = func(*args)
    callback(res)
    return


from queue import Queue
from functools import wraps


class Async:
    def __init__(self, fun: typing.Callable, args: typing.Tuple) -> None:
        self.fun = fun
        self.args = args
        return

    def __iter__(self):
        return self

    def __next__(self):
        if self.args is None:
            raise StopIteration
        fun = self.fun
        self.fun = None
        args = self.args
        self.args = None
        return fun, args


def inlined_async(fun: typing.Callable[[typing.Tuple], typing.Generator]) -> typing.Callable:
    def wrapper(*args) -> None:
        gen = fun(*args)
        # next(gen)
        # gen = fun.
        result_queue = Queue()
        result_queue.put(None)
        while True:
            try:
                # val = gen.send(result_queue.get())
                a: Async = gen.send(result_queue.get())
                print(a.args)
                apply_async(a.fun, a.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper


def add(a, b):
    return a + b


@inlined_async
def test(*args) -> typing.Generator:
    res = yield Async(add, (3, 3))
    print(res)
    res = yield Async(add, ('Hello', 'world'))
    print(res)
    for n in range(20):
        res = yield Async(add, (n, n))
        print(res)
    print("Goodbye")

test()
import multiprocessing
pool = multiprocessing.Pool()
apply_async = pool.apply_async
test()

prn_tem('7.12. Accessing Variables Defined Inside a Closure')
def sampel():
    n = 0
    def func():
        print(n)

    def get_n():
        return n

    def set_n(new_n: int) -> int:
        nonlocal n
        n = new_n

    func.get_n = get_n
    func.set_n = set_n
    return func

func = sampel()
func()
func.get_n()
func.set_n(100)
func()

import  sys
class ClosureInstance:
    def __init__(self):
        locals = sys._getframe(1).f_locals
        self.__dict__.update((k, v) for k, v in locals._items() if callable(v))

    def __len__(self):
        return self.__dict__['__len__']()

def Stack():
    items = []
    def pop():
        return items.pop()

    def push(item):
        items.append(item)

    def __len__():
        return len(items)

    return ClosureInstance()
s = Stack()
s.push('Yi')
s.push(3)
s.push((3, 2))
s.push('10')
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

from timeit import timeit
s1 = Stack()
s2 = Stack2()


timeit_str1 = timeit(stmt= 's1.push(1);len(s1);s1.pop()', setup='from __main__ import s1', number=1000000)
timeit_str2 = timeit(stmt= 's2.push(1);len(s2);s2.pop()', setup='from __main__ import s2', number=1000000)
timeit_str12 = timeit(stmt= 'from __main__ import s1; s1.push(1);len(s1);s1.pop()', number=100000)
timeit_str22 = timeit(stmt= 'from __main__ import s2;s2.push(1);len(s2);s2.pop()', number=100000)
print('timeit_str1',timeit_str1)
print('timeit_str2',timeit_str2)
print('timeit_str12',timeit_str12)
print('timeit_str22',timeit_str22)
