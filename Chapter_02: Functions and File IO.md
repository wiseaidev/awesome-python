# Chapter_02: Functions and File I/O.

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
2. [File I/O](#2)

## 1. Functions. <a name="1"></a>

A function is an object Like any other thing in python. It takes arguments(parameters) and returns another object. It is defined using the `def` keyword.

```python
def function_name(parameters,...):
	# internal variables and statements
	return some_operation(parameters)

>>> def mul(a,b):
...     return a * b
...
```

The return statement returns a value which is in our case the multiplication of x and y. Our function is callable(you can pass it some parameters).

```python
>>> a = 10
>>> b = 12.13
>>> c = mul(a,b)
>>> c
121.30000000000001  # See chapter_01 to know why the output looks like that.
>>> c = mul("string",3)
>>> c
'stringstringstring'
```

The function can be nested and return any data types (tuples, lists, sets, functions):

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

If there isn't any return value, the returned data will be a None object(void function):

```python
>>> def do_nothing():
...     pass
... 
>>> do_nothing()
>>> print(do_nothing())
None
```

A function can take any number of parameters or not a single one.

```python
>>> def mul(a, b, c=5): # default value if not passed
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

you can also specify the return data type of a function:

```python


```
An anonymous function is used to do some fast computation. It can only take one expression. It doesn't have a name, hence the name anonymous. It is defined using the keyword `lambda`.

```python

general form: lambda input_variables: expression

>>> f = lambda x : x ** 3 + x ** 2 - x + 1
>>> f(1)
2
