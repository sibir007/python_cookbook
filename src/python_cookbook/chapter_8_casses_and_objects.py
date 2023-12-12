from typing import Union, List

from chapter_0 import prn_tem
import typing

prn_tem('8.1. Changing the String Representation of Instances')


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Pair ({self.x!r}, {self.y!r})'

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)
print(repr(p))
print(p)
p = Pair(7, 8)
print('p is {0!r}'.format(p))
print('p is {0!s}'.format(p))

with open('test_files/xml_doc_whit_namespace.xml') as f:
    print(repr(f))

prn_tem('8.2. Customizing String Formatting')


class Date:
    _formats: typing.Dict[str, str] = {
        'ymd': '{d.year}-{d.month}-{d.day}',
        'mdy': '{d.month}/{d.day}/{d.year}',
        'dmy': '{d.day}/{d.month}/{d.year}'
    }

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        return Date._formats[format_spec].format(d=self)


inst1 = Date(1994, 12, 1)

print(format(inst1))
print(format(inst1, 'dmy'))
print('The data is {:mdy}'.format(inst1))
print('The data is {:ymd}'.format(inst1))
from datetime import date

d = date(2012, 12, 21)
print(d)
print(repr(d))
print('{:%A %B %d %y}'.format(d))
print('{}'.format(d))

prn_tem('8.3. Making Objects Support the Context-Management Protocol')

from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address: typing.Tuple[str, int], family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self) -> socket:
        if self.sock is not None:
            raise RuntimeError('Alredy connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


from functools import partial

conn = LazyConnection(('www.python.org', 80))
with conn as c:
    c.send(b'GET /index.html HTTP/1.1\r\n')
    c.send(b'Host:https://lp.jetbrains.com\n')
    c.send(b'\r\n')
    resp = c.recv(8192)
    # resp = b''.join(iter(partial(c.recv, 8192), b''))
    print(resp.decode('utf-8'))

prn_tem('8.4. Saving Memory When Creating a Large Number of Instances')


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


prn_tem('8.5. Encapsulating Names in a Class')


class B:
    def __init__(self, n):
        self.__private = n

    def __private_method(self):
        ...

    def public_method(self):
        self.__private_method()
        ...


class C(B):
    def __init__(self, m):
        super().__init__(m + 1)
        self.__private = m


obj = C(5)

prn_tem('8.6. Creating Managed Attributes')


class Person:
    def __init__(self, first_name):
        self.first_mame = first_name

    @property
    def first_mame(self):
        return self._first_name

    @first_mame.setter
    def first_mame(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError('Expected string')
        self._first_name = first_name

    @first_mame.deleter
    def first_mame(self):
        raise AttributeError('Can`t delete attribute')


a = Person('dima')
print(a.first_mame)
a.first_mame = 'sdkfjlsjf'
print(a.first_mame)
# del a.first_mame
print(a._first_name)


class Person2:
    def __init__(self, name):
        self.set_name(name)

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Expected a string")
        self._name = name

    def get_name(self):
        return self._name

    def del_name(self):
        raise AttributeError('Can`t delete attribute')

    name = property(get_name, set_name, del_name)


import math


class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimetr(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print(c.area)
print(c.perimetr)

prn_tem('8.7. Calling a Method on a Parent Class')


class A:
    def spam(self, spam: str):
        print('class A :', spam)


class B(A):
    def spam(self, spam: str):
        print('class B :', spam)
        super().spam("im b")


b = B()
b.spam('sldkfjs')


class C:
    def __init__(self):
        self.x = 0


class D(C):
    def __init__(self):
        self.y = 1
        super().__init__()


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name: str, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)


class A:
    pass


class B(A):
    pass


class C:
    pass


class D(B, C):
    pass


obj = D()
print(D.__mro__)

prn_tem('8.8. Extending a Property in a Subclass')


class Person:
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Expected a string')
        self._name = name

    @name.deleter
    def name(self):
        raise AttributeError('Can`t delete attribule')


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, name: str):
        print(f'Setting name {name}')
        print('super()', super(SubPerson, SubPerson).name)
        super(SubPerson, SubPerson).name.__set__(self, name)
        # name_prop: property = super(SubPerson, self).name
        # name_prop.__set__(name)

    @name.deleter
    def name(self):
        print('Deletigh name')
        super(SubPerson, SubPerson).name.__delete__(self)
        # name_prop: property = super(SubPerson, self).name
        # name_prop.__delete__()


s = SubPerson("dima")
print(s.name)
# del s.name

prn_tem('8.9. Creating a New Kind of Class or Instance Attribute')


class Integer:
    def __init__(self, name: str):
        self.name = name

    def __get__(self, instance: object, owner: type):
        return instance.__dict__[self.name]

    def __set__(self, instance: object, value: int):
        if not isinstance(value, int):
            raise TypeError('Expected int type')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


p1 = Point(3, 5)


# p2 = Point(1, 9.3)


class Typed:
    def __init__(self, name: str, expected_type: type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance: object, owner: type):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {repr(self.expected_type)}')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def typeassert(**kwargs):
    def decorate(cls: type):
        for atr_name, atr_type in kwargs.items():
            setattr(cls, atr_name, Typed(atr_name, atr_type))
        return cls

    return decorate


@typeassert(name=str, share=int, price=float)
class Stock:
    def __init__(self, name: str, share: int, price: float):
        self.name = name
        self.share = share
        self.price = price


s = Stock(name='cofe', share=1010, price=12.23)
print(s)

prn_tem('8.10. Using Lazily Computed Properties')

import time


class lazyprop:
    def __init__(self, fun: typing.Callable):
        self.fun = fun

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print('sleep')
        # time.sleep(1)
        val = self.fun(instance)
        setattr(instance, self.fun.__name__, val)
        return val


import math


def lazupropfun(fun: typing.Callable):
    name = '_lazy_' + fun.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        print('sleep in lazy fun')
        # time.sleep(1)
        val = fun(self)
        setattr(self, name, val)
        return val

    return lazy


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @lazyprop
    def area(self):
        return math.pi * self.radius ** 2

    @lazyprop
    def perimetr(self):
        return 2 * math.pi * self.radius

    @lazupropfun
    def area2(self):
        return math.pi * self.radius ** 2


c = Circle(4)
print(c)
print(vars(c))
print(c.area)
print(c.perimetr)

print(c.area)
print(c.perimetr)
print(vars(c))
print(c.area2)
print(vars(c))
# c.area2 = 20

prn_tem('8.11. Simplifying the Initialization of Data Structures')


class Structure:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} argument')
        for arg_name, value in zip(self._fields, args):
            setattr(self, arg_name, value)


