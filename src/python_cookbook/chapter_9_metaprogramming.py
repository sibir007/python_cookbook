from chapter_0 import prn_tem

prn_tem('9.1. Putting a Wrapper Around a Function')
import time
from functools import wraps
import typing


def timethis(fun: typing.Callable):
    # @wraps(fun)
    def wrapper(*args, **kwargs):
        statr = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f'{fun.__name__} exec time {end - statr}')
        return result

    return wrapper


@timethis
def countdown(n: int):
    while n := n - 1:
        pass


countdown(1000000)

prn_tem('9.2. Preserving Function Metadata When Writing Decorators')
import time
from functools import wraps


def timethis(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f'{fun.__name__} execution time {end - start}')
        return result

    return wrapper


@timethis
def countdown(n: int) -> None:
    """
    counts down
    :param n:
    :return:
    """
    while n := n - 1:
        pass


countdown(1000000)
print(countdown.__doc__)
print(countdown.__annotations__)
countdown.__wrapped__(100000)
from inspect import signature

print(signature(countdown))

prn_tem('9.3. Unwrapping a Decorator')


@timethis
def add(x: typing.Union[int, float], y: typing.Union[int, float]) -> typing.Union[int, float]:
    return x + y


prn_tem('9.4. Defining a Decorator That Takes Arguments')

from functools import wraps
import logging


def logged(level, name=None, message=None):
    def decorate(fun):
        logname = name if name else fun.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else fun.__name__

        @wraps(fun)
        def wrap(*args, **kwargs):
            log.log(level, logmsg)
            return fun(*args, **kwargs)

        return wrap

    return decorate


@logged(level=logging.DEBUG)
def add(x: typing.Union[int, float], y: typing.Union[int, float]) -> typing.Union[int, float]:
    return x + y


print(add.__annotations__)
r = add(100, 200)


@logged(level=logging.DEBUG, name='example')
def spam():
    print('spam')


spam()
prn_tem('9.5. Defining a Decorator with User Adjustable Attributes')
from functools import wraps, partial
import logging


def attach_wrapper(obj, fun=None):
    if not fun:
        return partial(attach_wrapper, obj)
    setattr(obj, fun.__name__, fun)


def logged(level, name=None, message=None):
    def decorate(fun: typing.Callable) -> typing.Callable:
        logname = name if name else fun.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else fun.__name__

        @wraps(fun)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            # print('здесь должен быть логгер')
            return fun(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate


@logged(logging.INFO)
def add(x, y):
    return x + y


add(3, 3)
add.set_message("new new newmsg")
add(12, 3)
add.set_level(logging.DEBUG)
add(19, 3)


@logged(logging.DEBUG, 'exemple')
def spam():
    print('spam ' * 3)


spam()

spam.set_level(logging.DEBUG)
spam()


@timethis
@logged(logging.DEBUG)
def countdown(n):
    while n := n - 1:
        pass


countdown(100000)

log = logging.getLogger('test logger')
log.info('looooooooog')

prn_tem('9.6. Defining a Decorator That Takes an Optional Argument')
from functools import wraps, partial
import logging


def logged(fun=None, *, level=logging.DEBUG, name=None, message=None):
    if not fun:
        return partial(logged, level=level, name=name, message=message)
    log_name = name if name else fun.__module__
    log_msg = message if message else fun.__name__
    logger = logging.getLogger(log_name)

    @wraps(fun)
    def wrapper(*args, **kwargs):
        logger.log(level, log_msg)
        return fun(*args, **kwargs)

    return wrapper


@logged
def add(a, b):
    return a + b


print(add(10, 100))


@logged(level=logging.INFO, name='example')
def spam():
    print('spam ' * 3)


spam()
prn_tem('9.7. Enforcing Type Checking on a Function Using a Decorator')
from inspect import signature
from functools import wraps


def spam(x, y, z=42) -> typing.Any:
    print(x + y)


sig = signature(spam)
print(sig)


def typyassert(*ty_args, **ty_kwords):
    def decorate(fun):
        if not __debug__:
            return fun
        sig = signature(fun)
        bound_types = sig.bind_partial(*ty_args, **ty_kwords).arguments

        @wraps(fun)
        def wrapper(*args, **kwargs):
            bound_value = sig.bind(*args, **kwargs)
            for name, value in bound_value.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            f'Argument {name} must be {bound_types[name]}'
                        )
            return fun(*args, **kwargs)

        return wrapper

    return decorate


@typyassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


