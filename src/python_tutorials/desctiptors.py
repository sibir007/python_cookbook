import logging

logging.basicConfig(level=logging.INFO)

def my_mod_function():
    logging.info('call my_cls_finciton(self)')


class LoggedAccess:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.privat_name = '_' + name


    def __get__(self, obj, objtype=None):
        logging.info(f'Accessing {self.public_name} giving')
        value = getattr(obj, self.privat_name)
        logging.info(f'Accessing {self.public_name} giving {value}')
        return value

    def __set__(self, instance, value):
        setattr(instance, self.privat_name, value)
        logging.info(f'Updating {self.public_name} to {value}')

class Person:
    name = LoggedAccess()
    age = LoggedAccess()
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age +=1

    def my_cls_finciton(self):
        logging.info('call my_cls_finciton(self)')

    my_static_method = staticmethod(my_cls_finciton)