class Stock(Structure):
    _fields = ['name', 'shres', 'price']


class Point(Structure):
    _fields = ['x', 'y', 'z']


class Circle(Structure):
    _fields = ['radius']

    @lazupropfun
    def area(self):
        return math.pi * 2 * self.radius ** 2


s = Stock('acme', 50, 91.1)
p = Point(2, 3, 7)
c = Circle(10)
# p2 = Point(1)
print(c.area)


class Structure2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)
        keys = kwargs.keys() - self._fields
        for name in keys:
            setattr(self, name, kwargs[name])


class Stock(Structure2):
    _fields = ['name', 'shres', 'price']


class Point(Structure2):
    _fields = ['x', 'y', 'z']


class Circle(Structure2):
    _fields = ['radius']

    @lazupropfun
    def area(self):
        return math.pi * 2 * self.radius ** 2


s = Stock('acme', 50, 91.1, name2='test')
p = Point(2, 3, 7, name='test')
c = Circle(10, name='test')
# p2 = Point(1)
print(c.area)
print(s.name2)
print(p.name)
print(c.name)
help(Stock)

import sys

prn_tem('8.12. Defining an Interface or Abstract Base Class')
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


try:
    obj1 = IStream()
except TypeError as ex:
    print('obj1 = IStream() except raised')


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        ...

    def write(self, data):
        ...


stream = SocketStream()
print('isinstance(stream, IStream) ', isinstance(stream, IStream))

import io

print('IStream.register(io.IOBase)', IStream.register(io.IOBase))


def custom_prop(fun: typing.Callable):
    name = 'custom-' + fun.__name__
    # @property


class Person:
    def __init__(self, name):
        self._mame = name

    @property
    def name(self):
        print('in get name Person')
        return self._mame

    @name.setter
    def name(self, name):
        self._mame = name
        print('in set name Person')

    @name.deleter
    def name(self):
        print('in del name Person')
        del self._mame


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('in get name SubPerson')

    # @Person.name.setter
    # def name(self, name):


class TextDesc:
    def __set_name__(self, owner: type, name: str):
        print(f'init TestDesc: name {name}, owner {owner.__name__} ')
        self.name = name

    def __get__(self, instance, owner):
        print(f'get data')
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f'set data')
        pass
        # instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f'del data')
        pass
        # del instance.__dict__[self.name]


