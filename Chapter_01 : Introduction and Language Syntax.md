# Chapter_01: Introduction and Language Syntax.

Document's Author: Harmouch101

---

## Table Of Content <a name="TOC"></a>

1. [A Tutorial Introduction](#1)    
	1.1	[What is Python ?](#1.1)    
	1.2	[Why Python ?](#1.2)    
	1.3 [Interpreted Language](#1.3)    
2. [Running Python](#2)    
3. [Language Syntax](#3)    
	3.1	[Print Instruction](#3.1)   
	3.2	[Comments](#3.2)   
	3.3	[Variables](#3.3)    
	&nbsp;&nbsp;&nbsp;&nbsp;3.3.1 [Names](#3.3.1)     
	3.4	[literals](#3.4)    
	&nbsp;&nbsp;&nbsp;&nbsp;3.4.1 [String Literals](#3.4.1)    
	    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.1.1 [String Formatting](#3.4.1.1)    
	    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.1.2 [Special characters](#3.4.1.2)    
	    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.1.3 [More Strings Examples](#3.4.1.3)    
	    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.1.4 [Useful Strings Functions](#3.4.1.4)    
	    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.1.5 [More Strings Methods Examples](#3.4.1.5)          
	&nbsp;&nbsp;&nbsp;&nbsp;3.4.2 [Numeric literals](#3.4.2)    
	[TODO]     
	.    
	.    
	.    

## 1. A Tutorial Introduction <a name="1"></a>

The goal of this chapter is to get you familiar with python 3 and its essential features.

## 1.1 What is Python ? <a name="1.1"></a>

Python is a high-level programming language that has the following features:
- It is designed to produce high quality, human-readable and maintainable code;
- Portable: Python is a cross-platform programming language, it can be used on Linux, Windows, macOS...;  
- Easy to integrate code;
- Object-Oriented programming language;
- Completely Free;
- Highly Productive: A program written in Python is typically 2 to 4 times shorter than an equivalent C++ program;
- Dynamic: the source code is not compiled unlike other languages ​​like C, C++, java, but executed on the fly. It is called an interpreted language;

## 1.2 Why Python ? <a name="1.2"></a>

Python is a good programming language to start with for a beginner who doesn't know programming at first. Python is very powerful and it is used in a lot of domains. The following list describes the different areas in which Python is mostly used:

- System Administration: System administrators often need to design small programs to automate certain tasks. Therefore the usage of python because it is simpler and more direct;
- Rapid Prototyping: There are a lot of softwares powered by python that allows you to build graphical user interfaces which can be useful for performing specification cycles between clients and the development team. Qt designer is a good example of that;
- Scientific Research: Python is much easier to learn for a researcher who does not have the knowledge of programming. Memory management, the use of pointers, the typing of variables, and all the details of the implementation of a program are all constraints that are far away from the first concerns of a researcher;
- Web Applications: A lot of web frameworks, written in Python(e.g. Twisted, Django ...) are very popular and active which allows python to the forefront of the scene in web development.

## 1.3 Interpreted Language <a name="1.3"></a>

Python commands and instructions are executed by the interpreter, which is written in C language and has different implementations like :
- CPython: C implementation, which is the default implementation of Python;
- Jython: Java implementation, which allows you to run Python source code in a Java environment, and use Java modules in Python code transparently; 
- PyPy: Python implementation of the Python language;
- IronPython: implementation for .NET and Mono;
- Stackless Python: a variant of CPython, slightly faster.

## 2. Running Python <a name="2"></a>

You can run the interpreter by simply entering the 'Python3' command in your terminal :

```sh
~$ python3 
```

```python
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

As you can see, the interpreter displays its python version, the compiler version and the copyright message and it is listening for statements from the user.

One of the most useful features in python is the interaction mode(shell), which allows the user to do operations and see results immediately on the shell.

```python
>>> 699120 + 20958 - 1932
718146
>>> _ 

718146
```

The **_** variable in python holds the result of the previous operation.
you could run your own program(script) in a file and name it with the extension **'.py'** and execute it on the shell without the usage of interactive mode.

```python
# hi.py
print('Hi There!')
```

```bash
~$ python3 hi.py
Hi There!
```

In a Linux distro, you can add at the first line of your program the following line to make the file executable on the shell :

```python
#!/usr/bin/env python3 # must be at the first line or you'll get a syntax error 
# hi.py
print('Hi There!')
```

To make it executable, just give the user the execution privileges using the following

```bash
~$ chmod u+x hi,py 
```

Now you can run the executable file like the following:

```sh
~$ ./hi.py
Hi There!
```

Back to the interpreter, you can exit it by pressing `Ctrl + D` which signal the interpreter an end of the file command, or by raizing a system exit exception as follows:

```python
>>> raise SystemExit() 
```

```sh
~$ 
```

you can also use the `exit()` method to exit the interactive prompt, aka the Read Eval Print Loop (REPL).


## 3. Language Syntax <a name="3"></a>

A complete documentation on Lexical analysis can be found on [Python Docs](https://docs.python.org/3/reference/lexical_analysis.html#lexical-analysis).

## 3.1 Print Instruction <a name="3.1"></a>

```python
>>> print("Hi There!")
Hi There!
>>> print(5)
5
>>> print(4 * 4)
16
>>> print(109 + 15 + 100)
224
>>> print("text goes here!")
text goes here!
>>> print(("text", "goes", "here!"))
('text', 'goes', 'here!')
>>> print(text goes here!)
  File "<stdin>", line 1
    print(text goes here!)
                  ^
SyntaxError: invalid syntax
>>> 
```

## 3.2 Comments  <a name="3.2"></a>

In Python, you can use the hash sign (#) to place comments on a single line.

```python
# first comment
print ("Hi There!") # second comment on the same line of the statement. 
# third comment
# fourth one is the best
```
These comments are ignored by the interpreter which considers, in this case, the `)` symbol as the end of the print statement, except when it is linked to the next line by the backslash character `\` as the following example shows:

```python
>>> print("text goes \
...     here!")
text goes       here!
>>> print("text goes \ # you can't insert a comment here!!!!!
  File "<stdin>", line 1
    print("text goes \ # you can't insert a comment here!!!!!
                                                       ^
SyntaxError: EOL while scanning string literal

```

## 3.3 Variables <a name="3.3"></a>

Python's Variables are object-based. Each object has :

- **An Identifier**: It is a positive unique integer that is created once for all when the object is being created. It is calculated from the object's memory address.

- **A Type**: The type of the object is immutable. you cannot change it during the runtime.

- **A Value**: The value assigned to the object can be modified depending on the type of the object. For instance, string and tuple type objects cannot be modified after their creation. They are called immutable objects.

- **Attributes**: properties of the object.

- **Name**: an object must have a name.

- **One or more base classes**

The following callable objects allow you reading each of the attributes described:

- **id ()**: returns the identifier of an object;

- **type ()**: returns the type of an object;

- **dir ()**: lists all the features of an object.

So as it is said before, Everything in python, at the runtime, is an object.

```python
>>> 32, id(32), type(32)
(32, 94140309858016, '<class 'int'>')
>>> 32, id(32), type(32)
(32, 94140309858016, '<class 'int'>')
>>> 32, id(32), type(32)
(32, 94140309858016, '<class 'int'>')
```

Every object has a **value**(32 here), an id which is used to indicate where it is stored in memory(94140309858016) and a data type(integer).

It is not convenient to use the identifier(id) as a name for the 32 value, Hence the need for assignments.

An assignment is made using the `=` symbol, like this:

```python
>>> a = 32
>>> a,id(a),type(a)
(32, 94140309858016, '<class 'int'>')
```

Notice that the object **name** `a` has the same reference of object 32(id = 94140309858016).

The object name `a` has the following **attributes** :

```python
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> a.__str__()
'32'
```
Notice that the private (`__`) **attribute** 'str' hold the value of a as string.

Let's take the following example :

```python
>>> b = a * 3
>>> b,id(b),type(b)
(96, 94140309860064, '<class 'int'>')
>>> a,id(a),type(a)
(32, 94140309858016, '<class 'int'>')
```

the interpreter takes the expression at the right side of the assignment symbol **=** and evaluates it. As a result, an object of type integer whose value is 96 is created and stored in memory and the reference of that object is assigned to b. Note that, the value of this particular object is already stored in memory. 

```python
>>> 96,id(96),type(96)
(96, 94140309860064, '<class 'int'>')
```

I think, in this particular example, the Python interpreter didn't create a new object of value `96` in memory(because it is already stored at that id for optimization porpuses), it changes the reference of b only. This is only true because 32 is between -5 and 256.

From [python C-API documentation](https://docs.python.org/3/c-api/long.html), I found the following explanation: 

>The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you actually just get back a reference to the existing object. So it should be possible to change the value of 1. I suspect the behavior of Python, in this case, is undefined. :-)

let's try it for a number larger than 256 :

```python
>>> b = 257
>>> id(b)
140086582008304
>>> id(257)
140086582008272
```

So as you can see, b and 257 are different objects in memory.
Now lets create a variable and increment it and see how much it takes space in memory:

```python
>>> a = 0
>>> a += 1
>>> a,id(a),type(a)
(1, 94140309857024, '<class 'int'>')
>>> a += 1
>>> a,id(a),type(a)
(2, 94140309857056, '<class 'int'>')
>>> a += 1
>>> a,id(a),type(a)
(3, 94140309857088, '<class 'int'>')
```

The id increments by 32(i found some cases on the internet where the id has increased by 16, maybe because it was a 32-bit architecture), my computer is 64 bits address space, so i think each object in python is stored on 32 bytes if you have a 64 bit machine.

you can assign one object to several variables simultaneously.

```python
>>> a = b = 8
>>> id(a),id(b)
(94232164422624, 94232164422624)
```

Notice that a and b point to the same object address in memory.

you could assign multiple values to multiple variables at the same time.

```python
>>> a, b = 32, 64
```

In python, objects are destroyed automatically(not explicitly) from memory by the garbage collector, which keeps a reference counter for each object. This field is incremented by one if other objects reference a given object. An example where this variable increases :

- assignment operator
- passing arguments
- inserting a new object into the list (the number of links for the object increases)
- a constructor like foo = bar (foo starts referring to the same object as bar)
 If this referencing(link) is destroyed, then the reference counter will decrease by one. If the reference counter reaches 0, then the interpreter starts the mechanism of destroying the object.

 The reference counter of global variables never drops to zero.

```python
>>> a = 8
>>> sys.getrefcount(a)
2
>>> b = a
>>> sys.getrefcount(a)
3
>>> del b
>>> sys.getrefcount(a)
2
```

![namespace and memory](./resources/namespace_memory.png)

## 3.3.1 Names <a name="3.3.1"></a>

Names are attached, as we saw previously, to objects. The following method shows the names that are stored in the namespace:

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

```

When you create a new object and give it a name, this name is stored in the namespace:

```python
>>> a = 16
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a']
```

You can write a function that returns an object's name and value pair stored in the namespace as a dictionary:

```Python
>>> def names_values():
...     obj = []
...     for (name,value) in globals().items():
...             if not name[:2] == '__':
...                     obj.append((name,value))
...     return dict(obj)
... 

```

globals().items() returns a tuple of names and values.
dir() returns only the name(key)

```Python
>>> names_values()
{}
>>> a = 8
>>> b = 16
>>> c = a
>>> names_values()
{'a': 8, 'b': 16, 'c': 8}
>>> del c
>>> names_values()
{'a': 8, 'b': 16}
```

So it is all about storing and deleting names from the namespace. As it is said previously, the object will be destroyed from memory if the refcount reaches zero. So the object 8 won't be destroyed because it is also referenced by the name `a`.

## 3.4 Literals <a name="3.4"></a>

A complete documentation on Literals can be found on [Python Docs](https://docs.python.org/3/reference/lexical_analysis.html#literals).

A literal in python is the simplest way to create an object, but at the same time it can be a constant, but which does not mean objects. A variable is assigned at the runtime, whereas a literal is assigned at the compile time.

```python
>>> 1 	# numeric literal
1
>>> "here goes a string" 	# string literal
'here goes a string'
>>> [1,2,3]		# list literals
[1, 2, 3]
>>> {'k0':1,'k1':2, 'k3':3}		# dict literal
{'k0': 1, 'k1': 2, 'k3': 3}
```

But this is not useful if you want to manipulate these values without assigning it to a variable. Hence the need for the assignment.

```python
>>> a = 8
```

Here the object whose name is 'a' is created by the numerical literal 8. So, on the left side, we have the variable name and on the right, we have the literal.
To see the difference between the built-in functions and the literals, you can create a list in two different ways :

```python
>>> a = list([1,2,3]) 	# creating a list using a built-in function
>>> a = [1,2,3]		# creating a list using a list literal
```
### 3.4.1 String Literals <a name="3.4.1"></a>

Strings are alphanumeric(text constant) values ​​surrounded by quotes. Single or double quotes, or even three single or double-quotes.

```python
>>> print("here we have a one-line string with one double quote")
here we have a one-line string with one double quote
>>> print('here we have a one-line string with one single quotes')
here we have a one-line string with one single quote
>>> print("""here we have multiple lines
...     string with three double quotes""")
here we have multiple lines
        string with three double quotes
>>> print('''here we have multiple lines
...     string with three single quotes''')
here we have multiple lines
        string with three single quotes
```

It is also possible to prefix strings with a character:
-  **r** or **R** : "raw string" :used with regular expressions and with strings that contain backslashs :

```python
>>> print('D:\files\file1')
D:
  iles
      ile1
>>> print(r'D:\files\file1')
D:\files\file1
```

It seems like`\f` act as a new line with tabulation: `\n\t`, in other terms a vertical tabulation.

- **u** or **U** : to indicate a Unicode string. Python 3 adopts the base Unicode standard, and the u prefix disappears.

```python
>>> unicode = u'i am a unicode string'
>>> unicode
'i am a unicode string'
>>> type(unicode)
<class 'str'>
```

- **b** or **B**: to indicate a byte string. Each byte in a byte string corresponds to a certain value in the range of [0; 255].

```python
>>> b'hi there'
b'hi there'
>>> b'hi there'[3]
116
```

Encoding and decoding methods make it possible to convert from type str to type bytes, using a correspondence table, called codec and having a unique name(UTF-8 is used in the example).

```python
>>> string = 'this is string'
>>> byte_string = string.encode('UTF-8') 	# from str to bytes
>>> byte_string
b'this is string'
>>> decoded_string = byte_string.decode('UTF-8') 	# # from bytes to str
>>> decoded_string
'this is a string'
```
- **f** or **F**: this prefix has been added since python 3.6 which allows you to define a string as formatted. So using this prefix, you can add a placeholder for a certain variable with the help of curly braces `{}` to indicate the appearance of this variable(e.g. precision of a number to display).

```python
>>> from math import cos, pi
>>> print(f'Value of PI with 4 digit precision: {pi:+1.4}')
Value of PI with 4 digit precision: +3.1416
>>> for i in range(1,20):
...     x = cos(pi/i)
...     print(f'|i = {i:<2}| cos(pi/{i:<2}) = {round(x,2):<+5.2}|') 
... 	# < indicates left alignement; ^ for center alignment; > for right alignment;
...		#  the number after the synbol < indicate the width of the column to display
... |  |       |  |  |     |
... |..|       |..|  |.....|
|i = 1 | cos(pi/1 ) = -1.0 |
|i = 2 | cos(pi/2 ) = +0.0 |
|i = 3 | cos(pi/3 ) = +0.5 |
|i = 4 | cos(pi/4 ) = +0.71|
|i = 5 | cos(pi/5 ) = +0.81|
|i = 6 | cos(pi/6 ) = +0.87|
|i = 7 | cos(pi/7 ) = +0.9 |
|i = 8 | cos(pi/8 ) = +0.92|
|i = 9 | cos(pi/9 ) = +0.94|
|i = 10| cos(pi/10) = +0.95|
|i = 11| cos(pi/11) = +0.96|
|i = 12| cos(pi/12) = +0.97|
|i = 13| cos(pi/13) = +0.97|
|i = 14| cos(pi/14) = +0.97|
|i = 15| cos(pi/15) = +0.98|
|i = 16| cos(pi/16) = +0.98|
|i = 17| cos(pi/17) = +0.98|
|i = 18| cos(pi/18) = +0.98|
|i = 19| cos(pi/19) = +0.99|

```

So as you can see, the `f` prefix is so much handy and useful. Alignment is done using one of the following characters:

| align | Description | Example | 
| --- | --- | --- | 
| `<` | align the object to the left. | `>>> print(f"[{'left':<16}]")`<br>[left&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br>`>>> print(f"[{'left':<<16}]")`<br>[left<<<<<<<<<<<<] | 
| `>` | align the object to the right. | `>>> print(f"[{'right':>16}]")`<br>[&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;right]<br>`>>> print(f"[{'right':>>16}]")`<br>[>>>>>>>>>>>right] |
| `^` | align the object to the center. | `>>> print(f"[{'center':^16}]")`<br>[&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;center&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br>`print(f"|{'center':^^16}]")`<br>[^^^^^center^^^^^] |
| `=` | forces the padding to be placed after the sign (`+` or `-`) but before the digits. | `>>> print(f"[{+32:0=+5}]")`<br>[+0032]<br>`>>> print(f"[{+32:^=+10}]")`<br>[+^^^^^^^32] |

The sign option is used only for numbers with the following values:

| sign | Description | Example |  
| --- | --- | --- | 
| `+` | `-` for negative numbers and `+` for positive numbers. | `>>> print(f"[{+32:^+5}]")`<br>[&nbsp;+32&nbsp;]<br>`>>> print(f"[{-32:^+5}]")`<br>[&nbsp;-32&nbsp;] |
| `-` | `-` for negative numbers and nothing for positive numbers. | `>>> print(f"[{+32:^-5}]")`<br>[&nbsp;32&nbsp;&nbsp;] |
| `Space` | `-` for negative numbers and whitespace for positive numbers. | `>>> print(f"[{+32:^ 5}]")`<br>[&nbsp;&nbsp;&nbsp;32&nbsp;&nbsp;] |

the general form of `f` strings is the following:
```python
{variable : fill_padding align sign column_width .precision type}
>>> print(f"{-32.215663:*^+15.2f}")
****-32.22*****
```

### 3.4.1.1 String Formatting <a name="3.4.1.1"></a>

There are three methods in python that can be used to format strings:

- Using the **`%`** modulo sign(borrowed from c language) with one of the following values:

| %type | Description | Example | 
| --- | --- | --- | 
| `%d`,`%i`,`%u` | signed decimal, signed integer and unsigned decimal. | `>>> print("%d + %i = %u"%(10,15,10+15))`<br> 10 + 15 = 25 |
| `%o` | unsigned octal | `>>> print(f"oct: %o"%41)` oct: 51<br> |
| `%x` or `%X` | hexadecimal value, prefixed by 0x or 0X. | `>>> print(f"hex: %x %X"%(0x12,0X32))`<br>hex: 12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32 |
| `%e` or `%E` | scientific notation of a number with a presicion of 6.('e' pr 'E' as exponent) | `>>>print('%E %e pounds' %(212345,212345))`<br>2.123450E+05&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.123450e+05 pounds  |
| `%f` ou `%F` | fixed-point notation with a presicion of 6. | `>>>print('%f %F pounds' %(21.2345,21.2345))`<br>21.234500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;21.234500 pounds |
| `%g` or `%G` | for floating point values, equivalent to %e or %E if the exponent is greater than -4 or less than precision, otherwise equivalent to %f. | `>>> print('%g %G pounds' %(234512312,00000.21000312))`<br>2.34512e+08&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.210003 pounds |
| `%c` | converts the integer to the corresponding unicode character.  | `>>> print('%c is a char' %(123))`<br>{ is a char | 
| `%r` | return the value of the attribute `__repr__` | `>>> a = 10`<br>`>>>a.__repr__()`<br>'10'<br>`>>> print("the value of a.__repr__() is %r"%a)`<br>the value of a.__repr__() is 10 |
| `%s` | return the value of the attribute `__str__` | `>>> a.__str__()`<br>'10'<br>`>>> print("the value of a.__str__() is %s"%a)`<br>the value of a.__str__() is 10 |
| `%%` | insert the % sign. | `>>> print("score is %g %%"%95.1)`<br>score is 95.1 % |
| `%(key)s` | insert the value of the key in the dictionnary. | `>>> print('%(key1)s %(key2)s %(key3)s'%{'key1':'value1','key2':'value2','key3':'value3'})`<br>value1 value2 value3 |

- using the **format** method(borrowed from C# language) like the following examples :
```python
>>> '{0}, {1}, {2}'.format('1', '2', '3')
'1, 2, 3'
>>> '{}, {}, {}'.format('1', '2', '3') 
'1, 2, 3'
>>> '{2}, {1}, {0}'.format('1', '2', '3')
'3, 2, 1'
>>> '{2}, {1}, {0}'.format(*'123')      # unpacking argument sequence
'3, 2, 1'
>>> '{0}, {0}, {0}'.format('1', '2', '3')   # arguments' indices can be repeated
'1, 1, 1'
```
- using the **`f`** prefix as the previous section explains.
for more information about string formatting, you can read [python documentation](https://docs.python.org/3/library/string.html).

### 3.4.1.2 Special characters <a name="3.4.1.2"></a>

Python allows you to insert special characters in a string literal. the following table contains a list of spetial characters:

| \Character | Description | Example |
| --- | --- | --- |
| `\'`, `\"` | insert a single or double quote in a string literal. | `>>> print("python\'s notes")` <br>python's notes |
| `\n` | insert a new line | `>>> print("that's\nnice!")`<br>that's<br>nice! |
| `\r\n`, `\r` | insert a new line in windows, \r on Mac, end of line character(EOL). | `>>> print("that's\r\nnice!")`<br>that's<br>nice! |
| `\\` | insert a single backslash in a string literal. | `>>> print("The file is in D:\\files\\file1")`<br>The file is in D:\files\file1 |
| `\v` | insert a vertical tabulation. | `>>> print("This is a vertical\v tabulation")`<br>This is a vertical<br>tabulation |
| `\t` | insert a Horizontal tabulation(tab). | `>>> print("This is a horizontal\t tabulation")`<br>This is a horizontal&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tabulation |
| `\b` | erase/delete a previous character from a string literal. | `>>> print("the last letter will be erased\bd")`<br>the last letter will be erased |
| `\Oct` | insert an octal value of a character. | `>>> print("\110i There!")`<br>Hi There!` |
| `\xHx` | insert an hexadecimal value of a character. | `>>> print("\x48i There!")`<br>`Hi There! |
| `\N{noun}` | insert a charater defined by a noun. | `>>> print('\N{dollar sign}')`<br>$<br>`>>> print('\N{pound sign}')`<br>£ |

Please refer to [this link](http://www.asciitable.com/) if you want to search for ASCII characters or simply type `man ascii` in your terminal.

### 3.4.1.3 More Strings Examples <a name="3.4.1.3"></a>

```python
>>> a = 'Python is cool'  # String type.
>>> b = r'Python is cool'  # raw String.
>>> a == b   # both strings have the same value.
True
>>> a is b   # but they are not the same object.
False
>>> id(a),id(b)    
(140092435297776, 140092435297904)    # each string points to a different object in memory.
>>> a = 'Python\t is cool'
>>> a = 'Python\tis cool'
>>> b = r'Python\tis cool'
>>> a,type(a),id(a)
('Python\tis cool', <class 'str'>, 140092435297776)	
>>> b,type(b),id(b)
('Python\\tis cool', <class 'str'>, 140092435297840)
Both objects share the same type str but different values and references.
>>> a is b
False
>>> a == b
False
>>> a = r'£'
>>> b = '\u00A3'
>>> c = '\N{pound sign}'
>>> a == b == c
True
>>> a is b is c   
True
>>> id(a),id(b),id(c)  
(140578043342896, 140578043342896, 140578043342896)  # a, b and c are the same object in memory .
>>> a,b,c
('£', '£', '£')   # Same Value.
>>> a = '512512'
>>> b = a.encode(encoding = 'ascii') # create a new object in memory.
>>> b
b'512512'
>>> c = b.decode(encoding = 'ascii') # create another new object in memory and not reference a !!!
>>> c
'512512'
>>> a == c  # same value.
True
>>> a is c  # different objects.
False
>>> a = int(a) # create a new object in memory.
>>> c = int(c) # create another new object in memory.
>>> a is c # same type and value but different objects.
False

Exception for numbers between -5 and 256 as it said before.
>>> a = '128'
>>> b = a.encode(encoding = 'ascii')
>>> c = b.decode(encoding = 'ascii')
>>> a is c
False
>>> c = int(c)
>>> a = int(a)
>>> a is c  # because it is between -5 and 256.
True
``` 
### 3.4.1.4 Useful Strings Functions <a name="3.4.1.4"></a>

For a complete list of string methods, you can refer to[python docs](https://docs.python.org/3/library/stdtypes.html#string-methods).

| Function | Description | Example |
| --- | --- | --- |
| `len(s)` | return the number of element in `s`. | `>>> s = 'this is a string'`<br>`>>> len(s)`<br>16 |
| `min(s)` | return the minimum value in `s`. | `>>> [ord(char) for char in s]`<br>[116, 104, 105, 115, 32, 105, 115, 32, 97, 32, 115, 116, 114, 105, 110, 103]<br>`>>> min(s)`<br>'&nbsp;&nbsp;&nbsp;'<br>`>>> ord(min(s))`<br>32 |
| `max(s)` | return the maximum value in `s`. | `>>> max(s)`<br>'t'<br>`>>> ord(max(s))`<br>116 |
| `sorted(s)` | sort values from lowest to highest. | `>>> sorted(s)`<br>[' ', ' ', ' ', 'a', 'g', 'h', 'i', 'i', 'i', 'n', 'r', 's', 's', 's', 't', 't'] |
| `list(reversed(s))` or `list(s[::-1])` | reverse the order of the values in the string(index 0 becomes index -1...)   | `>>> list(reversed(s))`<br>['g', 'n', 'i', 'r', 't', 's', ' ', 'a', ' ', 's', 'i', ' ', 's', 'i', 'h', 't']<br>`>>>s[::-1]`<br>'gnirts a si siht'<br>`>>> list(s[::-1])`<br>['g', 'n', 'i', 'r', 't', 's', ' ', 'a', ' ', 's', 'i', ' ', 's', 'i', 'h', 't'] |
| `s.startswith('str')` | return `True` only if `s` starts with `str`, otherwise it return `False` | `>>> s`<br>'this is a string'<br>`>>> s.startswith('h')`<br>False`>>> s.startswith('t')`<br>True<br>`>>> s.startswith('th')`<br>True<br>`>>> s.startswith('this')`<br>True |
| `s.endswith('str')` | return `True` only if `s` ends with `str`, otherwise it return `False` | `>>> s.endswith('ng')`<br>True<br>`>>> s.endswith('gn')`<br>False |
| `s.upper()` | converts a string to uppercase. | `>>> s.upper()`<br>'THIS IS A STRING' |
| `s.lower()` | converts a string to lowercase. | `>>> s.lower()`<br>'this is a string' |
| `s.strip()` | removes whitespaces from start and end of the string `s`. | `>>> s = '   Remove start and end whitespaces        '`<br>'`>>> s`'<br>'&nbsp;&nbsp;&nbsp;Remove start and end whitespaces&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'<br>`>>> s.strip()`<br>'Remove start and end whitespaces' |
| `s.lstrip()` or `s.rstrip()` | removes whitespaces from start or from end of the string `s`, respectively. | `>>> s.lstrip()`<br>'Remove start whitespaces&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'<br>`>>> s.rstrip()`<br>'&nbsp;&nbsp;&nbsp;&nbsp;Remove end whitespaces' |
| `s.find('str', start_index)` | return first from left occurrence index of `str` in `s` starting from index `start_index` if found, otherwise return -1 | `>>> s = 'python is so cool'`<br>`>>> s.find('o',5)`<br>11 |
| `s.index('str', start_index)` | same as find except it will throw a `ValueError` exception if `str` is not in `s` | `>>> s.find('1',5)`<br>-1<br>`>>> s.index('1')`<br>Traceback (most recent call last):<br>File `"<stdin>"`, line 1, in `<module>`<br>ValueError : substring not found |
| `s.count('str', start_index)` | count the occurrence of `str` in `s` starting from `start_index`. | `>>> s.count(' ',7)`<br>2 |

### 3.4.1.5 More Strings Methods Examples <a name="3.4.1.5"></a>

```python
>>> s = 'string'
>>> sorted(s)
['g', 'i', 'n', 'r', 's', 't'] # lowest to highest sorting.
>>> sorted(s, reverse = True)
['t', 's', 'r', 'n', 'i', 'g'] # highest to lowest sorting.
>>> list(reversed(s))
['g', 'n', 'i', 'r', 't', 's'] # reverse ordering of the string.
>>> s.upper()
'STRING'
>>> s.lower()
'string'
>>> s.title()
'String'
>>> s.istitle()
False
>>> s.title().swapcase()
'sTRING'
>>> 'st' in s
True
>>> s += s
>>> s
'stringstring'
>>> s.find('i')
3
>>> s.find('i',5)
9
>>> s.find('i',s.find('i') + 1)
9
>>> s.index('i',s.index('i')+1)
9
>>> s.index('1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> s.find('1')
-1
>>> s.count('i')
2
```

### 3.4.2  Numeric literals <a name="3.4.2"></a>

There are three types of numeric literals to represent values:
- **Integers** : reserved for a variable whose value is a stored relative integer in exact value. The possible values ​​for such a variable are only limited by the capabilities of the computer;
- **Floating Point**: it is a variable whose value is a real number, stored as an approximate value in the form of a triplet (s, m, e) where **s** is the **sign** in {-1,1}, **m** **mantissa** and **e** **exponent**. Such a triplet represents the decimal number s*m*b^e in scientific notation where b is the base of representation, namely: 2 on the computers. By varying e, we make the decimal point "float".
The real numbers are stored in Python according to the **double precision** format
specified by the **IEEE 754** standard. Thus, the sign is coded on 1 bit, the exponent on 11
bit and the 52-bit mantissa ,  11 + 1 + 52 -1 = 64 bits; the precision being 52 bits, thus 15 significant digits.

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Number = ± mantissa</font><sup><font style="vertical-align: inherit;">exponent</font></sup><font style="vertical-align: inherit;"> base</font></font><sup><font style="vertical-align: inherit;"></font></sup></p>

	|-63-|62-----------52|51------------------------0|      
	|sign|---exponent----|---------mantissa----------|      
	|1bit|----11bits-----|----------52bits-----------|       

To find information about float numbers used in python, you can use the command sys.float_info like the following:

```python
>>> import sys
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
```

Where :    
   - **max**: maximum representable number;    
   - **max_exp**: maximum degree base **2** (11 bits for the exponent ==> 2<sup>(11-1)</sup> = 1024);    
   - **max_10_exp**: maximum number **e** such that 10<sup>e</sup> is in [min , max];    
   - **min**: minimum representable number;    
   - **min_exp**: minimum degree 2;    
   - **min_10_exp**: minimum number **e** such that 10<sup>e</sup> is in [min , max];    
   - **dig**: maximum number of digits that can accurately display a number;    
   - **mant_dig**: maximum number of digits in the radix number system, which can accurately display a number(53 = 52 mant + 1 sign );    
   - **epsilon**: difference between 1 and the smallest number is greater 1 which can be represented as a floating point number;    
   - **radix**: base of the number system used;    
   - **rounds**: integer constant defining the rounding mode.    

- **Imaginary**: the complex type, corresponds to a variable whose value is a complex number, stored as a couple of floats (so in approximate value). The complex number 1 + 5i is noted 1 + 5J, the number i is noted J.



