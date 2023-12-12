from  src.python_cookbook.chapter_0 import prn_tem, get_plach1

print(round(1.23, 1))
x = 1.83838383
print(x, "format(x, '0.2f')", format(x, '0.2f'))
print('Value is {:0.3f}'.format(x))

prn_tem('3.2. Performing Accurate Decimal Calculations')

a = 4.2
b = 2.1
print((a + b))
print(((a + b) == 6.3))
from decimal import Decimal
a =Decimal('4.2')
b =Decimal('2.1')
print((a + b))

from  decimal import  localcontext

a = Decimal('1.3')
b = Decimal('1.7')
print((a + b))
with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)
with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)

prn_tem('3.3. Formatting Numbers for Output')
x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))
print(format(x, '^10,.1f'))
print(format(x, ',.1f'))
print(format(x, '.2E'))
print('The value is {:10,.2f}'.format(x))

prn_tem('3.4. Working with Binary, Octal, and Hexadecimal Integers')
x = 124
print(bin(x))
print(oct(x))
print(hex(x))
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))
print(int('7c', 16))
print(int('1111100', 2))
print(int('777', 8))

prn_tem('Packing and Unpacking Large Integers from Bytes')

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print('data', data)
print('len(data)', len(data))
print("int.from_bytes(data, 'little')",int.from_bytes(data, 'little'))
print("int.from_bytes(data, 'big')",int.from_bytes(data, 'big'))

x = 223479274923814098324701893247
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

prn_tem('3.6. Performing Complex-Valued Math')
prn_tem('3.7. Working with Infinity and NaNs')
a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)
print(a+54, a*10, 10/a)

prn_tem('Calculating with Fractions')
from fractions import Fraction
a = Fraction(4,5)
b = Fraction(7,16)
print((a + b))
print((a * b))
c = a*b
print(c.numerator)
print(c.denominator)
print(float(c))

prn_tem('3.9. Calculating with Large Numerical Arrays')
import numpy as nm
prn_tem('3.11. Picking Things at Random')
import random
values = [1,2,3,4,5,6,7,8,]
print(random.choice(values))
print(random.sample(values, 2))
print(random.sample(values, 4))
print(random.sample(values, 3))
print(random.sample(values, 6))
print(random.sample(values, 7))
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())

prn_tem('3.12. Converting Days to Seconds, and Other Basic Time Conversions')
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=6.4)
c=a+b
print(c)
print(c.days)
print(c.seconds/3600)

from  datetime import datetime
a = datetime(2012,9,23)
print(a + timedelta(days=10))
b = datetime(2012,12,21)
d = b-a
print(d.days)
naw = datetime.today()
print(naw)
print(naw + timedelta(minutes=10))

prn_tem('3.13. Determining Last Friday’s Date')
from datetime import datetime, timedelta, tzinfo

print(tzinfo)
weekdays = ['Monday', 'Tuesday', 'Wednesday' 'Thursday',
'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_data=None):
    if start_data is None:
        start_data = datetime.today()
    day_num = start_data.weekday()
    day_num_target = weekdays.index(day_num)

prn_tem('3.14. Finding the Date Range for the Current Month')

from datetime import datetime, date, timedelta
import calendar
cal1 = calendar.Calendar()
def get_month_range(star_data = None):
    if star_data is None:
        star_data = date.today().replace(day=1)
        # star_data = datetime.today().replace(day=1)
    _, days_in_month = calendar.monthrange(star_data.year, star_data.month)
    end_date = star_data + timedelta(days=days_in_month)
    return (star_data, end_date)
a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day


def data_range(starn: datetime, stop: datetime, step: timedelta):
    while starn < stop:
        yield starn
        starn += step

for d in data_range(datetime(2023,11,1),
                    datetime(2023,11,11),
                    timedelta(hours=6)):
    print(d)

prn_tem('3.15. Converting Strings into Datetimes')
from datetime import datetime
text = '2022-01-13'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
dif = z-y
print(dif)
s = datetime(2012, 9, 23, 21, 37, 4, 177393)
nice_s = datetime.strftime(s, '%A %B %d, %Y')
print(nice_s)
print(datetime.now().tzname())
prn_tem('3.16. Manipulating Dates Involving Time Zones')
from datetime import datetime
import pytz

d = datetime.now()
print(d)
print(d.tzname())
print(pytz.utc)
moscow_tz = pytz.timezone('Europe/Moscow')
loc_data = moscow_tz.localize(datetime.now())
utc_d = d.astimezone(pytz.utc)
print('utc_d', utc_d)
print(pytz.country_timezones['RU'])
for country in pytz.country_timezones:
    pass
    # print(country)
print(loc_data)
# d_loc =
# print(pytz.common_timezones)