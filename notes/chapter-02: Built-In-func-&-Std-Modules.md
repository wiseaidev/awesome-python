<!-- MIT License

Copyright (c) 2022, Harmouch101
All rights reserved.
 -->


# Chapter_02: Built-in functions & Standard Modules.

Copyright (c) 2022 Mahmoud Harmouch

---

## **Quotes**.

> “It’s better to be individual than a clone of someone else.” ― Fennel Hudson

> “You are amazing person with unique talents. Have faith in your abilities.” ― Lailah Gifty Akita

> “You can be all that you want to be. Keep dreaming and reach out to your dreams.” ― Lailah Gifty Akita

> “Be yourself....and make the world adjust!” ― Germany Kent

---

## Table Of Content (TOC) <a name="TOC"></a>

1. [Functions](#1)   
	1.1	[Function's Arguments](#1.1)   
	1.2	[Functional Programming](#1.2)   
	&nbsp;&nbsp;&nbsp;&nbsp;1.2.1 [Anonymous Functions](#1.2.1)   
	&nbsp;&nbsp;&nbsp;&nbsp;1.2.2 [Map](#1.2.2)   
	&nbsp;&nbsp;&nbsp;&nbsp;1.2.3 [Filter](#1.2.3)   
	&nbsp;&nbsp;&nbsp;&nbsp;1.2.4 [Reduce](#1.2.4)   
	&nbsp;&nbsp;&nbsp;&nbsp;1.2.5 [Zip](#1.2.5)   
	1.3 [Other Builtin Functions](#1.3)   
2. [File I/O](#2)
3. [Standard Modules](#3)

## 1. Functions. <a name="1"></a>

A function is an object Like any other thing in python. It takes arguments(parameters) and has the ability to return data. It is defined using the `def` keyword.

```python
def function_name(parameters,...):
	# internal variables and statements
	return some_operation(parameters)

>>> def mul(a,b):
...     return a * b
...
```

The `return` statement returns an object which value is, in our case, the result of multiplication of a and b. 

**Function call**

```python
>>> a = 10
>>> b = 12.13
>>> callable(mul)
True
>>> type(mul)  # so mul is an istance of the 'function' class.
<class 'function'>
>>> c = mul(a,b)
>>> c
121.30000000000001  # See chapter_01 to know why the output looks like that.
>>> c = mul("string",3)
>>> c
'stringstringstring'
```

A function can be nested and return any data types (tuples, lists, sets, functions):

```python
>>> def outer_function(a,b):
...     x = a * b
...     def inner_function(y):
...         return y + x
...     return inner_function
... 
>>> c = outer_function(100,3) # returns a function
>>> c(33)
333
```

If there isn't any return value, the returned data will be a `None` object(void function):

```python
>>> def do_nothing():
...     pass
... 
>>> do_nothing()
>>> print(do_nothing())
None
```

### 1.1. Function's Arguments. <a name="1.1"></a>

A function can take any number of parameters.

```python
>>> def mul(a, b, c=5): # Default parameter value.
...     return a * b *c
... 
>>> mul(2,3)
30
>>> mul(a = 2, b = 3)
30
>>> mul(a = 2, b = 3, c = 2)
12
>>> mul(a = 2, c = 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: mul() missing 1 required positional argument: 'b'
```

A function can also take a variable number of arguments if an asterisk `*` is placed before the name of the function:

```python
>>> def add(a,*b):
...     return a + sum(num for num in b)
... 
>>> add(1,2,3,4,5,6,7)
28
>>> def do_nothing(*args):
...     return args
... 
>>> do_nothing()
()
>>> do_nothing(1)
(1,)
>>> type(do_nothing())
<class 'tuple'>
```

So as you can see, `args` is a tuple object.

```python
>>> def do_nothing(**kwargs):
...     return kwargs
... 
>>> do_nothing()
{}
>>> type(do_nothing())
<class 'dict'>
>>> do_nothing(a = '1')
{'a': '1'}
```

So `kargs` is a dictionary object.

## 1.2. Functional Programming. <a name="1.2"></a>

Functional Programming is a often used to describe a piece of code that has no effects on other pieces(immutable data). A functional function is a function that does not change the value of data outside it(no shared variables). 

```python
# Non functional function:
a = 1
def add(b):
	global a 
	a = a + b
	return a 

# functional function:	
def add(a,b):
	return a + b
```

When talking about the elements of functional programming in Python, the following functions are meant: lambda , map , filter , reduce , zip .

### 1.2.1 Anonymous Functions. <a name="1.2.1"></a>

An anonymous function, also called lambda function, is a function that doesn't have a name and it is defined using the keyword `lambda`.

**Syntax**

> lambda arguments: expression

> returns a lambda object(iterable)

```python
>>> f = lambda x : x ** 3 + x ** 2 - x + 1
>>> f(1)
2
```

**Why does lambda function exist?**

The lambda function is best used as a nested function.

```python
>>> def add_mul(a,b):
...     return lambda c: (a + b)*c
... 
>>> add_mul(1,3)
<function add_mul.<locals>.<lambda> at 0x7f9a36d94170>
>>> add = add_mul(1,3)
>>> add(3)
12

# without the use of lambda function, the previous function will be written like:

>>> def add_mul(a,b):
...     def mul(c):
...         return (a+b)*c
...     return mul
... 
>>> add_mul(1,3)
<function add_mul.<locals>.mul at 0x7f9a36da1200>
>>> add = add_mul(1,3)
>>> add(3)
12
```

So as you can tell, it is preferable to use a lambda function when the anonymous function is needed once in a certain part of the code, but not in all the places of the code.

**Is it faster than a regular function?**

```python
# Lambda Function
>>> sum1 = lambda n : sum(n for n in range(n+1))
# regular function
>>> def sum2(n):
...     return sum(n for n in range(n+1))
... 
>>> import timeit
>>> timeit.timeit("sum1(100)", "from __main__ import sum1",number = 100000)
0.8884602810003344
>>> timeit.timeit("sum2(100)", "from __main__ import sum2",number = 100000)
0.8455167720003374
```

As you can notice, the normal function is slightly faster than the lambda function.

**lambda functions can be nested**

```python
>>> a = lambda a, b : lambda c: (a + b) * c
>>> c = a(1,2)
>>> c
<function <lambda>.<locals>.<lambda> at 0x7f2779d50710>
>>> c(2)
6
```

**Converting a normal function to lambda**

It is easy to rewrite a given function into a lambda form. All you need is to do is to replace the 'def func_name' with the `lambda` keyword, declare parameters after lambda, and continue the logic of the program after ':'.

```python

def mul(a,b):
	return a + b

lambda a,b : a + b
```

### 1.2.2 Map. <a name="1.2.2"></a>

`map()` is a built-in function that accepts a **function** and a **sequence**(dataset) as arguments. It works by applying the passed function to each element. Map can replace a loop.

**Syntax**

> map(function, sequence)

> returns an object map(iterable)

```python
>>> list_ = ['first', 'second',123]
>>> map(id,list_) # the function is id and the sequence is list_(id for each element).
<map object at 0x7fc6d395b790>
>>> list(map(id,list_))  
[140491930055984, 140491930056112, 94057408700992]
```

**Map with lambda**

```python
>>> list_ = [2,4,5,7]
>>> list(map(lambda x: x**2,list_)) # it is more convenient to use lambda and not a normal function ! 
[4, 16, 25, 49]
>>> list2 = []
>>> for e in list_:
...     list2.append(e**2)
... 
>>> list2
[4, 16, 25, 49]
>>> timeit.timeit("list2 = list(map(lambda x: x**2,list_))","from __main__ import list_",number=100000)
0.24455913900055748  # when you convert it to list,it becomes slower
>>> timeit.timeit("map(lambda x: x**2,list_)","from __main__ import list_",number=100000)
0.02997873599997547  # faster than a loop
>>> timeit.timeit("for e in list_: list2.append(e**2)","from __main__ import list_,list2",number=100000)
0.18769715700000233
```

### 1.2.3 Filter. <a name="1.2.3"></a>

`filter()` is a built-in function that filters(selects) items from a sequence of an iterable. Like `map()` function, it takes a **function** and a **sequence** as parameters.

**Syntax**

> filter(function, sequence)

> returns a filter object(iterable).

**Filter with lambda**

```python
>>> list_ = [1,2,3,4,5]
>>> filter(lambda x: x == 2, list_)
<filter object at 0x7fc6d38726d0>
>>> list(filter(lambda x: x == 2, list_)) # it works like a loop with an if statement
[2]
>>> list(filter(lambda x: x % 2 == 0, list_)) # selects even numbers.
[2, 4]
>>> list0 = [1,2,3,4,5]
>>> list1 = [2,4,7,8,9]
>>> inter = list(filter(lambda e: e in list1, list0))
>>> inter
[2, 4]
>>> list(set(list0) & set(list1))
[2, 4]
>>> timeit.timeit("list(set(list0) & set(list1))","from __main__ import list0,list1",number = 100000)
0.1329232750013034
>>> timeit.timeit("list(filter(lambda e: e in list1, list0))","from __main__ import list0,list1",number = 100000)
0.18562702400049602
>>> timeit.timeit("filter(lambda e: e in list1, list0)","from __main__ import list0,list1",number = 100000)
0.03419653799937805
>>> timeit.timeit("set(list0) & set(list1)","from __main__ import list0,list1",number = 100000)
0.10309240099923045
```

**Difference between Map() and Filter()**

The following example will illustrate the main difference between the two.

```python
>>> list(filter(lambda e: e in list1, list0))  # selects(filters) the elements that match the condition: e in list1
[2, 4]
>>> list(map(lambda e: e in list1, list0)) # runs(map) the expression 'e in list1' on list1
[False, True, False, True, False]
>>> list(map(lambda e: e**2, list0)) # squares the numbers in list0
[1, 4, 9, 16, 25]
>>> list(filter(lambda e: e**2, list0)) # does nothing, it returns list0 because e**2 is always True
>>> list(filter(lambda e: True, list0)) 
[1, 2, 3, 4, 5]
>>> list(filter(lambda e: False, list0))
[]
```
  
### 1.2.4 Reduce. <a name="1.2.4"></a>

Visit [Python Docs](https://docs.python.org/3/library/functools.html#functools.reduce) for more information.

`Reduce()` is a built-in function that combines items(e.g. add, mul..) in a sequence of an iterable. Like the previous functions, it takes a **function** and a **sequence** as parameters. But, it returns a single value. 

**Syntax**

> Reduce(function, sequence)

> returns a value of the function on the sequence.

```python
>>> from functools import reduce
>>> def add(a,b):
...     print(f"{a} + {b}")
...     return a + b
... 
>>> reduce(add,[1,2,3,4,5,6])
1 + 2
3 + 3
6 + 4
10 + 5
15 + 6
21
>>> reduce(lambda a,b : a+b,[1,2,3,4,5,6])
21
```

First, the function adds the first two elements of the sequence. Then the result of the function is used with the third element of the sequence to call the function again, and so on.

```python
-----------------------Exercice-------------------------
>>> persons = [{'name': 'Joe', 'weight': 60},
...     {' name ': 'David', 'weight': 70},
...     {' name ': 'Emma', 'weight': 55},
...     {'name': 'Marla'}]
>>> total_weight = 0
>>> count_weight = 0
>>> for person in persons:
...     if 'weight' in person:
...         total_weight += person['weight']
...         count_weight += 1
... 
>>> average_weight = total_weight / count_weight
>>> print("the average weight is {:.2f}".format(average_weight))
the average weight is 61.67

--------------------map filter reduce ------------------
>>> from functools import reduce
>>> weights = map(lambda x: x['weight'], filter(lambda x: 'weight' in x, persons))
>>> average_weight = reduce(lambda a,b: a+b , weights) # the weights variable is consumed here!
>>> average_weight/3
61.666666666666664 
>>> list(weights) # already consumed in average_weight!
[]
```

**Using filter() inside map()**

The elements are first selected by the `filter` function and then the `map` apply the function on these elements.

```python
>>> y = map(lambda x: x * x, filter (lambda x: (x >= 5), (3,4,5,6,7,8,9,10,11)))
>>> list(y)
[25, 36, 49, 64, 81, 100, 121]
>>> list(y)
[]
```

**Using map() inside filter()**

When you use the `map` function inside the `filter` function, the iterations are first handled by the `map` function and then the `filter` condition is applied to them.

```python
>>> y = filter (lambda x: (x >= 5), map (lambda x: x * x, (3,4,5,6,7,8,9,10,11)))
>>> list(y)
[9, 16, 25, 36, 49, 64, 81, 100, 121]
```

**Using filter() and map() inside reduce()**

The internal functions are executed first and then the reduce() function.

```python
>>> d = reduce (lambda x, y: x * y, map (lambda x: x + x, filter (lambda x: (x >= 5), (3,4,5,6,7,8,9,10,11))))
>>> d
212889600
```

### 1.2.5 Zip. <a name="1.2.5"></a>

It Concatenates sequences into tuples.

**Syntax**

> zip(sequence_1, sequence_2)

> returns a tuples list.

```python
>>> list(zip(range(5),range(2,10)))
[(0, 2), (1, 3), (2, 4), (3, 5), (4, 6)]   # stops at the lowest upper band of the two lists(4)
>>> list(zip(range(3,5),range(2,10)))  # think of it as two loops run in parallel.
[(3, 2), (4, 3)]
>>> keys = ['name', 'age', 'job']
>>> values = ['Joe', '22', 'Python Developer']
>>> dict_ = dict(zip(keys,values))
>>> dict_
{'name': 'Joe', 'age': '22', 'job': 'Python Developer'}
```

For more information about functionnal progamming, please refer to [python docs](https://docs.python.org/3.8/howto/functional.html).

## 1.3 Other Builtin Functions. <a name="1.3"></a>

[Python Docs.](https://docs.python.org/3/library/functions.html)

These functions are grouped together in the `__builtins__` module.

```python
>>> dir(__builtins__)
['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 
 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 
 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 
 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 
 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 
 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super',
 'tuple', 'type', 'vars', 'zip']
 73 Functions.
```

**import**

It is used to import a module from a given list.

```python
>>> help(__import__)
__import__(name, globals=None, locals=None, fromlist=(), level=0) -> module
```

The **local** and **global** environment can be passed as a parameter, and fromlist specify the directive. The level is a flag which allows determining if the imports are relative(1,2...n) or absolute( 0).

```python
>>> __import__('math', fromlist=['math.pi'],level=0)
<module 'math' from '/home/.../math.cpython-37m-x86_64-linux-gnu.so'>

# Same as the following.

>>> from math import pi

>>> globals().items()  # the name of the module is stored in the namespace.  
dict_items([('__name__', '__main__'), ('__doc__', None), ('__package__', None), ...
	('math', <module 'math' from '/home/.../math.cpython-37m-x86_64-linux-gnu.so'>), 
	('pi', 3.141592653589793)])
```

**abs**

It returns the absolute value of a given number(reel or complex).

```python
>>> abs(-13)
13
>>> abs(4 + 3j)   # returns sqrt(4**2 + 3**2)
5.0
```

**all**

```python
>>> help(all)
all(iterable, /)
    Return True if bool(x) is True for all values x in the iterable.
    If the iterable is empty, return True.

>>> list_ = [1,'2',3]
>>> all([isinstance(e, int) for e in list_])
False
>>> all([])
True
```

**any**

```python
>>> help(any)
any(iterable, /)
    Return True if bool(x) is True for any x in the iterable.
    
    If the iterable is empty, return False.

>>> list_ = [1,2,3]
>>> any([isinstance(e, int) for e in list_])
True
```

**ascii**

```python
>>> help(ascii)
ascii(obj, /)
    Return an ASCII-only representation of an object.

>>> ascii(0x33)
'51'
>>> type(ascii(0x33))
<class 'str'>
>>> ascii(0x33)[0]
'5'
>>> ascii([1,2,3])
'[1, 2, 3]'
>>> ascii('213a\asd\t')
"'213a\\x07sd\\t'"
>>> ascii('\a\b\t\n\v\f\r')
"'\\x07\\x08\\t\\n\\x0b\\x0c\\r'"
>>> ascii(0x0B)
'11'
>>> str(int('b',16))
'11'
	   from the ascii table $ man ascii
       Oct   Dec   Hex   Char                        Oct   Dec   Hex   Char
       ────────────────────────────────────────────────────────────────────────
 	   007   7     07    BEL '\a' (bell)             107   71    47    G
       010   8     08    BS  '\b' (backspace)        110   72    48    H
       011   9     09    HT  '\t' (horizontal tab)   111   73    49    I
       012   10    0A    LF  '\n' (new line)         112   74    4A    J
       013   11    0B    VT  '\v' (vertical tab)     113   75    4B    K
       014   12    0C    FF  '\f' (form feed)        114   76    4C    L
       015   13    0D    CR  '\r' (carriage ret)     115   77    4D    M
```

**bin**

```python
bin(number, /)
    Return the binary representation of an integer.

>>> bin(8)
'0b1000'
>>> int('0b1000',2)
8
```

**bool**

```python
>>> help(bool)
	Returns True when the argument is true, False otherwise.

>>> bool([])
False
>>> bool(())
False
>>> bool(1)
True
>>> bool("")
False
>>> bool([""])
True
>>> bool((''))
False
>>> bool(('',))
True
```

**breakpoint**

This function was introduced in Python 3.7 which does the job of importing pdb and calling pdb.set_trace().

```python
>>> help(breakpoint)
breakpoint(...)
    breakpoint(*args, **kws)
    
    Call sys.breakpointhook(*args, **kws).  sys.breakpointhook() must accept
    whatever arguments are passed.
    
    By default, this drops you into the pdb debugger.

-------without breakpoint----
# file.py
import pdb
x = 1
y = 2
print ( x ) 
pdb.set_trace()
print ( y )
z = x + y
-------with breakpoint----
# file.py
x = 1
y = 2
print ( x ) 
breakpoint()
print ( y )
z = x + y

$ python3 file.py

-> print ( y )
(Pdb) l  (l stands for list)
  1     x = 1
  2     y = 2
  3     print ( x )
  4     breakpoint()
  5  -> print ( y )
  6     z = x + y
[EOF]
(Pdb) x
1
(Pdb) y
2
(Pdb) z
*** NameError: name 'z' is not defined
(Pdb) n  (n stands for next)
2
-> z = x + y
(Pdb) n
--Return--
-> z = x + y
(Pdb) z
3
(Pdb) n
```

**bytearray**

Construct a **mutable** bytearray object.

```python
bytearray(iterable_of_ints) -> bytearray
>>> bytearray([1,2,3])
bytearray(b'\x01\x02\x03')

bytearray(string, encoding[, errors]) -> bytearray
>>> bytearray("123",'utf-8')
bytearray(b'123')

bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
>>> bytearray(b'123')
bytearray(b'123')

bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
>>> bytearray(2)
bytearray(b'\x00\x00')

bytearray() -> empty bytes array
>>> bytearray()
bytearray(b'')

>>> a = bytearray(b'123')  
>>> a[1] = 3   # mutable
>>> a
bytearray(b'1\x033')
```

**bytes**

Construct an **immutable** array of bytes.

```python
bytes(iterable_of_ints) -> bytes
bytes(string, encoding[, errors]) -> bytes
bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
bytes(int) -> bytes object of size given by the parameter initialized with null bytes
bytes() -> empty bytes object

>>> a =  bytes([1,2,3])
>>> a
b'\x01\x02\x03'
>>> a[1] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment
```

**callable**

Returns True if the passed object is a function or a method.

```python
>>> callable(callable)
True
>>> def func():
...     print("hi there!")
... 
>>> callable(func)
True
>>> string = 'abc'
>>> callable(string)
False
```

**chr**

Returns a string that represents the character whose ASCII code is the integer argument.

```python
>>> help(chr)
chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

>>> chr(65)
'A'
>>> chr(50 + 15)
'A'
>>> ord('A')
65
```

** classmethod**

Converts a function to a class method. A class method is a method which is associated with a class and not with its instances.

```python
>>> class car:
...      def __init__(self, speed, model):
...          self.speed = speed
...          self.model = model
...      def run(cls, speed, model):
...          return cls( speed, model)
...      def print(self):
...          print(self.model + "'s speed is: " + str(self.speed))
...      run = classmethod(run)
... 
>>> car0 = car(50,'mercedes')
>>> car0.print()
mercedes's speed is: 50
>>> car1 = car.run(60,'bmw')
>>> car1.print()
bmw's speed is: 60
```

You can use the `classmethod` as a decorator.

```python
>>> class car:
...      def __init__(self, speed, model):
...          self.speed = speed
...          self.model = model
...      @classmethod
...      def run(cls, speed, model):
...          return cls( speed, model)
```

**compile**

Python allows source code to be compiled on the fly. The result of this compilation can then be interpreted using the exec() or eval() methods.

```python
>>> help(compile)
compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
    Compile source into a code object that can be executed by exec() or eval().
The mode must be 'exec' to compile a module, 'single' to compile a
    single (interactive) statement, or 'eval' to compile an expression.
>>> bytes_ = compile("print('Hi There!')", '/dev/null','eval')
>>> exec(bytes_)
Hi There!
```

**complex**

Returns a complex number.

```python
>>> help(complex)
class complex(object)
   complex(real=0, imag=0)
>>> complex(3,4)
(3+4j)
```

**credits**, **copyright**

```python
>>> credits()
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
>>> copyright()
Copyright (c) 2001-2019 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
```

**delattr**

Removes an attribute from an object. Equivalent to del object.attribute_name.

```python
>>> class car:
...     speed = 10
... 
>>> car.speed
10
>>> delattr(car,'speed')
>>> car.speed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'car' has no attribute 'speed'
>>> class car:
...     speed = 10
... 
>>> del car.speed
>>> car.speed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'car' has no attribute 'speed'
```

**dict**

Creates a dictionary object.

```python
>>> dict([('key0','val0'),('key1','val1')])
{'key0': 'val0', 'key1': 'val1'}
```

**dir**

Returns a list of the object's attributes.

```python
>>> dir() # attributes of the namespace
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'byte_code', 'bytes_', 'car']
>>> class car:
...     speed = 10
...     model = 'mercedes'
... 
>>> dir(car)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'model', 'speed']
>>> car. # using the <tab> key
car.model car.speed
```

**divmod**

Returns the tuple: ((a-a% b) / b, a% b) which is an integer division followed by modulo.

```python
>>> divmod(10,3)
(3, 1)
>>> divmod(1,3)
(0, 1)
```

**enumerate**

Returns an object of type enumerate from an iterable(e.g. lists or tuples).

```python
>>> enumerate(range(10))
<enumerate object at 0x7fd271b73f00>
>>> for index, element in enumerate([1, 2, 3]):
...     print(index, element)   
... 
0 1
1 2
2 3
```

**eval**

```python
>>> help(eval)

eval(source, globals=None, locals=None, /)
    Evaluate the given source in the context of globals and locals.
    
    The source may be a string representing a Python expression
    or a code object as returned by compile().

>>> eval('1+2')
3
>>> eval('a+2', {'a': 1})
3
>>> eval('f"a equal to {a}"', {'a': 1+2})
'a equal to 3'
```

**exec**

Executes a python script.

```python
>>> exec('a = 2; print(a)')
2
>>> exec('f"a equal to {a}"', {'a': 1+2}) # returns nothing
```

If you want to see the difference between eval, exec, and compile, you can refer to the following answer @[stackoverflow](https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile), or you can read [python docs](https://docs.python.org/3.7/library/functions.html#eval) for more details about these functions.

**exit**

```python
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
```

[**filter**](#1.2.3)

**float**, **format**, **frozenset**

Explained in *chapter_01*.

**getattr**

Returns the attribute's value of an object. Same as object.attr_name.

```python
>>> class car:
...     speed = 50
... 
>>> getattr(car,'speed')
50
>>> car.speed
50
>>> getattr(car,'speed1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'car' has no attribute 'speed1'
>>> getattr(car,'speed1','attr not found!')
'attr not found!'
```

**globals**

Returns a dictionary containing all the global variables of the namespace.

```python
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class 
'_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, 
'__builtins__': <module 'builtins' (built-in)>, 'car': <class '__main__.car'>}
>>> x = 16
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class 
'_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, 
'__builtins__': <module 'builtins' (built-in)>, 'car': <class '__main__.car'>, 'x': 16}

```

**hasattr**


Returns True if the object has the given attribute's name.

```python
>>> hasattr(car, 'speed')
True
```

**hash**

Returns a unique hash of an object.

```python
>>> x = 'string'
>>> y = 'string'
>>> hash(x)
5126848504124768093
>>> hash(y)
5126848504124768093
>>> hash(123)
123
>>> hash(True)
1
>>> hash('0')
3652700342679621854
>>> hash('1')
-1863168594792410958
>>> hash('')
0
>>> hash('2')
-8901682508772374836
>>> hash('3')
4439948147711810720
>>> hash('4')
-6245016655141321378
```

**help**

```python
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> hash

Help on built-in function hash in module builtins:

hash(obj, /)
    Return the hash value for the given object.
    
    Two objects that compare equal must also have the same hash value, but the
    reverse is not necessarily true.
```

**hex**

Returns a string representing the hexadecimal form of an integer.

```python
>>> hex(16)
'0x10'
```

**id**

Returns a unique identifier of an object. When two objects of immutable type have the same value, the interpreter can decide to keep only one object in memory.

```python
>>> string0 = 'abc'
>>> string1 = 'abc'
>>> id(string0), id(string1)
(139658273441008, 139658273441008)
```

**input**

Executes a user-supplied expression.

```python
>>> x = input()
1
>>> x
'1'
>>> y = eval(input("Enter your number: ")) # same as int(input("Enter your number: ")
Enter your number: 1
>>> y
1
```

**int**

Converts a string or number to an integer of a given base.

```python
>>> int('20',16)
32
>>> int('20',10)
20
>>> int('20')  # by default base = 10
20
```

**isinstance**

Tests whether an object is of a given type or an instance of a class.

```python
>>> isinstance(10, int)
True
>>> isinstance('string', str)
True
```

**issubclass**

Checks if a given class derives from another class.

```python
>>> class x:
...     pass
... 
>>> class y(x):
...     pass
... 
>>> issubclass(y,x)
True
>>> issubclass(x,y)
False
```

**iter**

Returns an iterator from a given object.

```python
>>> it = iter([1, 2, 3])
>>> it
<list_iterator object at 0x7f04b98f0fd0>
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

>>> x = 0
>>> def iterator():
...     global x
...     x += 1
...     return x
... 
>>> it = iter(iterator,5)
>>> it
<callable_iterator object at 0x7f04b98f0fd0>
>>> next(it)
2
>>> next(it)
3
>>> next(it)
4
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

**len**

Returns the number of elements in a given sequence.

```python
>>> dict = {'key0': 'val0', 'key1': 'val1'}
>>> len(dict)
2
>>> string = "abc"
>>> len(string)
3
```

**license**

Displays the license information and the history of Python versions.

```python
A. HISTORY OF THE SOFTWARE
==========================

Python was created in the early 1990s by Guido van Rossum at Stichting
Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
as a successor of a language called ABC.  Guido remains Python's
principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for
National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
in Reston, Virginia where he released several versions of the
software.

In May 2000, Guido and the Python core development team moved to
BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
year, the PythonLabs team moved to Digital Creations, which became
Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
https://www.python.org/psf/) was formed, a non-profit organization
created specifically to own Python-related Intellectual Property.
Zope Corporation was a sponsoring member of the PSF.

All Python releases are Open Source (see http://www.opensource.org for
the Open Source Definition).  Historically, most, but not all, Python
Hit Return for more, or q (and Return) to quit: 
```

**list**

Generates a new list object. `list_ = list ()` is equivalent to `list_ = []`.

```python
>>> list()
[]
>>> list({'key0':'val0'})
['key0']
>>> list(('a','b'))
['a', 'b']
>>> list(('abc'))
['a', 'b', 'c']
```

**locals**

Returns a dictionary object containing the local variables of the current scope.

```python
>>> def add(a,b):
...     x = a + b
...     print(locals())
... 
>>> add(1,2)
{'a': 1, 'b': 2, 'x': 3}
```

[**map**](#1.2.2)

**max**

Returns the largest element in the sequence. If several sequences are provided, returns the largest one.

```python
>>> max(1,2,3)
3
>>> max([1,2,3])
3
>>> max([1,2,3],[1,2,3,4])
[1, 2, 3, 4]
>>> max([1,2,3],[1,2,3])
[1, 2, 3]
>>> max([1,2,3],[1,3])
[1, 3]
>>> max([1,2,3],[1,2])
[1, 2, 3]
>>> max([1,2,3],[1,5])
[1, 5]
>>> max('abc')
'c'
>>> max('hi', 'Hi')
'hi'
```

**memoryview**

Creates a new memoryview object which references the given object.

```python
>>> a = bytes(b'\a\bsd')
>>> a
b'\x07\x08sd'
>>> memoryview(a)
<memory at 0x7f21c6e08ae0>
>>> memoryview(a)
<memory at 0x7f21c6e08c80>
>>> memoryview(a)
<memory at 0x7f21c6e08ae0>
```

**min**

Returns the lowest value in a given sequence.

```python
>>> min('abcd')
'a'
>>> min(['abcd'])
'abcd'
>>> min(1,2,4)
1
>>> min(1, 2)
1
>>> min([1, 2], [1])
[1]
>>> min([1, 3], [1, 2])
[1, 2]
>>> min([3, 1], [1, 2])
[1, 2]
>>> min([1, 1], [1, 2])
[1, 1]
>>> min([1, 1], [2, 1])
[1, 1]
```

**next**

Returns the next element of an iterable.

```python
>>> it = iter([1,2,3,4,5])
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
```

**object**

Creates an object without any features.

```python
>>> a = object()
>>> a
<object object at 0x7f21c71d8d60>
>>> object() == object()
False
>>> object() is object()
False
```

**oct**

Returns an octal representation of an integer.

```python
>>> oct(8)
'0o10'
```

**open**

Returns a file object.

```python
>>> f = open('replay_pid4677.log')
>>> f
<_io.TextIOWrapper name='replay_pid4677.log' mode='r' encoding='UTF-8'>
>>> f.readline()
'JvmtiExport can_access_local_variables 0\n'
```
**ord**

Returns an integer Unicode code value of a character.

```python
>>> ord('a')
97
>>> list(map(ord,'asdqwr'))
[97, 115, 100, 113, 119, 114]
```

**pow**

Computes the power for a given number. It is equivalent to x ** y and (x ** y)% z.

```python
>>> pow(3,2)  # 3**2
9
>>> pow(3,2,2)  # 3**2 % 2
1
```

**print**

Displays values ​​to the data stream or `sys.stdout` by default. `sys.stdout` or the system standard output means the function `print` will print the value to the screen. It can be changed to `stdin` or `stderr`.

```python
>>> type(print)
<class 'builtin_function_or_method'>
>>> print(1,2,3,4, sep = ' ,')
1 ,2 ,3 ,4
>>> print(1,2,3,4, sep = '\n')
1
2
3
4
>>> print(1,2,3,4)  # by default sep = " "
1 2 3 4
>>> print(1,2,3,4, sep = '\n', end = '<---\n') # by default end = "\n"
1
2
3
4<---
```

**property**

Creates a property from an object attribute.

```python
>>> class A:
...     __a = 1
...     def set_a(self, val):
...         self.__a = val
...     def get_a(self):
...         return self.__a
...     a = property(get_a, set_a)
... 
>>> a = A
>>> a.a
1
>>> a.a = 10
>>> a.a
10
```

You can use `@property` decorator instead of calling the property object.

```python
>>> class A:
...     __a = 1
...     @property
...     def set_a(self, val):
...         self.__a = val
...     @property
...     def get_a(self):
...         return self.__a
... 
```

**quit**

Allows you to exit the REPL.

```python
>>> quit
Use quit() or Ctrl-D (i.e. EOF) to exit
```
**range**

Returns a range objectg indicating the start and the end. By default step = 1 and start 0.

```python
>>> range
<class 'range'>
>>> range(3)
range(0, 3)
>>> list(range(3))
[0, 1, 2]
>>> list(range(1,9,2))
[1, 3, 5, 7]
>>> list(range(9,2,-1))
[9, 8, 7, 6, 5, 4, 3]
>>> list(range())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: range expected 1 arguments, got 0
>>> for i in range(5):
...     print(i, end = ', ')
... 
0, 1, 2, 3, 4,
```

**repr**

Returns a functional representation as a string of a object.

```python
>>> list_ = [1,2,3]
>>> list_
[1, 2, 3]
>>> repr(list_)
'[1, 2, 3]'
>>> list_.__repr__()
'[1, 2, 3]'
>>> eval(repr(list_))
[1, 2, 3]
>>> eval(repr(list_)) == list_
True
>>> eval(repr(list_)) == eval(list_.__repr__())
True
```

**reversed**[chapter_01]

**round**

Round off a number based on n digits precision.

```python
>>> pi = 3.141592
>>> round(pi,3)
3.142
>>> round(pi,0)
3.0
>>> round(pi)
3
>>> n = 31234.1232
>>> round(n, -1)
31230.0
>>> round(n, -2)
31200.0
```

**set**

Returns an unordered collection of items. Parameter must be a sequence object.

```python
>>> set((1,2,3))
{1, 2, 3}
>>> set([1,2,3])
{1, 2, 3}
>>> set([1,2,3]).pop()
1
```

**setattr**

Allows you to change the value of an attribute for a given object. Equivalent to
object.attr = val.

```python
>>> class A:
...     a
... 
>>> a = A
>>> a.a = 10
>>> a.a
10
>>> setattr(a, 'a', 20)
>>> a.a
20
```

**slice**

Creates a slice object. It is used for extended slicing (e.g. a[0:5:2]: a[0], a[2], a[4])

```python
>>> list_ = [1,2,3,4,5,6]
>>> list_[1:3:1]
[2, 3]
>>> list_[1:1:1]
[]
>>> list_[2:0:2]
[]
>>> list_[-4::2]
[3, 5]
>>> list_[-4:-8:-2]
[3, 1]
```

**sorted**

Returns a list of sorted items based on the items of the iterable object.

```python
>>> sorted(['c', 'a', 'b', 'd', 'h'])
['a', 'b', 'c', 'd', 'h']
>>> sorted(['c', 'a', 'b', 'd', 'h'])
['a', 'b', 'c', 'd', 'h']
>>> sorted(['c', 'a', 'b', 'd', 'h'], reverse = True)
['h', 'd', 'c', 'b', 'a']
>>> def key(e):
...     r = -ord(e)
...     print(f"key({e}) = {r}")
...     return r
... 
>>> sorted(['c', 'a', 'b', 'd', 'h'], key=key)
key(c) = -99
key(a) = -97
key(b) = -98
key(d) = -100
key(h) = -104
['h', 'd', 'c', 'b', 'a']
>>> def key(e):
...     res = ord(e)
...     print(f"key({e}) = {res}")
...     return res
... 
>>> sorted(['c', 'a', 'b', 'd', 'h'], key=key)
key(c) = 99
key(a) = 97
key(b) = 98
key(d) = 100
key(h) = 104
['a', 'b', 'c', 'd', 'h']
```

**staticmethod**

Transforms a function into a static method. A static method is a method that is independent of the class instance.

```python
>>> class A:
...     def add(a,b):
...         return a + b
...     add = staticmethod(add)
... 
>>> A.add(1,3)
4
>>> a = A()
>>> a.add(3,5)
8
```

The last statement of the class be replaced by a decorator.

```python
>>> class A:
...     @staticmethod
...     def add(a,b):
...         return a + b
... 
>>> A.add(1,3)
4
>>> a = A()
>>> a.add(3,5)
8
```

**str**

Returns a visual representation of the object as a string object. If the object
is a string object, then str(object) is equal to object.

```python
>>> str(())
'()'
>>> str()
''
>>> str([])
'[]'
>>> str(5)
'5'
>>> str('5')
'5'
>>> str("5")
'5'
```

**sum**

Returns the sum of all elements of a sequence.

```python
>>> sum([1,3,4,5],3)
16
>>> sum([1,3,4,5])
13
>>> sum([],123)
123
```

**super**


It is frequently used when a method is overloaded in descendant classes.

```python
>>> class A:
...     def __init__(self):
...         print("A.__init__()")
... 
>>> class B(A):
...     def __init__(self):
...         print("B.__init__()")
...         super().__init__()
... 
>>> class C(B):
...     def __init__(self):
...         print("C.__init__()")
...         super().__init__()
... 
>>> c = C()
C.__init__()
B.__init__()
A.__init__()

```

**type**

Returns the type of an object. The test of an object's type is equivalent to `isinstance(type, object)`.

```python
>>> help(type)

class type(object)
 |  type(object_or_name, bases, dict)
 |  type(object) -> the object's type
 |  type(name, bases, dict) -> a new type

>>> type("asd")
<class 'str'>
>>> type("asd") == str
True
>>> isinstance("asd", str)
True

type(name, bases, dict) -> a new type
This notation is used to avoid an explicit definition of the new type.
>>> new = type('New', (str, ), dict(a ='1'))
>>> new
<class '__main__.New'>
>>> class New(str):
...     a = '1'
```

**vars**

If the object is not provided, vars() is equivalent to locals(). Otherwise, vars(object) is equivalent to object.__ dict__.

```python
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'bytes_': <code object <module> at 0x7f65de2731e0, file "/dev/null", line 1>, 'A': <class '__main__.A'>, 'B': <class '__main__.B'>, 'C': <class '__main__.C'>, 'c': <__main__.C object at 0x7f65de15c390>, 'MyType': <class '__main__.MyType'>, 'new': <class '__main__.New'>, 'New': <class '__main__.New'>}
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'bytes_': <code object <module> at 0x7f65de2731e0, file "/dev/null", line 1>, 'A': <class '__main__.A'>, 'B': <class '__main__.B'>, 'C': <class '__main__.C'>, 'c': <__main__.C object at 0x7f65de15c390>, 'MyType': <class '__main__.MyType'>, 'new': <class '__main__.New'>, 'New': <class '__main__.New'>}
>>> vars(new)
mappingproxy({'a': '1', '__module__': '__main__', '__dict__': <attribute '__dict__' of 'New' objects>, '__weakref__': <attribute '__weakref__' of 'New' objects>, '__doc__': None})
>>> new.__dict__
mappingproxy({'a': '1', '__module__': '__main__', '__dict__': <attribute '__dict__' of 'New' objects>, '__weakref__': <attribute '__weakref__' of 'New' objects>, '__doc__': None})
```

**zip**

Concatenates sequences.

```python
>>> list(zip([1,2,3],[4,5,6]))
[(1, 4), (2, 5), (3, 6)]
>>> list(map(lambda x, y : (x,y), [1,2,3],[4,5,6]))
[(1, 4), (2, 5), (3, 6)]
>>> for i, j in zip([1,2,3],[4,5,6]): 
...     print(i, j)
... 
1 4
2 5
3 6
```

## 2. File I/O. <a name="2"></a>

### 2.1 Opening a file. <a name="2.1"></a>

Before reading from and writing to a file, you need to open it. Using the built-in open() function, you can create an object of type file, which you can work on.

**syntax**
```python
f = open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

| mode | Description |
| --- | --- |
| `r` | Opens the file as **read-only** with a pointer placed at the beginning of a given file. |
| `rb` | Opens a file for **reading** in **binary** format. |
| `r+` | Opens a file for **reading** and **writing**. |
| `rb+` | Opens a file for **reading** and **writing** in binary format. |
| `w` | Opens a file for **writing** only. Creates a file if it does not exist. |
| `wb` | Opens a file for **writing** in **binary** format. Creates a file if it doesn't exist. |
| `w+` | Opens a file for **reading** and **writing**. Creates a file if it does not exist. |
| `wb+` | Opens a file for **reading** and **writing** in **binary** format. Creates a file if it does not exist. |
| `a` | Opens for writing, **appending** to the end of the file if it exists. The pointer is at the end of the file. |
| `ab` | Opens for writing, **appending** in **binary** to the end of the file if it exists. |
| `a+` | Opens a file for **appending** and **reading**. The pointer is at the end of the file. |
| `ab+` | Opens a file for **appending** and **reading** in **binary** format. The pointer is at the end of the file. |

```python
>>> f = open("file.txt", "w")
>>> f.
f.buffer          f.fileno(         f.newlines        f.seek(           f.write_through
f.close(          f.flush(          f.read(           f.seekable(       f.writelines(
f.closed          f.isatty(         f.readable(       f.tell(           
f.detach(         f.line_buffering  f.readline(       f.truncate(       
f.encoding        f.mode            f.readlines(      f.writable(       
f.errors          f.name            f.reconfigure(    f.write(          
>>> f.mode
'w'
>>> f.name
'file.txt'
>>> f.closed
f.closed
>>> f.closed
False
>>> f.encoding
'UTF-8'
```

### 2.2 Reading from a file. <a name="2.2"></a>

The `file.read(size)` and `file.readline(size)` method reads a line from an opened file.

```python
>>> help(f.read)

read(size=-1, /) method of _io.TextIOWrapper instance
    Read at most n characters from stream.

>>> f = open("file.txt", "r")
>>> f
<_io.TextIOWrapper name='file.txt' mode='r' encoding='UTF-8'>
>>> f.read(10)
'line 1 <--'
>>> f.read(-1) # by default, size = -1; f.read()
'-\nline 2 <---\nline 3 <---\nline 4 <---\nline 5 <---\nline 6 <---\nline 7 <---\nline 8 <---\nline 9 <---\nline 10 <---'

>>> help(f.readline)

readline(size=-1, /) method of _io.TextIOWrapper instance
    Read until newline or EOF.

>>> f.readline()
'line 1 <---\n'
>>> f.readline() # Reads the first line.
'line 2 <---\n'
>>> f.readline(3) # Reads the third line.
'lin'
>>> f.readline(5)
'e 1 <'
>>> f.tell() # Tells the position of the pointer. 
5
>>> help(f.readlines)

readlines(hint=-1, /) method of _io.TextIOWrapper instance
    Return a list of lines from the stream.

>>> f.readlines()
['---\n', 'line 2 <---\n', 'line 3 <---\n', 'line 4 <---\n', 'line 5 <---\n', 'line 6 <---\n', 'line 7 <---\n', 'line 8 <---\n', 'line 9 <---\n', 'line 10 <---']

To move the pointer to a given position, use the seek() function.

>>> f.seek(0)
0
>>> f.tell()
0
```

### 2.3 Writing to a file. <a name="2.3"></a>

The `write()` function is used to write to a file opened in write mode. If the file does not exist, then a new one will be created.

```python
>>> f = open('file1.txt', 'w')
>>> help(f.write)

write(text, /) method of _io.TextIOWrapper instance
    Write string to stream.
    Returns the number of characters written (which is always equal to
    the length of the string).

>>> f.write('Hi \n There!')
11
>>> len('Hi \n There!')
11
```

### 2.4 Closing a file. <a name="2.4"></a>

The `close()` method automatically closes the file, and any unsaved information is lost.

```python
>>> f = open('file1.txt', 'r')
>>> f.readline()
'Hi \n'
>>> f.readline()
' There!'
>>> f.closed
False
>>> f.close()
>>> f.closed
True
```

## 3. [Standard Modules.](https://docs.python.org/3/library/index.html) <a name="3"></a>

Standard modules can be divided into groups by topic.

pathlib — Object-oriented filesystem paths
os.path — Common pathname manipulations
fileinput — Iterate over lines from multiple input streams
stat — Interpreting stat() results
filecmp — File and Directory Comparisons
tempfile — Generate temporary files and directories
glob — Unix style pathname pattern expansion
fnmatch — Unix filename pattern matching
linecache — Random access to text lines
shutil — High-level file operations


| Topic | Modules |
| --- | --- |
| Internet Data Handling | base64, binhex, binascii, email, json, mailbox, mailcap, mimetypes, quopri, uu. |
| Development Tools | unittest, typing , pydoc, doctest, test, 2to3. |
| Debugging and Profiling | cProfile, faulthandler , pdb, profile, trace, tracemalloc. | 
| Graphical | IDLE, PyGObject, PyGTK, PyQt, PySide2, wxPython, Tkinter. |
| Internet Protocols | cgi, cgitb, imaplib, ipaddress, nntplib, poplib, smtplib, socket, syncore, telnetlib, urllib, urllib2. |
| Platform | UNIX: pwd , grp , fcntl , resource , termios. |
| Language Services | ast, compileall, dis, keyword, parser, pickletools, pyclbr, py_compile, symbol, symtable, tabnanny, token, tokenize.  |
| Networking | asyncio, asynchat, asyncore, mmap, select, selectors, signal, socket, ssl. |
| Concurrent Execution | concurrent.futures, multiprocessing, multiprocessing.shared_memory, queue, sched, subprocess,  threading, _thread. |
| OS Services | argparse, ctypes, curses, curses.ascii, curses.panel, curses.textpad, errno, io, logging, logging.config, logging.handlers , getopt, getpass, platform, time, os. |
| Cryptographic Services | hashlib, hmac, secrets. |
| File Formats | configparser, csv, netrc, plistlib, xdrlib. |
| Data Compression | bz2, gzip, lzma, tarfile, zlib, zipfile. |
| Data Persistence | copyreg, dbm, marshal, pickle, shelve, sqlite3. |
| File and Directory Access | filecmp, fileinput, fnmatch, glob, linecache, os.path, pathlib, stat, shutil, tempfile. |
| Functional Programming | functools, itertools , operator. |
| Numeric and Mathematics | cmath, decimal, fractions, math, numbers, random, statistics. |
| Data Types | array, bisect, calendar, collections, collections.abc, copy, datetime, enum, graphlib, heapq, pprint, reprlib, types, weakref, zoneinfo. |
| Runtime Services | array, atexit, calendar, cmath, copy, datetime, gettext, itertools, locale, math, random, sets, struct, sys, traceback. |
| Text Processing Services | string, re, difflib, textwrap, unicodedata, stringprep, readline, rlcompleter. |
| Binary Data Services | struct, codecs. |


### [base64](https://docs.python.org/3.9/library/base64.html)

This module provides binary data encoding and decoding functions in the formats defined by RFC3548 for base16, base32, and base64. It is used in the HTTP protocol for binary data transmission. 

```python
>>> dir(base64)
['MAXBINSIZE', 'MAXLINESIZE', '_85encode', '_A85END', '_A85START', '__all__', '__builtins__', '__cached__', 
'__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_a85chars', '_a85chars2', 
'_b32alphabet', '_b32rev', '_b32tab2', '_b85alphabet', '_b85chars', '_b85chars2', '_b85dec', 
'_bytes_from_decode_data', '_input_type_check', '_urlsafe_decode_translation', '_urlsafe_encode_translation', 
'a85decode', 'a85encode', 'b16decode', 'b16encode', 'b32decode', 'b32encode', 'b64decode', 'b64encode', 'b85decode', 
'b85encode', 'binascii', 'bytes_types', 'decode', 'decodebytes', 'decodestring', 'encode', 'encodebytes', 'encodestring', 
'main', 're', 'standard_b64decode', 'standard_b64encode', 'struct', 'test', 'urlsafe_b64decode', 'urlsafe_b64encode']
```

#### Base64 encoding and decoding

**b64encode syntax**

`b64encode(s, altchars=None)`

Encodes a bytes-like object `s`. If `altchars` is specified( not None), it is a byte string object of length 2, which defines special characters for the `+` and `/` characters.

```python
>>> import base64
>>> string = "Hi There!"
>>> bytes_ = string.encode("UTF-8")
>>> b64 = base64.b64encode(bytes_) # takes a bytes object not string !!!
>>> b64
b'SGkgVGhlcmUh'
>>> type(b64)
<class 'bytes'>
>>> type(bytes_)
<class 'bytes'>	
>>> b64_decode = b64.decode("UTF-8") # converts bytes object to string object. !!!
>>> b64_decode
'SGkgVGhlcmUh'
>>> type(b64_decode)
<class 'str'>
```

**b64decode syntax**

`b64decode(s, altchars=None, validate=False)`

Decode the Base64 encoded bytes-like object or ASCII string s. It returns as a bytes object.

```python
>>> b64_decode = base64.b64decode(b64)
>>> b64_decode
b'Hi There!'
>>> b64_decode.decode('utf-8')
'Hi There!'
```

**base64 encode decode a file**

```python
>>> import base64
>>> for line in open("file.txt"):
...     line_bytes = line.encode('ascii')
...     line_b64_enc = base64.b64encode(line_bytes)
...     print(line_b64_enc)
...     line_decode = base64.b64decode(line_b64_enc)
...     line_dec = line_decode.decode('ascii')
...     print(line_dec)
...     with open("file1.b64", "ab+") as f:  # append each line in binairy.
...         f.write(line_b64_enc)
... 
b'bGluZV8wMQkJPC0tLS0tLQo='
line_01         <------

24
b'bGluZV8wMiAJPC0tLS0tLQo='
line_02         <------

24
b'bGluZV8wMwkJPC0tLS0tLQo='
line_03         <------

24
b'bGluZV8wNCAJPC0tLS0tLQo='
line_04         <------

24
b'bGluZV8wNSAJPC0tLS0tLQo='
line_05         <------

24
b'bGluZV8wNiAJPC0tLS0tLQo='
line_06         <------

24
b'bGluZV8wNyAJPC0tLS0tLQ=='
line_07         <------
24

# content of file1.b64
bGluZV8wNyAJPC0tLS0tLQ==bGluZV8wMQkJPC0tLS0tLQo=bGluZV8wMiAJPC0tLS0tLQo=bGluZV8wMwkJPC0tLS0tLQo=bGluZV8wNCAJPC0tLS0tLQo=bGluZV8wNSAJPC0tLS0tLQo=bGluZV8wNiAJPC0tLS0tLQo=bGluZV8wNyAJPC0tLS0tLQ==
```

#### Base32 encoding and decoding

```python
>>> import base64 
>>> string = "Hi There!"
>>> bytes_ = string.encode("ascii")
>>> b32 = base64.b32encode(bytes_)
>>> b32
b'JBUSAVDIMVZGKII='
>>> b32_decode = base64.b32decode(b32)
>>> b32_decode
b'Hi There!'
>>> b32_decode.decode('ascii')
'Hi There!'

```

#### hexadecimal(Base16) encoding and decoding

```python
>>> import base64 
>>> string = "Hi There!"
>>> bytes_ = string.encode("ascii")
>>> b16 = base64.b16encode(bytes_)
>>> b16
b'486920546865726521'
>>> b16_decode = base64.b16decode(b16)
>>> b16_decode
b'Hi There!'
>>> b16_decode.decode('ascii')
'Hi There!'
```

### [binhex](https://docs.python.org/3.9/library/binhex.html)

This module provides binary data encoding and decoding functions in binhex4 format.

**binhex.binhex syntax**

`binhex(infilename, outfilename)`

```python
>>> import binhex
>>> binhex.binhex('file.txt', 'file1.hqx')
>>> for line in open('file1.hqx', 'r'):
...     print(line)
... 
(This file must be converted with BinHex 4.0)



:#'CTE'8ZG(Kd!&4&@&3rN!3!N!9f!*!%ET*XD@jPAc!a#3Nm,C!'#QaTEQ9I-$)

J#6`YN!B+E'PZC9m`-`N*2#f3"JTXD@jPAc!d)!Nm,C!'#QaTEQ9I-$8J#6`YN!B

+E'PZC9m`0L!*2#f3"JTXD@jPAc!h)!Nm,C!'2Jd!!!:
```

**binhex.hexbin syntax**

`hexbin(infilename, outfilename)`

```python
>>> binhex.hexbin('file1.hqx', 'file1.txt')
>>> for line in open('file1.txt', 'r'):
...     print(line)
... 
line_01         <------

line_02         <------

line_03         <------

line_04         <------

line_05         <------

line_06         <------

line_07         <------
```

### [binascii](https://docs.python.org/3.9/library/binascii.html?highlight=binascii)

Convert between binary and various ASCII-encoded binary representations.

**binascii.a2b_hex, binascii.unhexlify**

Coverts binary data to hexadecimal and returns a bytes object.

```python
>>> binascii.b2a_hex('Hi there!'.encode('utf-8')) # input should be a byte object.
b'486920746865726521' # length = 2 * len(input) = 2 * 9 = 18
>>> binascii.hexlify('Hi there!'.encode('utf-8'))
b'486920746865726521'
```

**binascii.a2b_hex, binascii.unhexlify**

Coverts hexadecimal to binary data and returns a bytes object.
The input should have an even number of hex digits.

```python
>>> binascii.unhexlify(b'486920746865726521')
b'Hi there!'
>>> binascii.unhexlify(b'486920746865726521').decode('utf-8')
'Hi there!'
>>> binascii.a2b_hex(b'486920746865726521').decode('utf-8')
'Hi there!'
```

### [sys](https://docs.python.org/3.9/library/sys.html?highlight=sys#module-sys)

The sys module contains most of the information relating to the current execution, as well as a series of basic functions and objects of the low level.

**argv**

Contains the list of parameters of a given script. The first element of the list is the name of the script(.py) followed by the list of parameters.

**executable**

Returns the path of the Python interpreter.

```python
>>> sys.executable
'/home/.../bin/python3'
```

**exc_info**

Returns a tuple contains the type of exception, the instance of the exception, and the traceback object(sys.last_type, sys.last_value, sys.last_traceback).

```python
>>> import sys
>>> sys.exc_info()
(None, None, None)
>>> try:
...     a = input()
...     a = a/3
... except:
...     print(sys.exc_info())
... 
qwe
(<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'str' and 'int'"), <traceback object at 0x7f13b8ccb690>)

>>> sys.last_type
<class 'TypeError'>
>>> sys.last_value
TypeError("unsupported operand type(s) for /: 'str' and 'int'")
>>> sys.last_traceback
<traceback object at 0x7f13b8ccb690>
```

**platform**

Returns the type of the current running platform.

```python
>>> sys.platform
'linux'
```

**builtin_module_names** 

Returns a tuple of strings containing the names of all available modules.

```python
>>> sys.builtin_module_names
('_abc', '_ast', '_codecs', '_collections', '_functools', '_imp', '_io', '_locale', '_operator', '_signal', '_sre', 
'_stat', '_string', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'atexit', 'builtins', 
'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time', 'xxsubtype', 'zipimport')
```

**byteorder**

Returns 'big' if the bits are in most significant order(big-Endian), and 'little' if it is in least significant order(little-Endian).

```python
>>> sys.byteorder
'little'
```

**maxsize**

Returns an integer that represents the maximum value a variable can have. In a 32-bit platform, the value is usually 2 ** 33 - 1 (2147483647), and in a 64-bit platform it is 2 ** 63 - 1 (9223372036854775807).

```python
>>> sys.maxsize
9223372036854775807
```

**version**

Returns the version of the Python interpreter.

```python
>>> sys.version
'3.7.6 (default, Jan  8 2020, 19:59:22) \n[GCC 7.3.0]'
```

**version_info**

Returns a tuple containing five version number components.

```python
>>> sys.version_info
sys.version_info(major=3, minor=7, micro=6, releaselevel='final', serial=0)
```

**api_version**

Returns the C API version.

```python
>>> sys.api_version
1013
```


**stdin, stdout, stderr**

standard input, standard output and standard error stream.

```python
>>> sys.stdin
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
>>> sys.stdout
<_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
>>> sys.stdout.write("Hi there!\n") # print out the message and returns the len of the string.
Hi there!
10	
>>> a = sys.stderr.write("Error\n")
Error
```

**ps1, ps2**

Returns the primary and the secondary prompt for the interpreter.

```python
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '

```

**implementation**

Returns an object containing information about the running python interpreter.

```python
>>> sys.implementation
namespace(_multiarch='x86_64-linux-gnu', cache_tag='cpython-37', hexversion=50792176, 
	name='cpython', version=sys.version_info(major=3, minor=7, micro=6, releaselevel='final', serial=0))
```

### [sys](https://docs.python.org/3/library/os.html)

The os module groups together 333 functions or objects.

```python
>>> len(dir(os))
333
>>> len([n for n in dir(os) if not n.startswith("_")])
313
```