class TestClass1:
    var1 = TextDesc()

    def __init__(self, var1):
        self.__dict__[TestClass1.var1.name] = var1


var1 = TestClass1('test var')
var1.var1 = 'sldfkjsdlkfj'
print(var1.var1)
var1.var1 = "22222222"
print(vars(var1))
del var1.var1
print(vars(var1))
var1.var1 = "3333333"
print(vars(var1))


class D:
    def f(self, x):
        return x


obj = D()
print(D.f)
print(D.f.__qualname__)
print(D.__dict__['f'])
print(obj.f)
print(obj.f.__func__)
print(obj.f.__self__)
print(obj)

prn_tem('8.13. Implementing a Data Model or Type System')
from abc import ABCMeta, abstractmethod


class Descriptor:
    def __set_name__(self, owner, name):
        print(f'int desck owner: {owner}, name: {name}')
        self.name = name

    def __init__(self, name=None, **opt):
        setattr(self, 'name', name)
        for k, v in opt.items():
            setattr(self, k, v)

    def __set__(self, instance, value):
        self.verify(instance, value)
        instance.__dict__[self.name] = value

    # @abstractmethod
    def verify(self, instance, value):
        pass


class Typed(Descriptor):
    expected_type = type(None)

    def verify(self, instance, value):
        if not issubclass(type(value), self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().verify(instance, value)


class Unsigned(Descriptor):
    def verify(self, instance, value):
        if value < 0:
            raise TypeError('expected unsigned value')
        super().verify(instance, value)


class MaxSized(Descriptor):
    def __init__(self, **opt):
        if 'size' not in opt.keys():
            raise TypeError("missing size option")
        super().__init__(**opt)

    def verify(self, instance, value):
        if (size := self.size) < len(value):
            raise TypeError(f'value should be < {size}')
        super().verify(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignetInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignetFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


class Stock:
    name = SizedString(size=8)
    shares = UnsignetInteger()
    price = UnsignetFloat()

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price


st = Stock('ACME', 50, 91.1)

print(st.name)
print(st.price)
try:
    st.shares = 1.2
except TypeError as ex:
    print(f'exception cathet {ex.args}')


# st.price = 70
# print(st.price)

def check_attributes(**kwargs):
    def decorate(cls):
        for k, v in kwargs.items():
            setattr(cls, k, v)
        return cls

    return decorate


@check_attributes(name=SizedString(name='name', size=8),
                  shares=UnsignetInteger(name='shares'),
                  price=UnsignetFloat(name='price'))
class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price


st = Stock('ACME', 50, 91.1)
print(st.name)
print(st.price)
try:
    st.shares = 1.2
except TypeError as ex:
    print(f'exception cathet {ex.args}')


class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # methods = kwargs['methods']
        for name, method in methods.items():
            if isinstance(method, Descriptor):
                cls.name = name
        return super().__new__(cls, clsname, bases, methods)


class Stock(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignetInteger()
    price = UnsignetFloat()

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price


st = Stock('ACME', 50, 91.1)

print(st.name)
print(st.price)
try:
    st.shares = 1.2
except TypeError as ex:
    print(f'exception cathet {ex.args}')


class DescriptorDecorator:
    def __init__(self, name=None, **args):
        self.verifi_init(**args)
        self.name = name
        for name, value in args.items():
            setattr(self, name, value)

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        self.verifi_set(instance, value)
        instance.__dict__[self.name] = value

    def verifi_set(self, instance, value):
        pass

    def verifi_init(self, **args):
        pass


def typed(expecte_type: type, cls: DescriptorDecorator = None):
    if cls == None:
        return lambda cls: typed(expecte_type, cls)
    super_verifi_set = cls.verifi_set

    def cls_verifi_set(self, intance, value):
        if not isinstance(value, expecte_type):
            raise TypeError(f'Expected {str(expecte_type)}')
        super_verifi_set(self, intance, value)

    cls.verifi_set = cls_verifi_set
    return cls


def unsigned(cls: DescriptorDecorator):
    super_verifi_set = cls.verifi_set

    def cls_verifi(self, intance, value):
        if value < 0:
            raise TypeError(f'Expected value >= 0')
        super_verifi_set(self, intance, value)

    cls.verifi_set = cls_verifi
    return cls


def maxsized(cls: DescriptorDecorator):
    super_verifi_init = cls.__init__

    def cls_verifi_init(self, **args):
        if 'size' not in args.keys():
            raise TypeError('Missing size optin')
        super_verifi_init(self, **args)

    super_verifi_set = cls.verifi_set

    def cls_verifi_set(self, intance, value):
        if value < 0:
            raise ValueError(f'Expected value >= 0')
        super_verifi_set(self, intance, value)

    cls.verifi_set = cls_verifi_set
    cls.verifi_init = cls_verifi_init
    return cls


prn_tem('8.14. Implementing Custom Containers')

import collections.abc
import bisect


class A(collections.abc.Iterable):
    def __iter__(self):
        pass


class SortedItems(collections.abc.Sequence):
    def __init__(self, initial: collections.abc.Sequence = None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


itemls = SortedItems([10, 2, 5, 1, 7, 4, 3])

print(isinstance(itemls, collections.abc.Iterable))

prn_tem('8.15. Delegating Attribute Access')


class Delegat:
    def spam(self):
        print('Delegat spam')

    def foo(self):
        print('Delegat foo')


class Wrapper:
    def __init__(self):
        self.__delegat = Delegat()

    # def spam(self):
    #     # print('Wraper spav')
    #     # self.__delegat.spam()
    #     pass
    #
    #
    # def foo(self):
    #     # print('Wraper foo')
    #     # self.__delegat.foo()
    #     pass

    def __getattr__(self, item):
        return getattr(self.__delegat, item)


obj = Wrapper()
obj.foo()
obj.spam()


class Proxy:
    def __init__(self, delegat):
        self._delegate = delegat

    def __getattr__(self, name):
        print(f'__getattr__({self}, {name})')
        return getattr(self._delegate, name)

    def __setattr__(self, name: str, value):
        print(f'def __setattr__({self}, {name}, {value})')
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._delegate, name, value)

    def __delattr__(self, name):
        print(f'def __delattr__({self}, {name})')
        if name.startswith('_'):
            super().__delattr__(name, name)
        else:
            delattr(self._delegate, name)


class Spam:
    def __init__(self, x):
        self.x = x

    def __len__(self):
        print('Spam.__som_spam__(self)')

    def bar(self, y):
        print(f'Spam.bar: {self.x}{y}')


obj = Proxy(Spam(5))

print(obj.x)
obj.bar(6)
obj.__len__()
# len(obj)

prn_tem('8.16. Defining More Than One Constructor in a Class')
import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls: Date):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


prn_tem('8.17. Creating an Instance Without Invoking init')


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)
dic = {'year': 2020, 'month': 8, 'day': 27}
for k, v in dic.items():
    setattr(d, k, v)
print(d.year)
print(d.month)
print(d.day)

prn_tem('8.19. Implementing Stateful Objects or State Machines')


class Connection:
    def __init__(self):
        self._new_connection_state(ClosedConnectionState)

    def _new_connection_state(self, connection_state):
        self._c_state = connection_state

    def open(self):
        pass

    def close(self):
        pass

    def read(self):
        pass

    def write(self, data):
        pass


class ConnectionState:
    @staticmethod
    def open(connection):
        raise NotImplementedError()

    @staticmethod
    def close(connection):
        raise NotImplementedError()

    @staticmethod
    def read(connection):
        raise NotImplementedError()

    @staticmethod
    def write(connection, data):
        raise NotImplementedError()


class ClosedConnectionState(ConnectionState):
    @staticmethod
    def open(connection):
        raise connection._new_connection_state(OpenConnectionState)

    @staticmethod
    def close(connection):
        raise RuntimeError('connection already closed')

    @staticmethod
    def read(connection):
        raise RuntimeError('connection closed')

    @staticmethod
    def write(connection, data):
        raise RuntimeError('connection closed')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def open(connection):
        raise RuntimeError('connection already open')

    @staticmethod
    def close(connection):
        raise connection._new_connection_state(ClosedConnectionState)

    @staticmethod
    def read(connection):
        print('read connection')

    @staticmethod
    def write(connection, data):
        print('write connection')


c = Connection()


class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, connection):
        self.__class__ = connection

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

    def read(self):
        raise NotImplementedError()

    def write(self, dane):
        raise NotImplementedError()


