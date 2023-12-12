import http
import io
from typing import List, Any

from chapter_0 import prn_tem

prn_tem('6.1. Reading and Writing CSV Data')
import csv

rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000)]

# with open('test_files/stocks.csv', '+ta') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerows(rows)
#     f.flush()
# f_csv_r = csv.reader(f)
# for line in f_csv_r:
#     print(line)
rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
        {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
        {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
        ]
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
# with open('test_files/stocks.csv', 'at') as f:
#     f_csv = csv.DictWriter(f, headers)
#     f_csv.writerows(rows)

with open('test_files/stocks.csv', 'rt') as f:
    f_csv = csv.reader(f)
    # next(f_csv)
    for line in f_csv:
        print(line)

with open('test_files/stocks.csv', 'rt') as f:
    f_csv = csv.DictReader(f)
    for line in f_csv:
        print(line)

from collections import namedtuple
from datetime import date, time

Row = namedtuple('Row', headers)
namedtuple_rows: List[Row] = []
with open('test_files/stocks.csv', 'rt') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    col_types = [str, float, str, str, float, int]
    for raw_row in f_csv:
        row = tuple(convert(value) for convert, value in zip(col_types, raw_row))
        namedtuple_rows.append(Row(*row))
for namedtuple_row in namedtuple_rows:
    print(namedtuple_row)

prn_tem('6.2. Reading and Writing JSON Data')
import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(data)
print(data)
# print(json_str)
json_str2 = "{'Symbol': 'AXP', 'Price': '62.58', 'Date': '6/11/2007', 'Time': '9:36am', 'Change': '-0.46', 'Volume':'935000'}"
convert_json_str2 = json_str2.replace('\'', '\"')
json_str2_io = io.StringIO(convert_json_str2)

data2: dict = json.load(json_str2_io)
for k in data2:
    print(k, data2[k], sep=': ')
with open('test_files/test_file4', 'w') as f:
    json.dump(data2, f)

with open('test_files/test_file4', 'r') as f:
    data: dict = json.load(f)
    for datum in data:
        print(data[datum])

import urllib.request as req
import json
import http.client
import gzip
from pprint import pprint
import os

url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
# b'sldfjlskfjlskdfjs'.
# b_data.decode()
with req.urlopen(url) as resp:
    resp: http.client.HTTPResponse
    info = resp.info()
    print(info)
    data: bytes = resp.read()
    gzip_file = io.BytesIO(data)
    with gzip.open(gzip_file) as gf:
        json_data = json.loads(gf.read().decode('utf-8'))
        json_str = json.dumps(json_data)
        # if 'json_from_stackoverflow.json' not in os.listdir('test_files'):
        with open('test_files/json_from_stackoverflow.json', 'wt') as f:
            json.dump(json_data, f)

        # pprint(json_data)
        # pprint(json_str)
# pprint(json_data)
print(json.dumps(json_data, indent=4))


class JSONObject:
    def __init__(self, d: dict) -> None:
        self.__dict__ = d


json_object: JSONObject = JSONObject(json_data)
print(json_object.has_more)


class Point:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z


point1: Point = Point(1, 2, 3)


def serialize_instance(obj: Any) -> dict:
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


d_obj = serialize_instance(point1)
print(d_obj)
ser_obj = json.dumps(serialize_instance(point1))

print(ser_obj)
point1_deser = json.loads(ser_obj)
# print(type(point1_deser))
# def unserialize_obj(d:dict) -> Any:
#
classes = {
    'Point': Point
}


def unserialize_object(d: dict):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key in d:
            setattr(obj, key, d[key])
        return obj
    return d


p2 = Point(3.3, 4.3, 5)
print('p2 object', p2)
dict_p2 = serialize_instance(p2)
print(dict_p2)
json_p2 = json.dumps(dict_p2)
print(json_p2)
p21 = json.loads(json_p2, object_hook=unserialize_object)
print(p21)

prn_tem('6.3. Parsing Simple XML Data')
from urllib.request import urlopen
from xml.etree.ElementTree import parse, Element

from http.client import HTTPResponse

# u: HTTPResponse = urlopen('http://planet.python.org/rss20.xml')
# u2: HTTPResponse = urlopen('http://planet.python.org/rss20.xml')
# with open('test_files/xml_from_planet_python_org.xml', 'bw') as f:
#     f.write(u2.read())
with open('test_files/xml_from_planet_python_org.xml', 'rt') as f:
    xml_doc = parse(f)
    coun1 = 0
    coun2 = 0
from pprint import pprint

# import http.client.HTTPResponse

countet = 0
for item in xml_doc.iterfind('channel/item'):
    if countet >= 5:
        break
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)
    print('counter:', countet)
    countet += 1

