# Chapter_02: Functions, File I/O and Generators.

Document's Author: Mahmoud Harmouch

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
3. [Generators](#3)

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

**filter**

Already described in [this section](#1.2.3).

 