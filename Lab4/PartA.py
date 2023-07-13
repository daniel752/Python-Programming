import datetime

date_today = datetime.date.today()

"""Part 1"""
"""Q1"""


# class for date info
class Date:
    # class constructor
    def __init__(self, day=date_today.day, month=date_today.month, year=date_today.year):
        self.day = day
        self.month = month
        self.year = year

    # class's generic str function to print the date
    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)


# class for temp info
class Temperature(Date):
    # class constructor
    def __init__(self, temp, day=date_today.day, month=date_today.month, year=date_today.year):
        self.temp = temp
        self.date = Date(day, month, year)

    # class's generic str function to print temperature and date
    def __str__(self):
        if self.temp > 0:
            return "+{}°C:{}".format(self.temp / 1, self.date)
        else:
            return "{}°C:{}".format(self.temp / 1, self.date)

    # comparing two object's temperature values and returning the highest
    def compareTemp(self, other):
        if self.temp > other.temp:
            return self
        else:
            return other


# class for location info
class Location(Temperature):

    # class's constructor
    def __init__(self, name):
        self.name = name
        self.temp_list = []

    # adding temperature object to the location temperature list
    def addTemp(self, *temp_list):
        for x in temp_list:
            self.temp_list.append(x)

    # printing location's temperature data (temperature values with date)
    def printLocation(self):
        print(self.name)  # printing location's name
        for x in self.temp_list:
            print(x, end=" ")
        print()

    # getting location's temp average from temp list
    def getAverage(self):
        avg = 0
        for x in self.temp_list:
            avg += x.temp  # adding to the sum temp value
        return avg / len(self.temp_list)  # getting average by dividing the sum with the length of temp_list

    # getting max temp value from temp_list and returning the relevant object
    def getMaxTemp(self):
        max_temp = -1000  # var to hold the max temp value
        i = Temperature(0)  # new temperature object to hold the relevant object
        for x in self.temp_list:
            if max_temp < x.temp:
                max_temp = x.temp  # max_temp equals to the higher temp value
                i = x  # getting the relevant object by value
        return i  # returning the relevant object

    # comparing two location's temperature average and returning the highest
    def compareLocation(self, other):
        if self.getAverage() > other.getAverage():
            return self
        else:
            return other


"""
d1 = Date(1, 2, 2020)
d2 = Date()
print(d1, '-', d2)
t1 = Temperature(-12, 1, 2, 2020)
t2 = Temperature(0)
t3 = Temperature(32, 20, 8, 2020)
print(t1, ',', t2, ',', t3)
print(t1.compareTemp(t3))
loc1 = Location('London')
loc1.printLocation()
loc1.addTemp(Temperature(9), Temperature(7, 1, 12, 2020), Temperature(23, 21, 8, 2020), Temperature(16, 4, 5, 2020))
loc1.printLocation()
print(loc1.getAverage())
print(loc1.getMaxTemp())
loc2 = Location('Berlin')
loc2.addTemp(Temperature(6), Temperature(28, 12, 8, 2020), Temperature(3, 1, 12, 2020), Temperature(-3, 2, 1, 2020))
loc2.printLocation()
loc2.getAverage()
loc2.compareLocation(loc1).printLocation()
"""
"""Q2"""