spam(1, 2, 3)
spam(1, 'hello', 3)
try:
    spam(2, 'hello', 'hello')
except TypeError as ex:
    print(f'exeption {ex}')

prn_tem('9.8. Defining Decorators As Part of a Class')

from functools import wraps


class A:
    def decorator1(self, fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            print('decorator 1')
            return fun(*args, **kwargs)

        return wrapper

    @classmethod
    def decorator2(cls, fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            print('decorator2')
            return fun(*args, **kwargs)

        return wrapper


a = A()


@a.decorator1
def spam1():
    print(spam1.__name__)


@A.decorator2
def spam2():
    print(spam2.__name__)


spam2()
spam1()
prn_tem('9.9. Defining Decorators As Classes')
import types
from functools import wraps


class Profiled:
    def __init__(self, fun):
        wraps(fun)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, inst, cls):
        if inst is None:
            return self
        else:
            return types.MethodType(self, inst)


@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


add(2, 3)
add(5, 3)
add(2, 7)
print(add.ncalls)

s = Spam()
s.bar(4)
s.bar.ncalls

import types
from functools import wraps


def profiled(fun):
    ncalls = 0

    @wraps(fun)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return fun(*args, **kwargs)

    wrapper.ncalls = lambda: ncalls
    return wrapper


@profiled
def add(x, y):
    return y + x


add(2, 3)
add(2, 3)
add(2, 3)
add(2, 3)
add(2, 3)
print(add.ncalls())

prn_tem('9.10. Applying Decorators to Class and Static Methods')
import time
from functools import wraps


def timethis(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        stime = time.time()
        res = fun(*args, **kwargs)
        etime = time.time()
        print(f'fun {fun.__name__} elapsed time {-(stime - etime)}')
        return res

    return wrapper


class Spam:
    @timethis
    def instance_method(self, n):
        while n := n - 1:
            pass

    @classmethod
    @timethis
    def class_method(cls, n):
        while n := n - 1:
            pass

    @staticmethod
    @timethis
    def static_method(n):
        while n := n - 1:
            pass


@timethis
def fun(n):
    while n := n - 1:
        pass


n = 10000000
inst = Spam()
inst.instance_method(n)
inst.class_method(n)
Spam.static_method(n)
fun(n)
prn_tem('9.11. Writing Decorators That Add Arguments to WrappedFunctions')
from functools import wraps
import inspect


def optional_debug(fun: typing.Callable):
    if 'debug' in inspect.signature(fun).parameters.keys():
        raise TypeError('debug argument already defined')

    @wraps(fun)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print(f'Calling fun.__name__ {fun.__name__}')
        return fun(*args, **kwargs)

    sig = inspect.signature(fun)
    param = list(sig.parameters.values())
    param.append(inspect.Parameter('debug',
                                   inspect.Parameter.KEYWORD_ONLY,
                                   default=False))
    wrapper.__signature__ = sig.replace(parameters=param)
    return wrapper


@optional_debug
def spam(x, y):
    print(f'Call {spam.__name__}')


spam(2, 3)
spam(2, 4, debug=True)
print(inspect.signature(spam))

try:
    @optional_debug
    def spam2(debug):
        pass
except TypeError as exc:
    print(f'exception cauth {exc}')

prn_tem('9.12. Using Decorators to Patch Class Definitions')


def log_getattribute(cls: type):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print(f'Call {cls.__name__}__getattribute__(inst, {name})')
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls


@log_getattribute
class Spam:
    def bar(self):
        print('Call bar()')


spam = Spam()
spam.bar()

prn_tem('9.13. Using a Metaclass to Control Instance Creation')


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if inst := self.__instance:
            return inst
        self.__instance = super().__call__(*args, **kwargs)
        return self.__instance


class Spam(metaclass=Singleton):
    def __init__(self):
        print('Create Spam')


s1 = Spam()
s2 = Spam()
print(s1 is s2)

import weakref


class Cached(type):
    def __init__(self, *args):
        self.__cached_instances = weakref.WeakValueDictionary()
        super().__init__(*args)

    def __call__(self, *args):
        # print(args)
        # print(self.__cached_instances.get(args))
        if inst := self.__cached_instances.get(args):
            # print(args)
            return inst
        obj = super().__call__(*args)
        self.__cached_instances[args] = obj
        return self.__cached_instances.get(args)


class Spam(metaclass=Cached):
    def __init__(self, x):
        print('create Spam instance')
        self.x = x


s1 = Spam(3)
s2 = Spam(4)
s3 = Spam(3)
print(s1 is s2)
print(s1 is s3)


class _Spam:
    def __init__(self):
        print('Create instance _Spame')


_spam_instance = None


def Spam():
    global _spam_instance
    if _spam_instance:
        return _spam_instance
    _spam_instance = _Spam()
    return _spam_instance


prn_tem('9.14. Capturing Class Attribute Definition Order')
from collections import OrderedDict


class Typed:
    _type = type(None)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError(f'Expected {str(self._type)} type')
        instance.__dict__[self._name] = value


class Integer(Typed):
    _type = int


class Float(Typed):
    _type = float


class String(Typed):
    _type = str


class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = [name for name, value in clsdict.items() if isinstance(value, Typed)]
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()


class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)


class Store(Structure):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s1 = Store('GOOG', 100, 490.1)
print(s1.as_csv())
try:
    s1 = Store('GOOG', 'fail', 490.1)
except TypeError as ex:
    print(f'Exception {ex}')

from collections import OrderedDict


class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname):
        self._clsname = clsname

    def __setitem__(self, key, value):
        if key in self:
            raise TypeError(f'name {key} already defined in class {self._clsname}')
        super().__setitem__(key, value)


