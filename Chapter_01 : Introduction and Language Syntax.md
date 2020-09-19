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
	3.4	[literals](#3.4)    
		3.4.1 [String Literals](#3.4.1)    
			3.4.1.1 [Special characters](#3.4.1.1)    
		3.4.2 [Numeric literals](#3.4.2)    
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

This following list describes the different areas in which Python is mostly used:
- System Administration: System administrators often need to design small programs to automate certain tasks. Therefore the usage of python because it is simpler and more direct;
- Rapid Prototyping: [TODO];
- Scientific Research: [TODO];
- Management Applications: [TODO];
- Web Applications: [TODO].

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

you can also use the `exit()` method to exit from the interactive mode.


## 3. Language Syntax <a name="3"></a>

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

- **A Type**: The type of the object is immutable. you cannot change it during the run time.

- **A Value**: The value assigned to the object can be modified depending on the type of the object. For instance, string type objects cannot be modified after their creation. They are called immutable objects.

The following callable objects allow you reading each of the attributes described:
- **id ()**: returns the identifier of an object;
- **type ()**: returns the type of an object;
- **dir ()**: lists all the features of an object.

```python
>>> dir(1)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

In python, objects are destroyed automatically(not explicitly) from memory by the garbage collector, which keeps a reference counter for each object. This field is incremented by one if other objects reference a given object. An example where this variable increases :
- assignment operator
- passing arguments
- inserting a new object into the list (the number of links for the object increases)
- a constructor like foo = bar (foo starts referring to the same object as bar)
 If this referencing(link) is destroyed, then the reference counter will decrease by one. If the reference counter reaches 0, then the interpreter starts the mechanism of destroying the object.

 The reference counter of global variables never drops to zero.

```python
>>> a = 'Hi There!'
>>> sys.getrefcount(a)
2
>>> b = a
>>> sys.getrefcount(a)
3
>>> del b
>>> sys.getrefcount(a)
2
```

## 3.4 Literals <a name="3.4"></a>

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

Strings are alphanumeric values ​​surrounded by quotes. Single or double quotes, or even three single or double-quotes.

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
-  r or R : "raw string" :used with regular expressions and with strings that contain backslashs :

```python
>>> print('D:\files\file1')
D:
  iles
      ile1
>>> print(r'D:\files\file1')
D:\files\file1
```

It seems like`\f` act as a new line with tabulation: `\n\t`, in other terms a vertical tabulation.

- u or U : to indicate a Unicode string. Python 3 adopts the base Unicode standard, and the u prefix disappears.

```python
>>> unicode = u'i am a unicode string'
>>> unicode
'i am a unicode string'
>>> type(unicode)
<class 'str'>
```

- b or B: to indicate a byte string.
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

### 3.4.1.1 Special characters <a name="3.4.1.1"></a>

Python allows you to insert special characters in a string literal. the following table contains a list of spetial characters:

| \Character | Description | Exemple |
| --- | --- | --- |
| `\'`, `\"` | insert a single or double quote in a string literal | `>>> print("python\'s notes")` <br>`python's notes` |
| `\n` | insert a new line | `>>> print("thats\r\nnice!")`<br>`thats nice!` |
| `\r\n`, `\r` | insert a new line in windows, \r on Mac, end of line character(EOL) | `>>> print("thats\r\nnice!")`<br>`thats nice!` |
| `\\` | insert a single backslash in a string literal. | `>>> print("The file is in D:\\files\\file1")`<br>`The file is in D:\files\file1` |
| `\v` | insert a vertical tabulation | `>>> print("This is a vertical\v tabulation")`<br>`This is a vertical`<br>`tabulation` |
| `\t` | insert a Horizontal tabulation(tab) | `>>> print("This is a horizontal\t tabulation")`<br>`This is a horizontal    	tabulation`
| `\b` | erasing/deleting a previous character from a string literal | `>>> print("the last letter will be erased\bd")`<br>`the last letter will be erased` |
| `\Oct` | insert an octal value of a character | `>>> print("\110i There!")`<br>`Hi There!` |
| `\xHx` | insert an hexadecimal value of a character | `>>> print("\x48i There!")`<br>`Hi There!` |
| `\N{noun}` | insert a charater defined by a noun | `>>> print('\N{dollar sign}') `<br>`$`<br>`>>> print('\N{pound sign}')`<br>`£` |

Please refer to [this link](http://www.asciitable.com/) if you want to retrieve ASCII values.

### 3.4.2  Numeric literals <a name="3.4.2"></a>

There are three types of numeric literals to represent values:
- Integers;
- Floating points;
- Complex numbers.




