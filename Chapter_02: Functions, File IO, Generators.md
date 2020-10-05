# Chapter_02: Functions, File I/O and Generators.

Document's Author: Mahmoud Harmouch

---

**Reset your brain**.

Don't try to memorize everything because you don't have to, just remember that something exists to know what you are looking for.

Theory without Practice is useless; Practice without Theory is blind.

Practice/coding is the key to success as a programmer.

Don't give up. Difficult roads **often** lead to beautiful destinations. 

---

## Table Of Content (TOC) <a name="TOC"></a>

1. [Functions](#1)   
	1.1	[Function's Arguments](#1.1)   
	1.2	[Functional Programming](#1.2)   
	&nbsp;&nbsp;&nbsp;&nbsp;1.2.1 [Anonymous Functions](#1.2.1)   
	&nbsp;&nbsp;&nbsp;&nbsp;1.2.2 [Map](#1.2.2)   
	&nbsp;&nbsp;&nbsp;&nbsp;1.2.3 [Filter](#1.2.3)   
	&nbsp;&nbsp;&nbsp;&nbsp;1.2.4 [Reduce](#1.2.4)   


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

Functional Programming is a often used to describe a piece of code that has no effects on other pieces(immutable data). A functional function is a function that does not change the value of data outside it.

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

## 1.2.1 Anonymous Functions. <a name="1.2.1"></a>

An anonymous function, also called lambda function, is a function that doesn't have a name and it is defined using the keyword `lambda`.

**Syntax**

> lambda arguments: expression

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

## 1.2.2 Map. <a name="1.2.2"></a>

`map()` is a built-in function that Accepts a **function** and **sequence**(dataset) as an argument. It works by applying the passed function to each element. Map avoids loops.

**Syntax**

> map(function, sequence)

> returns an object map

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
>>> list(map(lambda x: x**2,list_)) # it is more convinient to use lambda and not a normal function ! 
[4, 16, 25, 49]
>>> list2 = []
>>> for e in list_:
...     list2.append(e**2)
... 
>>> list2
[4, 16, 25, 49]
>>> timeit.timeit("list2 = list(map(lambda x: x**2,list_))","from __main__ import list_",number=100000)
0.24455913900055748  # when you convert it to list,it becomes is slower
>>> timeit.timeit("map(lambda x: x**2,list_)","from __main__ import list_",number=100000)
0.02997873599997547  # faster than a loop
>>> timeit.timeit("for e in list_: list2.append(e**2)","from __main__ import list_,list2",number=100000)
0.18769715700000233
```