prn_tem('6.4. Parsing Huge XML Files Incrementally')
from xml.etree.ElementTree import iterparse


def parse_and_remove(filename: str, path: str):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[:-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


dec_iter = parse_and_remove('test_files/xml_from_planet_python_org.xml', 'channel/description')
elem: Element = next(dec_iter)
print(elem.text)

from xml.etree.ElementTree import parse
from collections import Counter

couner = Counter()
xml_doc = parse('test_files/xml_from_planet_python_org.xml')
for elem in xml_doc.iterfind('channel/item'):
    couner[elem.findtext('link')] += 1
for el in couner.most_common():
    print(el)

prn_tem('6.5. Turning a Dictionary into XML')

from xml.etree.ElementTree import Element


def from_dict_to_xml(tag: str, d: dict) -> Element:
    root_elem = Element(tag)
    for k, v in d.items():
        elem = Element(k)
        elem.text = str(v)
        root_elem.append(elem)
    return root_elem


s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
elem = from_dict_to_xml('stock', s)
from xml.etree.ElementTree import tostring

elem.set('_id', '12345')
print(tostring(elem))
print(elem.text)
for el in elem:
    print(el.text)
prn_tem('6.6. Parsing, Modifying, and Rewriting XML')
from xml.etree.ElementTree import parse, Element

doc = parse('test_files/xml_doc_for_change.xml')
root = doc.getroot()

root.remove(root.find('sri'))
root.remove(root.find('cr'))
ind = list(root).index(root.find('nm'))
# root.getchildren().index(root.find('nm'))
new_element = Element('spam')
new_element.text = 'this is a test'
root.insert(ind + 1, new_element)
doc.write('test_files/xml_doc_for_change_var1.xml', xml_declaration=True)

prn_tem('6.7. Parsing XML Documents with Namespaces')

from xml.etree.ElementTree import parse

doc = parse('test_files/xml_doc_whit_namespace.xml')
print(doc.findtext('author'))
print(doc.find('content'))
print(doc.find('content/html'))
print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title'))
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/'
                   '{http://www.w3.org/1999/xhtml}head/'
                   '{http://www.w3.org/1999/xhtml}title'))


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for k, v in kwargs.items():
            self.register(k, v)

    def register(self, name, val):
        self.namespaces[name] = '{' + val + '}'

    def __call__(self, path: str):
        return path.format_map(self.namespaces)


ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
el1 = doc.find(ns('content/{html}html'))
print(el1)
el2 = doc.find(ns('content/{html}html/{html}head/{html}title'))
print(el2.text)

prn_tem('6.8. Interacting with a Relational Database')
stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]
import sqlite3

db = sqlite3.connect('test_files/database.db')
print(db)
c = db.cursor()
# print(c.execute('create table if not exists portfolio (symbol text, shares integer, price real)'))
# db.commit()
# c.executemany('insert into portfolio values (?,?,?)', stocks)
# db.commit()
for fow in db.execute('select * from portfolio'):
    print(fow)
for row in db.execute('select * from portfolio'):
    print(row)
min_price = 100
for row in db.execute('select * from portfolio where price >= ?', (min_price,)):
    print(row)

prn_tem('6.9. Decoding and Encoding Hexadecimal Digits')

s = b'hello'
import binascii

h = binascii.b2a_hex(s)
print(h)

prn_tem('6.11. Reading and Writing Binary Arrays of Structures')
from struct import Struct


def write_records(records, format, f):
    record_struc = Struct(format)
    for r in records:
        f.write(record_struc.pack(*r))


records = [(1, 2.3, 4.5),
           (6, 7.8, 9.0),
           (12, 13.4, 56.7)]
with open('test_files/test_data.b', 'wb') as f:
    write_records(records, '<idd', f)

prn_tem('CHAPTER 7 Functions')