class ClosedConnection(Connection):
    def open(self):
        print('opening connection')
        self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError('Non open')

    def read(self):
        raise RuntimeError('Not open')

    def write(self, dane):
        raise RuntimeError('Not open')


class OpenConnection:
    def open(self):
        raise RuntimeError('Already open')

    def close(self):
        self.new_state(ClosedConnection)

    def read(self):
        print('read')

    def write(self, dane):
        print('write')


c = Connection()
print(c)
try:
    c.read()
except RuntimeError as ex:
    print('exeption cauth')
c.open()
c.write('lsdfkj')
c.read()


class State:
    def __init__(self):
        self.set_state(StateA)

    def set_state(self, state):
        self.__class__ = state

    def action(self):
        raise NotImplementedError()


class StateA(State):
    def action(self):
        print('StateA action')
        self.set_state(StateB)


class StateB(State):
    def action(self):
        print('StateB action')


prn_tem('8.20. Calling a Method on an Object Given the Name As a String')
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point {self.x!r}, {self.y!r}'

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(4, 10)
d = getattr(p, 'distance')(0, 0)
print(d)

import operator

print(operator.methodcaller('distance', -1, 20)(p))
points = [
    Point(1, 2),
    Point(3, 6),
    Point(-2, 2),
    Point(10, -2),
    Point(11, -22),
    Point(34, 2),
    Point(1, -2),
    Point(1, -2)
]