def make_class(attrs, base_class=None):
    def get_value(name):
        if name in attrs:
            return attrs[name]
        elif base_class is not None:
            return base_class['get'](name)

    def set_value(name, value):
        if name in attrs:
            attrs[name] = value

    def new(*args):
        attrs = {}

        def get_value(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        def set_value(name, value):
            attrs[name] = value

        obj = {'get': get_value, 'set': set_value}
        init = get_value('__init__')
        if init: init(*args)
        return obj

    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls


def make_date_class():
    def __init__(self, day=date_today.day, month=date_today.month, year=date_today.year):
        self['set']('day', day)
        self['set']('month', month)
        self['set']('year', year)

    def str(self):
        return "{:02}/{:02}/{:02}".format(int(self['get']('day')), int(self['get']('month')), int(self['get']('year')))

    return make_class(locals())


def make_temperature_class():
    def __init__(self, temp, day=date_today.day, month=date_today.month, year=date_today.year):
        self['set']('temp', temp)
        date = make_date_class()['new'](day, month, year)
        self['set']('date', date)

    def str(self):
        temp_str = ''
        if float(self['get']('temp')) > 0:
            temp_str = '+'
        temp_str += '{:.1f}°C:'.format(self['get']('temp'))
        return temp_str + self['get']('date')['get']('str')()

    def compareTemp(self, other):
        if self['get']('temp') > other['get']('temp'):
            return self
        else:
            return other

    return make_class(locals())


def make_location_class():
    def __init__(self, name):
        self['set']('name', name)
        self['set']('temp_list', [])

    def addTemp(self, *temp):
        i = []
        for x in temp:
            i += [x]
        self['set']('temp_list', i)

    def printLocation(self):
        print(self['get']('name'))
        if self['get']('temp_list'):
            for x in self['get']('temp_list'):
                print(x['get']('str')(), end=" ")
            print()
        else:
            print('no temperature measurements available')

    def getAverage(self):
        avg = 0
        for x in self['get']('temp_list'):
            avg += x['get']('temp')
        return avg / len(self['get']('temp_list'))

    def getMaxTemp(self):
        max_temp = -1000
        i = make_temperature_class()['new'](0)
        for x in self['get']('temp_list'):
            if max_temp < x['get']('temp'):
                max_temp = x['get']('temp')
                i = x
        return i

    def compareLocation(self, other):
        if self['get']('getAverage')() > other['get']('getAverage')():
            return self
        else:
            return other

    return make_class(locals())


"""
Date = make_date_class()
Temperature = make_temperature_class()
Location = make_location_class()

d1 = Date['new'](1, 2, 2020)
d2 = Date['new']()
print(d1['get']('str')(), '-', d2['get']('str')())
t1 = Temperature['new'](-12, 1, 2, 2020)
t2 = Temperature['new'](0)
t3 = Temperature['new'](32, 20, 8, 2020)
print(t1['get']('str')(), ',', t2['get']('str')(), ',', t3['get']('str')())
print(t1['get']('compareTemp')(t3)['get']('str')())
loc1 = Location['new']('London')
loc1['get']('printLocation')()
loc1['get']('addTemp')(Temperature['new'](9), Temperature['new'](7, 1, 12, 2020), Temperature['new'](23, 21, 8, 2020),Temperature['new'](16, 4, 5, 2020))
loc1['get']('printLocation')()
loc1['get']('getAverage')()
print(loc1['get']('getMaxTemp')()['get']('str')())
loc2 = Location['new']('Berlin')
loc2['get']('addTemp')(Temperature['new'](6), Temperature['new'](28, 12, 8, 2020), Temperature['new'](3, 1, 12, 2020),
                       Temperature['new'](-3, 2, 1, 2020))
loc2['get']('printLocation')()
loc2['get']('getAverage')()
loc2['get']('compareLocation')(loc1)['get']('printLocation')()
"""

"""Q3"""


def make_class(class_name, attrs, base_class=None):
    def get_value(name):
        if name == 'name':
            return class_name
        elif name in attrs:
            return attrs[name]
        elif base_class is not None:
            return base_class['get'](name)

    def set_value(name, value):
        if name in attrs:
            attrs[name] = value

    def new(*args):
        attrs = {}

        def get_value(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        def set_value(name, value):
            attrs[name] = value

        obj = {'get': get_value, 'set': set_value}
        init = get_value('__init__')
        if init: init(*args)
        return obj

    def class_path():
        if base_class:
            path = str(base_class['class_path']())
            path += "::"
            path += class_name
            return path
        return class_name

    cls = {'get': get_value, 'set': set_value, 'new': new, 'class_path': class_path}
    return cls


def make_account_class():
    return make_class('Account', {'interest': 0.05})


def make_save_account_class():
    def init(self, owner):
        self['set']('owner', owner)
        self['set']('balance', 0)

    return make_class('SaveAccount', {'__init__': init, 'interest': 0.03}, Account)


""""
Account = make_account_class()
SaveAccount = make_save_account_class()
print(Account['get']('name'))
print(SaveAccount['get']('name'))
print(Account['class_path']())
print(SaveAccount['class_path']())
"""

"""Part 2"""
"""Q4"""

# from fractions import gcd
from math import atan2, sin, cos, pi,gcd
const_num = 10


class Rational(object):
    """A rational number represented as a numerator and denominator.

    All rational numbers are represented in lowest terms"""

    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)


class ComplexRI(object):
    """A rectangular representation of a complex number"""

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return 'ComplexRI({0}, {1})'.format(self.real, self.imag)


class ComplexMA(object):
    """A polar representation of a complex number."""

    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA({0}, {1})'.format(self.magnitude, self.angle)


class Exponential(object):

    def __init__(self, base, expo):
        self.base = base
        self.expo = expo

    def __repr__(self):
        return 'Exponential ({0},{1})'.format(self.base, self.expo)


def add_complex(z1, z2):
    """Return a complex number z1 + z2"""
    return ComplexRI(z1.real + z2.real, z1.imag + z2.imag)


def mul_complex(z1, z2):
    """Return a complex number z1 * z2"""
    return ComplexMA(z1.magnitude * z2.magnitude, z1.angle + z2.angle)


def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = x.numer, x.denom
    ny, dy = y.numer, y.denom
    return Rational(nx * dy + ny * dx, dx * dy)


def mul_rational(x, y):
    """Multiply rational numbers x and y."""
    return Rational(x.numer * y.numer, x.denom * y.denom)


def add_exponential(x, y):
    if x.expo != y.expo:
        num = x.base*(const_num**(x.expo-y.expo)) + y.base
        return Exponential(num,y.expo)
    return Exponential(x.base + y.base, x.expo)


def mul_exponential(x, y):
    return Exponential(x.base*y.base,x.expo+y.expo)


def is_complex(z):
    return type(z) in (ComplexRI, ComplexMA)


def is_rational(z):
    return type(z) == Rational


def is_exponential(z):
    return type(z) == Exponential


def type_tag(x):
    """Return the tag associated with the type of x."""
    return type_tag.tags[type(x)]


type_tag.tags = {ComplexRI: 'com', ComplexMA: 'com', Rational: 'rat', Exponential: 'exp'}


def add(z1, z2):
    """Add z1 and z2, which may be complex or rational"""
    types = (type_tag(z1), type_tag(z2))
    return add.implementations[types](z1, z2)


def add_complex_and_rational(c, r):
    if c.real:
        return ComplexRI(c.real + r.numer / r.denom, c.imag)
    else:
        return ComplexMA(c.real * r.denom + r.numer, atan2(c.imag, c.real))

add_rational_and_complex = lambda r, c: add_complex_and_rational(c, r)


def add_complex_and_exponential(c, e):
    return ComplexRI(e.base*(const_num**e.expo) + c.real,c.imag)

add_exponential_and_complex = lambda e, c: add_complex_and_exponential(c, e)


def add_rational_and_exponential(r, e):
    return Exponential(e.base + (r.numer/r.denom)*const_num**(-e.expo),e.expo)

add_exponential_and_rational = lambda r, e: add_rational_and_exponential(e, r)


def mul_complex_and_rational(c, r):
    return ComplexMA(c.magnitude * r.numer / r.denom, c.angle)

mul_rational_and_complex = lambda r, c: mul_complex_and_rational(c, r)


def mul_complex_and_exponential(c, e):
    return ComplexMA(c.magnitude * e.base*(const_num**e.expo),c.angle)

mul_exponential_and_complex = lambda e, c: mul_complex_and_exponential(c, e)


def mul_rational_and_exponential(r, e):
    return Exponential(e.base*(r.numer/r.denom),e.expo)

mul_exponential_and_rational = lambda e, r: mul_rational_and_exponential(r, e)


def apply(operator_name,x,y):
    tags = (type_tag(x),type_tag(y))
    key = (operator_name,tags)
    return apply.implementations[key](x,y)


apply.implementations ={
    ('mul',('com','com')): mul_complex,
    ('mul',('com','rat')): mul_complex_and_rational,
    ('mul',('rat','com')): mul_rational_and_complex,
    ('mul',('com','exp')): mul_complex_and_exponential,
    ('mul',('exp','com')): mul_exponential_and_complex,
    ('mul',('rat','exp')): mul_rational_and_exponential,
    ('mul',('exp','rat')): mul_exponential_and_rational,
    ('mul',('rat','rat')): mul_rational,
    ('mul',('exp','exp')): mul_exponential,
    ('add',('com','com')): add_complex,
    ('add',('com','rat')): add_complex_and_rational,
    ('add',('rat','com')): add_rational_and_complex,
    ('add',('com','exp')): add_complex_and_exponential,
    ('add',('exp','com')): add_exponential_and_complex,
    ('add',('rat','exp')): add_rational_and_exponential,
    ('add',('exp','rat')): add_exponential_and_rational,
    ('add',('rat','rat')): add_rational,
    ('add',('exp','exp')): add_exponential
}


def rational_to_complex(x):
    return ComplexRI(x.numer / x.denom, 0)

def exponential_to_complex(x):
    return ComplexRI(x.base*(const_num**x.expo),0)

"""
apply('add', Exponential(2,3), Rational(7,2))
apply('add', Exponential(2,-4), ComplexRI(3,4))
apply('add', Exponential(2,-4), Exponential(3,-5))
apply('mul', Exponential(2,-4), Exponential(3,-5))
apply('mul', Exponential(2,-4), ComplexMA(10,1))
apply('mul', Exponential(2,-4), Rational(1,3))
"""


"""Q5"""
coercions = {('rat', 'com'): rational_to_complex,
             ('exp','com'): exponential_to_complex}


def coerce_apply(operator_name, x, y):

    tx, ty = type_tag(x), type_tag(y)
    if tx != 'com':
        if tx == 'rat':
            x = ComplexRI(x.numer/x.denom,0)
            tx = 'com'
        else:
            x = ComplexRI(x.base*(const_num**x.expo),0)
            tx = 'com'
    if ty != 'com':
        if ty == 'rat':
            y = ComplexRI(y.numer/y.denom,0)
            ty = 'com'
        else:
            y = ComplexRI(y.base*(const_num**y.expo),0)
            ty = 'com'
    if tx != ty:
        if (tx, ty) in coercions:
            tx, x = ty, coercions[(tx, ty)](x)
        elif (ty, tx) in coercions:
            ty, y = tx, coercions[(ty, tx)](y)
        else:
            return 'No coercion possible.'
    key = (operator_name, tx)
    return coerce_apply.implementations[key](x, y)


coerce_apply.implementations = {('mul', 'com'): mul_complex,
                                ('mul', 'rat'): mul_rational,
                                ('mul','exp'): mul_exponential,
                                ('add', 'com'): add_complex,
                                ('add', 'rat'): add_rational,
                                ('add','exp'): add_exponential}

"""
print(coerce_apply('add', Exponential(2,-4), Rational(3,4)))
print(coerce_apply('add', Exponential(2,-4), ComplexRI(3,4)))
print(coerce_apply('add', Exponential(2,-4), Exponential(3,-5)))
print(coerce_apply('mul', Exponential(2,-4), Exponential(3,-5)))
print(coerce_apply('mul', Exponential(2,-4), ComplexMA(10,1)))
print(coerce_apply('mul', Exponential(2,-4), ComplexRI(3,4)))
print(coerce_apply('mul', Exponential(2,-4), Rational(1,3)))
"""


"""Part 3"""
"""Q6"""


def make_sequence(sequence = None):

    try:
        x = sequence[0]
    except TypeError as e:
        print(type(e),end=" no sequence argument")
        print()

    """func to return filtered tuple"""
    def Filter(bool_func = None):

        try:
            return tuple(filter(bool_func, sequence))
        except ValueError as e:
            print(type(e),end=" no filter function")
            print()
            return tuple(sequence)


    """func to traverse in sequence using 'next' and 'reverse' commands"""
    def filter_iterator(bool_func = None):

        try:
            bool_func()
        except TypeError as e:
            print(type(e), end=" no filter function")
            print()

        iter_seq = tuple(filter(bool_func, sequence))
        index = 0

        """func to return the next iterator in sequence"""
        def next_iter():
            nonlocal index
            try:
                res = iter_seq[index]
                index = (index + 1) % len(sequence)
            except IndexError as e:
                print(type(e), end=" tuple index out of range")
                print()
                return
            return res

        """func to return previous iterator in sequence"""
        def prev_iter():
            nonlocal index
            try:
                res = iter_seq[index]
                index = (index - 1) % len(sequence)
            except IndexError as e:
                print(type(e), end=" tuple index out of range")
                print()
                return
            return res

        """return next/reverse iterator based on syntax"""
        return {'next': next_iter, 'reverse': prev_iter}

    """func to return the sequence in reverse"""
    def reverse():
        return sequence[::-1]

    """func to combine the current sequence with the new sequence"""
    def extend(seq):
        nonlocal sequence
        sequence += seq

    """returning the func to use based on syntax"""
    return {'filter': Filter, 'filter_iterator': filter_iterator, 'reverse': reverse, 'extend': extend}


s1=make_sequence()
s1=make_sequence(200)
s1=make_sequence((1,2,3,4,5))
s1['filter']()
p1=s1['filter_iterator']()
p1=s1['filter_iterator'](lambda x: x<4)
for _ in range(6):
    p1['next']()
p1=s1['filter_iterator'](lambda x: x>1)
p1['next']()
p1['next']()
p1['next']()
for _ in range(6):
    p1['reverse']()


class Tree():

    def __init__(self, value, nodes=None):
        self.value = value
        self.nodes = nodes

    def __repr__(self):
        if self.nodes:
            return 'Tree({0},{1})'.format(self.value,repr(self.nodes))
        return 'Tree({0})'.format(self.value)




"""Part 5"""
"""Q8"""

"""Calculator

An interpreter for a calculator language using prefix-order call syntax.
Operator expressions must be simple operator names or symbols.  Operand
expressions are separated by commas.

Examples:
    calc> mul(1, 2, 3)
    6
    calc> add()
    0
    calc> add(2, div(4, 8))
    2.5
    calc> add
    SyntaxError: expected ( after add
    calc> div(5)
    TypeError: div requires exactly 2 arguments
    calc> div(1, 0)
    ZeroDivisionError: division by zero
    calc> ^DCalculation completed.
"""


from functools import reduce
from operator import mul

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return


# Eval & Apply

class Exp(object):
    """A call expression in Calculator.

    >>> Exp('add', [1, 2])
    Exp('add', [1, 2])
    >>> str(Exp('add', [1, Exp('mul', [2, 3])]))
    'add(1, mul(2, 3))'
    """

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)