class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        d['_order'] = [name for name in clsdict if name[0] != '_']
        type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(metacls, name, bases):
        return NoDupOrderedDict(name)


try:
    class A(metaclass=OrderedMeta):
        def spam(self):
            pass

        def spam(self):
            pass
except TypeError as ex:
    print(f'Exception {ex}')

prn_tem('9.15. Defining a Metaclass That Takes Optional Arguments')


class MyMeta(type):
    # optional
    @classmethod
    def __prepare__(metacls, name, bases, *, debug=False, synchronize=False):
        return super().__prepare__(name, bases)

    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        return super().__new__(cls, name, bases, ns)

    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        super().__init__(name, bases, ns)


class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    pass


prn_tem('9.16. Enforcing an Argument Signature on *args and **kwargs')
from inspect import Signature, Parameter

param = [
    Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
    Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
    Parameter('z', Parameter.KEYWORD_ONLY, default=None)
]
sig = Signature(param)
print(sig)


def fun(*args, **kwargs):
    bound_value = sig.bind(*args, **kwargs)
    for name, value in bound_value.arguments.items():
        print(name, value)


fun(1, 2, z=3)
fun(x=0, y=1)
try:
    fun(1, 2, 3, 4)
except TypeError as ex:
    print(f'Exception {ex}')

from inspect import Parameter, Signature


def make_sig(*names):
    param = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(param)


class Structure:
    __signature__: Signature = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


import inspect

print(inspect.signature(Stock))

prn_tem('9.17. Enforcing Coding Conventions in Classes')


class MyMeta1(type):
    def __new__(self, clsname, bases, clsdir):
        return super().__new__(clsname, bases, clsdir)


class MyMeta2(type):
    def __init__(self, clsname, bases, clsdir):
        super().__init__(clsname, bases, clsdir)


class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdir):
        for name in clsdir:
            if name.lower() != name:
                raise TypeError(f'Bad attribute name: {name}')
        return super().__new__(cls, clsname, bases, clsdir)


class Root(metaclass=NoMixedCaseMeta):
    pass


class A(Root):
    def boo(self):
        pass

    def foo(self):
        pass


try:
    class B(Root):
        Name = 'spam'
except TypeError as ex:
    print(f'Exception {ex}')

from inspect import signature
import logging


class CheckMethodSignature(type):
    def __init__(cls, clsname, bases, clsdict):
        sup = super(cls, cls)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            # prev_val =
            prev_val = getattr(sup, name, None)
            print(f'{clsname} {prev_val} pre if prev_val := getattr(sup, name, None):')
            if prev_val:
                print(f'{clsname} {prev_val} past if prev_val := getattr(sup, name, None):')
                prev_sig = signature(prev_val)
                cur_sig = signature(value)
                if prev_sig != cur_sig:
                    print(f'signature mismatch in {value.__qualname__}. {prev_sig} != {cur_sig}')
                    # logging.warning(f'signature mismatch in {value.__qulname__}. {prev_sig} != {cur_sig}')
        # return super().__new__(cls, clsname, bases, clsdict)


class Root(metaclass=CheckMethodSignature):
    pass


class A(Root):
    def foo(self, x, y, z):
        pass


class B(A):
    def foo(self, x, y):
        pass


prn_tem('9.18. Defining Classes Programmatically')


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}
import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__
s = Stock('ACME', 50, 43.2)
print(s)