points.sort(key=operator.methodcaller('distance', 0, 0))
print(points)

prn_tem('8.21. Implementing the Visitor Pattern')


class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operator):
        self.operator = operator


class BinaryOperator(Node):
    def __init__(self, left, rite):
        self.left = left
        self.rite = rite


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Myl(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


t1 = Sub(Number(1), Number(4))
t2 = Myl(Number(4), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)


class NodeVisitor:
    def visit(self, node: Node):
        methname: str = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError(f'No visit_{type(node).__name__} method')


class Evaluator(NodeVisitor):
    def visit_Number(self, node: Number) -> Union[int, float]:
        return node.value

    def visit_Add(self, node: Add) -> Union[int, float]:
        return self.visit(node.left) + self.visit(node.rite)

    def visit_Sub(self, node: Sub) -> Union[int, float]:
        return self.visit(node.left) - self.visit(node.rite)

    def visit_Myl(self, node: Myl) -> Union[int, float]:
        return self.visit(node.left) * self.visit(node.rite)

    def visit_Div(self, node: Div) -> Union[int, float]:
        return self.visit(node.left) / self.visit(node.rite)

    def visit_Negate(self, node: Negate) -> Union[int, float]:
        return -node.operator


e = Evaluator()
print(e.visit(t4))


class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def binop(self, nod: BinaryOperator, instruction: str):
        self.visit(nod.left)
        self.visit(nod.rite)
        self.instructions.append((instruction,))

    def visit_Number(self, node: Number):
        self.instructions.append(('PUSH', node.value))

    def visit_Add(self, node: Add) -> None:
        self.binop(node, 'ADD')

    def visit_Sub(self, node: Sub) -> None:
        self.binop(node, "SUB")

    def visit_Myl(self, node: Myl) -> None:
        self.binop(node, "MYL")

    def visit_Div(self, node: Div) -> None:
        self.binop(node, "DIV")

    def unaruop(self, node: UnaryOperator, instruction):
        self.visit(node)
        self.instructions.append((instruction,))

    def visit_Negate(self, node: Negate) -> None:
        self.unaruop(node, 'NEG')


s = StackCode()
print(s.generate_code(t4))

a = Number(0)
for i in range(1, 100000):
    a = Add(a, Number(i))
try:
    print(e.visit(a))
except RecursionError:
    print('RecursionError occurs')

prn_tem('8.22. Implementing the Visitor Pattern Without Recursion')
import types


class NodeVisitor:
    def visit(self, node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                elif isinstance(last, typing.Generator):
                    stack.append(last.send(last_result))
                    last_result = None
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result

    def _visit(self, node):
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name)
        return method(node)


class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def binop(self, nod: BinaryOperator, instruction: str):
        yield nod.left
        yield nod.rite
        self.instructions.append((instruction,))

    def visit_Number(self, node: Number):
        self.instructions.append(('PUSH', node.value))

    def visit_Add(self, node: Add) -> None:
        return self.binop(node, 'ADD')

    def visit_Sub(self, node: Sub) -> None:
        return self.binop(node, "SUB")

    def visit_Myl(self, node: Myl) -> None:
        return self.binop(node, "MYL")

    def visit_Div(self, node: Div) -> None:
        return self.binop(node, "DIV")

    def unaruop(self, node: UnaryOperator, instruction):
        yield node
        self.instructions.append((instruction,))

    def visit_Negate(self, node: Negate) -> None:
        return self.unaruop(node, 'NEG')


s = StackCode()
print(s.generate_code(t4))


class Evaluator(NodeVisitor):
    def visit_Number(self, node: Number) -> Union[int, float]:
        yield node.value

    def visit_Add(self, node: Add) -> Union[int, float]:
        yield (yield node.left) + (yield node.rite)

    def visit_Sub(self, node: Sub) -> Union[int, float]:
        yield (yield node.left) - (yield node.rite)

    def visit_Myl(self, node: Myl) -> Union[int, float]:
        yield (yield node.left) * (yield node.rite)

    def visit_Div(self, node: Div) -> Union[int, float]:
        yield (yield node.left) / (yield node.rite)

    def visit_Negate(self, node: Negate) -> Union[int, float]:
        return -node.operator


e = Evaluator()
print(e.visit(t4))
a = Number(0)
for i in range(1, 100000):
    a = Add(a, Number(i))
print(e.visit(a))

prn_tem('8.23. Managing Memory in Cyclic Data Structures')
import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return f'Node {self.value!r:}'

    @property
    def parent(self):
        return self._parent if self._parent in None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)