def calc_eval(exp):
    """Evaluate a Calculator expression.

    >>> calc_eval(Exp('add', [2, Exp('mul', [4, 6])]))
    26
    """
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


def calc_apply(operator, args):
    """Apply the named operator to a list of args.

    >>> calc_apply('+', [1, 2, 3])
    6
    >>> calc_apply('-', [10, 1, 2, 3])
    4
    >>> calc_apply('*', [])
    1
    >>> calc_apply('/', [40, 5])
    8.0
    >>> calc_apply('!', [1564])
    8435
    """
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer / denom
    if operator in ('compl', '!'):
        if len(args) != 1:
            raise TypeError(operator + ' requires exactly 1 argument')
        if type(args[0]) == int:
            return int(''.join((map(lambda x:  str(9 - int(x)), list(str(args[0]))))))
        raise TypeError(str(args[0]) + ' is not <class int>')



# Parsing

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree


def tokenize(line):
    """Convert a string into a list of tokens.

    >>> tokenize('add(2, mul(4, 6))')
    ['add', '(', '2', ',', 'mul', '(', '4', ',', '6', ')', ')']
    """
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.strip().split()


known_operators = ['add', 'sub', 'mul', 'div','compl', '+', '-', '*', '/', '!']


def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens.

    Operand expressions can be separated by commas, spaces, or both.

    >>> analyze(tokenize('add(2, mul(4, 6))'))
    Exp('add', [2, Exp('mul', [4, 6])])
    >>> analyze(tokenize('mul(add(2, mul(4, 6)), add(3, 5))'))
    Exp('mul', [Exp('add', [2, Exp('mul', [4, 6])]), Exp('add', [3, 5])])
    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    str_token = str(token)
    index = len(str_token) - 1
    if type(token) in (int, float):
        return token
    elif token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    elif str_token[index] == 'b' or 'q' or 'h':
        if str_token[index] == 'b':
            str_token = int(str_token[:index:], 2)
            return str_token
        elif str_token[index] == 'q':
            str_token = int(str_token[:index:], 8)
            return str_token
        elif str_token[index] == 'h':
            str_token = int(str_token[:index:], 16)
            return str_token
    else:
        raise SyntaxError('unexpected ' + token)


def analyze_operands(tokens):
    """Analyze a sequence of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands


def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')


def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token.

    >>> analyze_token('12')
    12
    >>> analyze_token('7.5')
    7.5
    >>> analyze_token('add')
    'add'
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


def run():
    read_eval_print_loop()


run()