print(s.cost())
from abc import ABCMeta

Stock = types.new_class('Stock', (), {'metaclass': ABCMeta}, lambda ns: ns.update(cls_dict))

Stock.__module__ = __name__
print(Stock)
import collections

Stock = collections.namedtuple('Stock', ['name', 'shares', 'price'])
print(Stock)

import operator
import types
import sys


def named_tuple(cls_name, field_names):
    cls_dict = {name: property(operator.itemgetter(n))
                for n, name
                in enumerate(field_names)}

    def __new__(cls, *args):
        l1 = len(field_names)
        l2 = len(args)
        if l1 != l2:
            raise TypeError(f'Expected {l1} arguments - passed {l2}')
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    cls = types.new_class(cls_name,
                          (tuple,),
                          {},
                          lambda ns: ns.update(cls_dict))

    return cls


Spam = named_tuple('Spam', ['name', 'shares', 'price'])
s1 = Spam('ACME', 50, 91.1)
print(s1)
Point = named_tuple('Point', ['x', 'y'])
p1 = Point(3, 4)
print(p1)
try:
    p2 = Point(3, 4, 5)
except TypeError as ex:
    print(f'Exception {ex}')

prn_tem('9.19. Initializing Class Members at Definition Time')
import operator


class StructTupleMeta(type):
    # def __new__(cls, cls_name, bases: tuple, cls_dict):
    #     tuple_bas = (tuple,)
    #     new_bases = tuple_bas + bases
    #     return super().__new__(cls, cls_name, new_bases, cls_dict)

    def __init__(cls, *args, **kwargs):
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))
            # cls.__dict__[name] = property(operator.itemgetter(n))
        super().__init__(*args, **kwargs)


class Strut(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(self, *args):
        if len(self._fields) != len(args):
            raise ValueError(f'Expected {len(self._fields)}, passed {len(args)}')
        return super().__new__(self, args)


class Stack(Strut):
    _fields = ['name', 'shares', 'price']


class Pint(Strut):
    _fields = ['x', 'y']


s1 = Stack('ACME', 50, 91.1)
print(s1.price)
print(s1)
p1 = Point(3, 4)
print(p1)
try:
    Pint(3, 4, 5)
except ValueError as ex:
    print(f'Exception: {ex}')

prn_tem('9.20. Implementing Multiple Dispatch with Function Annotations')
import inspect
import types


class MultiMethod:
    def __init__(self):
        self._functions = {}

    def register_function(self, function):
        sig = inspect.signature(function)
        param_types = []
        for name, parameter in sig.parameters.items():
            if name == 'self':
                continue
            annotation_value = parameter.annotation
            if annotation_value is inspect.Parameter.empty:
                raise TypeError(
                    f'Argument {name} must be annotated a type'
                )
            if not isinstance(annotation_value, type):
                raise TypeError(
                    f'Argument {name} annotation must be a type'
                )
            param_types.append(annotation_value)
        param_types_tuple = tuple(param_types)
        self._functions[param_types_tuple] = function

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return types.MethodType(self, instance)

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        fun = self._functions.get(types, None)
        if fun is None:
            raise TypeError(f'No matchig method for types {types}')
        return fun(*args)


class MultiDict(dict):
    def __setitem__(self, key, value):
        if isinstance(value, types.FunctionType):
            if key in self:
                multi_method: MultiMethod = self[key]
                multi_method.register_function(value)
                value = multi_method
            else:
                multi_method = MultiMethod()
                multi_method.register_function(value)
                value = multi_method
        super().__setitem__(key, value)
        # if key not in self:
        #     super().__setitem__(key, value)
        # else:
        #     current_value = self[key]
        #     if isinstance(current_value, types.FunctionType):
        #         new_value = MultiMethod(current_value)
        #         new_value


class MultiMethodMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return MultiDict()


class Spam(metaclass=MultiMethodMeta):
    def foo(self, x: int, y: int):
        print(f'Spam.foo(self, {x}, {y})')

    def foo(self, x: int, y: int, z: int):
        print(f'Spam.foo(self, {x}, {y}, {z})')

    def foo(self, x: str, y: float):
        print(f'Spam.foo(self, {x}, {y})')


spam = Spam()
spam.foo(1, 2)
spam.foo(3, 4, 5)
spam.foo('spam', 3.21)
import time


class Dame(metaclass=MultiMethodMeta):
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self):
        dame = time.localtime()
        self.__init__(dame.tm_year, dame.tm_mon, dame.tm_mday)

    def __repr__(self):
        return f'Dame(year: {self.year}, month: {self.month}, day: {self.day})'