class Data:
    def __del__(self):
        print('Data.__del__')
        # super().__del__()


class Node:
    def __init__(self):
        self.data = Data()
        self.children = []
        self.parent = None

    def add_child(self, node: Node):
        self.children.append(node)
        node.parent = weakref.ref(self)


a = Data()
del a
a = Node()
del a
a = Node()
a.add_child(Node())
del a

prn_tem('8.24. Making Classes Support Comparison Operations')

from functools import total_ordering


class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.squere_feet = self.length * self.width


@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms: List[Room] = []

    @property
    def living_space_footage(self):
        return sum(r.squere_feet for r in self.rooms)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def __str__(self):
        return (f'{self.name!s:}: '
                f'{self.living_space_footage!s:} '
                f'square foot {self.style!s:}')

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


h1 = House('h1', 'Cape')
h1.add_room(Room('Master Bedroom', 14, 21))
h1.add_room(Room('Living Room', 18, 20))
h1.add_room(Room('Kitchen', 12, 16))
h1.add_room(Room('Office', 12, 12))
h2 = House('h2', 'Ranch')
h2.add_room(Room('Master Bedroom', 14, 21))
h2.add_room(Room('Living Room', 18, 20))
h2.add_room(Room('Kitchen', 12, 16))
h3 = House('h3', 'Split')
h3.add_room(Room('Master Bedroom', 14, 21))
h3.add_room(Room('Living Room', 18, 20))
h3.add_room(Room('Office', 12, 16))
h3.add_room(Room('Kitchen', 15, 17))
houses = [h1, h2, h3]
print('Is h1 bigger than h2?', h1 > h2)  # prints True
print('Is h2 smaller than h3?', h2 < h3)  # prints True
print('Is h2 greater than or equal to h1?', h2 >= h1)  # Prints False
print('Which one is biggest?', max(houses))  # Prints 'h3: 1101-square-foot Split'
print('Which is smallest?', min(houses))  # Prints 'h2: 846-square-foot Ranch'

prn_tem('8.25. Creating Cached Instances')
import weakref


class Spam:
    _spam_cache = weakref.WeakValueDictionary()

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_spam_for_name(cls, name: str):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        spam = cls(name)
        cls._spam_cache[name] = spam
        return spam


s1 = Spam.get_spam_for_name('name1')
s2 = Spam.get_spam_for_name('name1')
s3 = Spam.get_spam_for_name('name2')
print(s1 is s2)
print(s1 is s3)
print(list(Spam._spam_cache))
del s3
print(list(Spam._spam_cache))
del s1
print(list(Spam._spam_cache))
del s2
print(list(Spam._spam_cache))

import weakref


class Spam:
    _cache = weakref.WeakValueDictionary()

    def __init__(self):
        raise RuntimeError('Can`t instantiate directly')

    @classmethod
    def _new(cls, name):
        if name in cls._cache:
            return cls._cache[name]
        inst = cls.__new__(cls)
        inst.name = name
        cls._cache[name] = inst
        return inst


class Spam2:
    def __init__(self, *args, **kwargs):
        raise RuntimeError('Can`t instantiate directly')

    @classmethod
    def _new(cls, name):
        inst = cls.__new__(cls)
        inst.name = name
        return inst

class Spam2CacheManager:
    _spam_cache = weakref.WeakValueDictionary()
    def __init__(self):
        pass
    @classmethod
    def get_spam2(cls, name):
        if inst := cls._spam_cache.get(name):
            return inst
        inst = Spam2._new(name)
        cls._spam_cache[name] = inst
        return inst


