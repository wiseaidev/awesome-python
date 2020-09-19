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
	2.1	[Print Instruction](#3.1)    
	2.2	[Variables](#3.2)    
	2.3	[literals](#3.3)    
	[TODO] 
	.
	.
	.

## 1. A Tutorial Introduction <a name="1"></a>

The goal of this chapter is to get you familiar with python 3 and its essential features.

## 1.1 What is Python ? <a name="1.1"></a>

Python is a high-level programming language that has the following features:
- It is designed to produce high quality, human-readable and maintainable code.
- Portable: Python is a cross-platform programming language, it can be used on Linux, Windows, macOS...  
- Easy to integrate code.
- Object-Oriented programming language.
- Completely Free.
- Highly Productive: A program written in Python is typically 2 to 4 times shorter than an equivalent C++ program.
- Dynamic: the source code is not compiled unlike other languages ​​like C, C++, java, but executed on the fly. It is called an interpreted language.

## 1.2 Why Python ? <a name="1.2"></a>

This following list describes the different areas in which Python is mostly used:
- System Administration: System administrators often need to design small programs to automate certain tasks. Therefore the usage of python because it is simpler and more direct.
- Rapid Prototyping: [TODO]
- Scientific Research: [TODO]
- Management Applications: [TODO]
- Web Applications: [TODO]

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

As you can see, the interpreter displays its copyright message and it is listening for statements from the user.

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

Back to the interpreter, you could exit it by pressing 'Ctrl + D' which signal the interpreter an end of the file command, or by raizing a system exit exception as follows:

```python
>>> raise SystemExit() 
harmouch@kali:~$ 
```

you can also use the exit() command.