d = Dame()
print(d)
print(Dame(1974, 10, 2))

import types
import inspect


class multimethod:
    def __init__(self, fun):
        self.__name__ = fun.__name__
        self._default_fun = fun
        self._fun_match = {}

    def match(self, *type_args):
        for arg in type_args:
            if not isinstance(arg, type):
                raise AttributeError(f'Arguments must be type')

        def wrapper(fun):
            if fun.__name__ != self.__name__:
                raise ValueError(
                    f'Wrapped function name: {fun.__name__} not matched multimetchod name: {self.__name__}')
            fun_param = inspect.signature(fun).parameters.keys()
            if len(fun_param) != len(type_args) + 1:
                raise ValueError(f'Wrapped function parameters quantity: {len(fun_param)} '
                                 f'not matched multimetchod parameters quantity: {len(type_args)}')
            type_args_tuple = tuple(type_args)
            self._fun_match[type_args_tuple] = fun
            return self

        return wrapper

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return types.MethodType(self, instance)

    def __call__(self, *args):
        fun_args = args[1:]
        fun_args_types_tuple = tuple(type(arg) for arg in fun_args)
        match_fun = self._fun_match.get(fun_args_types_tuple, None)
        if match_fun is not None:
            return match_fun(*args)
        return self._default_fun(*args)


class Spam:
    @multimethod
    def bar(self, *args):
        """default method"""
        raise TypeError(f'not match method fo bar {args}')

    @bar.match(int, int, int)
    def bar(self, x, y, z):
        print(f'bar({x},{y},{z})')

    @bar.match(int, str)
    def bar(self, x, y):
        print(f'bar({x},{y})')

    # @bar.match(str, str)
    # def foo(self, x,y):
    #     pass


s = Spam()
s.bar(1, 2, 3)
s.bar(1, 'spam')
try:
    s.bar('spam', 'spam')
except TypeError as ex:
    print(f'Exception {ex}')

try:
    s.bar(1, 2, 3, 4, 5)
except TypeError as ex:
    print(f'Exption {ex}')

prn_tem('9.21. Avoiding Repetitive Property Methods')


def typped_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'{value} must be type: {expected_type}')
        setattr(self, storage_name, value)

    return prop


class Person:
    name = typped_property('name', str)
    age = typped_property('age', int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


from functools import partial

String = partial(typped_property, expected_type=str)
Integer = partial(typped_property, expected_type=int)


class Person:
    name = String('name')
    age = Integer('age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


prn_tem('9.22. Defining Context Managers the Easy Way')
import time
from contextlib import contextmanager


@contextmanager
def time_this():
    start_time = time.time()
    try:
        yield
    except Exception as ex:
        print(f'Exception {ex}')
    finally:
        end_time = time.time()
        print(f'Elapse time: {end_time - start_time}')


with time_this():
    n = 10000000
    while n := n - 1:
        pass


@contextmanager
def list_transacrions(orig_list):
    worcing_list = list(orig_list)
    try:
        yield worcing_list
        orig_list[:] = sorted(worcing_list)
    except Exception as ex:
        print(f'Exception: {ex}')


orig_list = [1, 2, 356, 2, 8, 90]
with list_transacrions(orig_list) as worc_list:
    worc_list.append(4)
    worc_list.append(9)
print(orig_list)

prn_tem('9.23. Executing Code with Local Side Effects')


def exec_test(a):
    loc = locals()
    exec('b = a+1')
    b = loc['b']
    print(b)
exec_test(10)

def test2():
    x=0
    loc = locals()
    print(f'locals befo: {loc}')
    exec('x += 1')
    print(f'locals past: {loc}')
    print(f'x={x}')
test2()
fun1 = """def test_fun():\t\tprint('test fun')\ntest_fun()"""


prn_tem('9.24. Parsing and Analyzing Python Source')
import ast
ex = ast.parse('2+3*4+x', mode='eval')
print(ex)
print(ast.dump(ex))

ex2 = ast.parse(fun1)
print(ast.dump(ex2))
exec(fun1)

prn_tem('9.25. Disassembling Python Byte Code')
def countdown(n):
    while n:=n-1:
        print(f'T-minus {n}')
    print(f'Blastoff {n}')

import dis
d = dis.dis(countdown)
print(d)
c = countdown.__code__.co_code
print(c)
import opcode

print(opcode.opname[c[0]])
