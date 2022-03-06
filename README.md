<!-- MIT License

Copyright (c) 2022, Harmouch101
All rights reserved.
 -->

<div align="center">
    <a href="https://gitter.im/py-awesome/community">
       <img src="https://img.shields.io/badge/GITTER-join%20chat-green.svg?style=for-the-badge&logoColor=blue&color=black" alt="Join the chat at https://gitter.im/py-awesome/community"/>
    </a>
    <a href="https://github.com/Harmouch101/awesome-python">
       <img src="https://img.shields.io/badge/open_source-%F0%9F%A4%8D-3DA639.svg?style=for-the-badge&logoColor=blue&color=black" alt="Open Source Love"/>
    </a>
    <a href="https://github.com/Harmouch101/awesome-python/blob/master/LICENSE">
       <img src="https://img.shields.io/github/license/Harmouch101/awesome-python?style=for-the-badge&logoColor=blue&color=black" alt="License"/>
    </a>
    <a href="https://github.com/Harmouch101/awesome-python/blob/master/CODE_OF_CONDUCT.md">
       <img src="https://img.shields.io/badge/code_of_conduct-🌐-ff69b4.svg?style=for-the-badge&logoColor=blue&color=black" alt="Code of Conduct"/>
    </a>
    <a href="https://github.com/Harmouch101/awesome-python/">
       <img src="https://img.shields.io/github/repo-size/Harmouch101/awesome-python?style=for-the-badge&logoColor=blue&color=black" alt="Repo Size"/>
    </a>
</div>

<!-- 
[![Latest Version](https://img.shields.io/github/v/tag/Harmouch101/awesome-python?sort=semver&label=version)](https://github.com/Harmouch101/awesome-python/) -->

<!-- 
[![Last Commit](https://img.shields.io/github/last-commit/Harmouch101/awesome-python?color=brown&logo=github&logoColor=green&style=for-the-badge)](https://github.com/Harmouch101/awesome-python/commits/master)
 -->

<div align="center">
<!--     <span>
        <a href="https://github.com/Harmouch101/awesome-python">
            <img loading="lazy" width="149" height="149" src="https://github.blog/wp-content/uploads/2008/12/forkme_right_darkblue_121621.png?resize=149%2C149" class="attachment-full size-full jetpack-lazy-image" alt="Fork me on GitHub" data-recalc-dims="1" data-lazy-src="https://github.blog/wp-content/uploads/2008/12/forkme_right_darkblue_121621.png?resize=149%2C149&is-pending-load=1" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" align="right" float="right">
        </a>
    </span> --> 
    <span display="inline-block">
        <h1>😎 Awesome Python!</h1>
    </span>
</div>

<div align="center">
    <a href="https://github.com/Harmouch101/awesome-python">
        <img src="./assets/Banner1.jpg" alt="Awesome Python">
    </a>
    <br>
</div>

---

## 📜 Summary

A curated list of python tutorials, notes, slides deck, files related to pycon talks, and a handful list of books I read and/or am currently reading. This repository can be used as a reference documentation for mastering the python programming language and other related content like frameworks and such.

This repository serves three primary roles:

1. Sharing an opinionated list of python videos. 

2. Sharing my own notes of what I learned while watching Pycon on YT, reading books, and other resources.

3. Sharing a handful list of books that can play a significant role in honing your python skills. 


> If you are looking for a way to contribute to the project, please refer to the [`Guideline`][00].  

> Don't forget to slap that ⭐ button an odd number of times ;-) 

> Currently maintained by [`Mahmoud Harmouch`][01].  

---

## 📜 Requirements:

<b>Python 3.6 +.</b>

---

## 👉 Table Of Content (TOC). <a name="TOC"></a>

1. [Awesome Python Talks](#Talks)   
    1.1 [Novice Level - Core](#Novice)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.1.1 [Stuart Williams - Python Epiphanies](#1.1.1)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.1.2 [Trey Hunner - Hands-On Intro to Python](#1.1.2)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.1.3 [Jessica McKellar - Hands-on intro to Python](#1.1.3)   
    1.2 [Intermediate Level - Core](#Intermediate)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.2.2 [Luciano Ramalho - Pythonic Objects](#1.2.1)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.2.2 [Luciano Ramalho - Pythonic APIs](#1.2.2)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.2.3 [Luciano Ramalho - Decorators & Descriptors](#1.2.3)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.2.4 [Trey Hunner - Lazy Looping in Python](#1.2.4)    
    &nbsp;&nbsp;&nbsp;&nbsp;1.2.5 [Trey Hunner - List Comprehensions & Generator](#1.2.5)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.2.6 [Trey Hunner - Readable Regular Expressions](#1.2.6)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.2.7 [Raymond Hettinger - Dataclasses](#1.2.7)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.2.8 [Raymond Hettinger - OOP from scratch](#1.2.8)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.2.9 [Ariel Ortiz - Design Patterns in Python for the Untrained Eye](#1.2.9)   
    1.3 [Fun To Watch](#Fun)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.3.1 [David Beazley - Discovering Python](#1.3.1)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.3.2 [David Beazley - The Fun of Reinvention](#1.3.2)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.3.3 [David Beazley - Fear and Awaiting in Async](#1.3.3)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.3.4 [David Beazley - Built in Super Heroes](#1.3.4)   
    1.4 [Python 2 and Python 3](#2to3)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.4.1 [Brett Cannon - Python 3.3 is Better than  Python 2.7](#1.4.1)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.4.2 [Brett Cannon - How to make your code Python 2/3 compatible](#1.4.2)  
    1.5 [DSA](#DSA)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.5.1 [Brandon Rhodes - Data Structures in the Std Lib](#1.5.1)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.5.2 [Justin Abrahms - Computer Science Fundamentals](#1.5.2)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.5.3 [Raymond Hettinger - Modern solvers(BFS, DFS)](#1.5.3)    
    &nbsp;&nbsp;&nbsp;&nbsp;1.5.4 [Raymond Hettinger - Build powerful, new data structures with Python's abstract base classes](#1.5.4)    
    &nbsp;&nbsp;&nbsp;&nbsp;1.5.5 [Claudio Freire - Efficient shared memory data structures](#1.5.5)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.5.6 [Learning Algorithms and Data Structures in Python](#1.5.6)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.5.7 [Nina Zakharenko - Elegant Solutions For Everyday Python Problems](#1.5.8)   
    &nbsp;&nbsp;&nbsp;&nbsp;1.5.8 [Jiaqi Liu - Fuzzy Search Algorithms How and When to Use Them.](#1.5.8)   

    1.6 [DevOps](#DevOps)  
     
    1.6 [Full-Stack](#Full)   

2. [My Notes/Book](#Notes)   
    2.1 [Chapter-01: The Language Basics](#chapter1)   
    2.2 [Chapter-02: Built-In functions and the Std-Modules](#chapter2)  

3. [Python Books](#Books)   
    3.1 [Novice Level](#books3.1)    
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.1 [Head-First Python: A Brain-Friendly Guide
](#books3.1.1)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.2 [Python for Everybody: Exploring Data in Python 3](#books3.1.2)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.3 [Learn Python 3 the Hard Way](#books3.1.3)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.4 [Python Programming for the Absolute Beginner](#books3.1.4)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.5 [Introduction to Computation and Programming Using Python](#books3.1.5)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.6 [Python Programming: An Introduction to Computer Science](#books3.1.6)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.7 [Python Crash Course](#books3.1.7)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.8 [Python for Kids](#books3.1.8)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.9 [Core Python Programming](#books3.1.9)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.10 [Programming Python](#books3.1.10)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.11 [Learning Python](#books3.1.11)    
    &nbsp;&nbsp;&nbsp;&nbsp;3.1.12 [Think Python](#books3.1.12)   
    3.2 [Intermediate Level](#books3.2)    
    &nbsp;&nbsp;&nbsp;&nbsp;3.2.1 [Murach's Python Programming](#books3.2.1)    
    &nbsp;&nbsp;&nbsp;&nbsp;3.2.2 [Python Cookbook](#books3.2.2)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.2.3 [Effective Python: 59 Specific Ways to Write Better Python](#books3.2.3)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.2.4 [Python Tricks: A Buffet of Awesome Python Features](#books3.2.4)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.2.5 [Intermediate Python](#books3.2.5)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.2.6 [Python 3 Object Oriented Programming](#books3.2.6)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.2.7 [Problem Solving with Algorithms and Data Structures Using Python](#books3.2.7)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.2.8 [Practices of the Python Pro](#books3.2.8)   
    3.3 [Reference](#books3.3)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.3.1 [Fluent Python](#books3.3.1)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.3.2 [Mastering Python High Performance](#books3.3.2)   
    &nbsp;&nbsp;&nbsp;&nbsp;3.3.3 [Python Testing with pytest](#books3.2.3)   

---

## 1. 📺 Awesome Python Talks <a name="Talks"></a>

<div align="center">
    <a href="https://github.com/Harmouch101/awesome-python">
        <img src="./assets/Banner2.PNG" alt="Awesome Pycon">
    </a>
    <br>
</div>

#### 🔝 [Go To TOC](#TOC). 

### 1.1 Novice Level <a name="Novice"></a>  

| Thumbnail |  Video Title | YT Links   |  Duration     | Speaker Deck  | Backup files |
| :---:| :---: | :------------:      | :------------:     |  :------------:     | :------------: |
| <img src="https://img.youtube.com/vi/-kqZtZj4Ky0/0.jpg" width="60px"/> | Python Epiphanies <a name="1.1.1"></a>  | [`2014`][000] [`2016`][001] [`2017`][002] [`2018`][003] |  `3:17:08` |  [`2015`][0000] [`2016`][0001] [`2018`][0002] | [`Mega`][00000] |
| <img src="https://img.youtube.com/vi/6zu8lrYn6t8/0.jpg" width="60px"/> | Hands-On Intro to Python <a name="1.1.2"></a>  | [`2017`][010] |  `3:26:03` |  [`2017`][0100]| --- |
| <img src="https://img.youtube.com/vi/MirG-vJOg04/0.jpg" width="60px"/> | Hands-on Intro to Python For Beginning Programmers<a name="1.1.3"></a>  | [`2014`][020] |  `3:21:49` |  --- | --- |

### 1.2 Intermediate Level <a name="Intermediate"></a>   

#### 🔝 [Go To TOC](#TOC). 

| Thumbnail |  Video Title | YT Links   |  Duration   | Speaker Deck  | Backup files |
| :---: | :---: | :------------:      | :------------:     | :------------:     | :------------: |
| <img src="https://img.youtube.com/vi/mUu_4k6a5-I/0.jpg" width="60px"/> | Pythonic Objects <a name="1.2.1"></a>  | [`2019`][110] | `3:22:15` | [`2014`][1100] [`Github`][1101] | [`Mega`][11000] |
| <img src="https://img.youtube.com/vi/k55d3ZUF3ZQ/0.jpg" width="60px"/> | Pythonic APIs <a name="1.2.2"></a>  | [`2016`][120] | `3:01:52` | [`2016`][1200] [`Github`][1201] | [`Mega`][12000] |
| <img src="https://img.youtube.com/vi/81S01c9zytE/0.jpg" width="60px"/> | Decorators & Descriptors <a name="1.2.3"></a>  | [`2017`][130] |  `2:55:02` | [`2017`][1300] | [`Mega`][13000] |
| <img src="https://img.youtube.com/vi/ixiRkUwPI2A/0.jpg" width="60px"/> | Lazy Looping in Python <a name="1.2.4"></a>  | [`2019`][140] |   `3:22:14` | [`2017`][1400] | --- |
| <img src="https://img.youtube.com/vi/_6U1XoxyyBY/0.jpg" width="60px"/> | List Comprehensions & Generators <a name="1.2.5"></a>  | [`2018`][150] |  `3:21:43` |  [`2017`][1500] | --- |
| <img src="https://img.youtube.com/vi/aTZalKdYB44/0.jpg" width="60px"/> | Readable Regular Expressions <a name="1.2.6"></a>  | [`2016`][160] [`2017`][161] [`2021`][162] |  `3:19:43` |  [`2016`][1600] [`2017`][1601] [`2021`][1602] | --- |
| <img src="https://img.youtube.com/vi/T-TwcmT6Rcw/0.jpg" width="60px"/> | Dataclasses: The code generator to end all code generators <a name="1.2.7"></a>  | [`2018`][170] |  `00:45:21` |  --- | --- |
| <img src="https://img.youtube.com/vi/8moWQ1561FY/0.jpg" width="60px"/> | Object Oriented Programming from scratch <a name="1.2.8"></a>  | [`2020`][180] |  `1:16:18` |  [`Colab`][1800] | --- |
| <img src="https://img.youtube.com/vi/o1FZ_Bd4DSM/0.jpg" width="60px"/> | Design Patterns in Python for the Untrained Eye  <a name="1.2.9"></a>  | [`2019`][190] |  `3:14:47` | [`2019`][1900] | --- |

### 1.3 Fun To Watch <a name="Fun"></a>   

#### 🔝 [Go To TOC](#TOC). 

| Thumbnail |  Video Title | YT Links   |  Duration   | Speaker Deck  | Backup files |
| :---: | :---: | :------------:      | :------------:     | :------------:     | :------------: |
| <img src="https://img.youtube.com/vi/RZ4Sn-Y7AP8/0.jpg" width="60px"/> | Discovering Python <a name="1.3.1"></a>  | [`2014`][210] |  `00:47:49` |  [`2014`][2100] |[`Mega`][21000] |
| <img src="https://img.youtube.com/vi/js_0wjzuMfc/0.jpg" width="60px"/> | The Fun of Reinvention <a name="1.3.2"></a>  | [`2017 - Screencast`][220] [`2017`][221] |  `00:55:21` |  [`2017`][2200] |[`Mega`][22000] |
| <img src="https://img.youtube.com/vi/Bm96RqNGbGo/0.jpg" width="60px"/> | Fear and Awaiting in Async <a name="1.3.3"></a>  | [`2016 - Screencast`][230] [`2016`][231] | `00:56:42` |  [`2016`][2300] | [`Mega`][23000] |
| <img src="https://img.youtube.com/vi/j6VSAsKAj98/0.jpg" width="60px"/> | Built in Super Heroes <a name="1.3.4"></a>  | [`2016 - Screencast`][240] [`2016`][241] |  `00:44:31` | [`2016`][2400] | [`Mega`][24000] |

### 1.4 Python 2 and Python 3 <a name="2to3"></a>   

#### 🔝 [Go To TOC](#TOC). 

| Thumbnail |  Video Title | YT Links   |  Duration   | Speaker Deck  | Backup files |
| :---: | :---: | :------------:      | :------------:     | :------------:     | :------------: |
| <img src="https://img.youtube.com/vi/f_6vDi7ywuA/0.jpg" width="60px"/> | Python 3.3 is better Than Python 2.7 <a name="1.4.1"></a>  | [`2012`][310] [`2013`][311]   |  `00:53:24` |  [`2013`][3100] | --- |
| <img src="https://img.youtube.com/vi/KPzDX5TX5HE/0.jpg" width="60px"/> | How to make your code Python 2/3 compatible <a name="1.4.2"></a>  | [`2015`][320]   |  `00:28:37` |  [`2015`][3200] | --- |

### 1.5 Data Structures & Algorithms <a name="DSA"></a>   

#### 🔝 [Go To TOC](#TOC). 

| Thumbnail |  Video Title | YT Links   |  Duration   | Speaker Deck  | Backup files |
| :---: | :---: | :------------:      | :------------:     | :------------:     | :------------: |
| <img src="https://img.youtube.com/vi/fYlnfvKVDoM/0.jpg" width="60px"/> | Data Structures in the Std Lib and Beyond  <a name="1.5.1"></a>  | [`2014`][410] |  `00:37:40` |  [`2014`][4100] | --- |
| <img src="https://img.youtube.com/vi/nEquiifH33w/0.jpg" width="60px"/> | Computer science fundamentals  <a name="1.5.2"></a>  | [`2014`][420] |  `00:30:22` |  [`2014`][4200] | --- |
| <img src="https://img.youtube.com/vi/_GP9OpZPUYc/0.jpg" width="60px"/> | Modern solvers: Problems well-defined are problems solved(BFS, DFS)  <a name="1.5.3"></a>  | [`2019`][430] |  `00:47:14` |  [`2019`][4300] | --- |
| <img src="https://img.youtube.com/vi/S_ipdVNSFlo/0.jpg" width="60px"/> | Build powerful, new data structures with Python's abstract base classes  <a name="1.5.4"></a>  | [`2019`][440] |  `1:02:01` |  --- | --- |
| <img src="https://img.youtube.com/vi/52zM4GgmqDE/0.jpg" width="60px"/> | Efficient shared memory data structures  <a name="1.5.5"></a>  | [`2018`][450] |  `00:27:15` | [`2018`][4500] | --- |
| <img src="https://img.youtube.com/vi/HN5-7Kn_XsI/0.jpg" width="60px"/> | Learning Algorithms and Data Structures in Python  <a name="1.5.6"></a>  | [`2012`][460] |  `00:34:43` | --- | --- |
| <img src="https://img.youtube.com/vi/WiQqqB9MlkA/0.jpg" width="60px"/> | Elegant Solutions For Everyday Python Problems  <a name="1.5.7"></a>  | [`2018`][470] |  `00:32:57` | [`2018`][4700] | --- |
| <img src="https://img.youtube.com/vi/kTS2b6pGElE/0.jpg" width="60px"/> | Fuzzy Search Algorithms How and When to Use Them  <a name="1.5.8"></a>  | [`2017`][480] |  `00:30:23` | [`2017`][4800] | --- |

### 1.6 DevOps <a name="DevOps"></a>   

#### 🔝 [Go To TOC](#TOC). 

### 1.7 Full-Stack <a name="Full"></a>   

#### 🔝 [Go To TOC](#TOC). 

---

## 2. 📝 My Notes/Book <a name="Notes"></a>

#### 🔝 [Go To TOC](#TOC). 

### [Chapter-01: The Language Basics][0]. <a name="chapter1"></a>

### [Chapter-02: Built-In functions and the Std-Modules][1]. <a name="chapter2"></a>

---

## 3. 📚 Python Books(Core). <a name="Books">

#### 🔝 [Go To TOC](#TOC). 

### 3.1 Novice Level. <a name="books3.1"> 

| Cover |  Title | Authors   |  Publication(Year)  | Publisher | Store |
| :----: |  :----: | :----:      | :----:     | :----:     | :----: |
| <img src="https://learning.oreilly.com/library/cover/9781491919521/250w/" width="60px"/> | Head-First Python, 2nd Edition.  <a name="books3.1.1"></a>  | Paul Barry | `2016` | [`O'Reilly Media, Inc`][3.1.1] |  [`Amazon`][3.1.1.1] |
| <img src="https://images-na.ssl-images-amazon.com/images/I/51e7gE9IqCL._SX348_BO1,204,203,200_.jpg" width="60px"/> | Python for Everybody.  <a name="books3.1.2"></a>  | Dr. Charles Russell Severance. | `2017` | [`O'Reilly`][3.1.2] |  [`Amazon`][3.1.2.1] |
| <img src="https://images-na.ssl-images-amazon.com/images/I/41sXSVzqW-L._SX380_BO1,204,203,200_.jpg" width="60px"/> | Learn Python 3 the Hard Way, 1st Edition.  <a name="books3.1.3"></a>  | Zed A. Shaw | `2017` | [`Addison-Wesley`][3.1.3] |  [`Amazon`][3.1.3.1] |
| <img src="https://images-na.ssl-images-amazon.com/images/I/51jg6IMYSCL._SX402_BO1,204,203,200_.jpg" width="60px"/> | Python Programming for the Absolute Beginner, 3rd Edition.  <a name="books3.1.4"></a>  | Michael Dawson | `2010` |  Course Technology |  [`Amazon`][3.1.4.1] |
| <img src="https://mitpress.mit.edu/sites/default/files/styles/large_book_cover/http/mitp-content-server.mit.edu%3A18180/books/covers/cover/%3Fcollid%3Dbooks_covers_0%26isbn%3D9780262529624%26type%3D.jpg?itok=QS7XuVRd" width="60px"/> | Introduction to Computation and Programming Using Python, 2nd Edition.  <a name="books3.1.5"></a>  | John V. Guttag, Julie Sussman | `2016` |  [`The MIT Press`][3.1.5] |  [`Amazon`][3.1.5.1] |
| <img src="https://images-na.ssl-images-amazon.com/images/I/41Jbi2BlgEL._SX403_BO1,204,203,200_.jpg" width="60px"/> | Python Programming: An Introduction to Computer Science, 3rd Edition.  <a name="books3.1.6"></a>  | John M. Zelle | `2016` |  Franklin, Beedle & Associates, Inc |  [`Amazon`][3.1.6.1] |
| <img src="https://learning.oreilly.com/library/cover/9781457197185/250w/" width="60px"/> | Python Crash Course, 2nd Edition.  <a name="books3.1.7"></a>  | Eric Matthes | `2019` |  [`No Starch Press`][3.1.7] |  [`Amazon`][3.1.7.1] |
| <img src="https://nostarch.com/sites/default/files/styles/uc_product_full/public/PFK_frontcover.jpg" width="60px"/> | Python for Kids, 2nd Edition.  <a name="books3.1.8"></a>  | Jason R. Briggs | `2012` |  [`No Starch Press`][3.1.8] |  [`Amazon`][3.1.8.1] |
| <img src="https://learning.oreilly.com/library/cover/0132269937/250w/" width="60px"/> | Core Python Programming, 2nd Edition  <a name="books3.1.9"></a>  | Wesley J. Chun | `2006` |  [`Pearson P T R`][3.1.9] |  [`Amazon`][3.1.9.1] |
| <img src="https://learning.oreilly.com/library/cover/9781449398712/250w/" width="60px"/> | Programming Python, 4th Edition  <a name="books3.1.10"></a>  | Mark Lutz | `2010` |  [`O'Reilly Media, Inc.`][3.1.10] |  [`Amazon`][3.1.10.1] |
| <img src="https://learning.oreilly.com/library/cover/9781449355722/250w/" width="60px"/> | Learning Python, 5th Edition.  <a name="books3.1.11"></a>  | Mark Lutz | `2010` |  [`O'Reilly Media, Inc.`][3.1.11] |  [`Amazon`][3.1.11.1] |
| <img src="https://images-na.ssl-images-amazon.com/images/I/51CxdWNJ+OL._SX379_BO1,204,203,200_.jpg" width="60px"/> | Think Python, 2nd Edition.  <a name="books3.1.12"></a>  | Allen B. Downey | `2016` |  [`O'Reilly Media, Inc.`][3.1.12] |  [`Amazon`][3.1.12.1] |

---
## 3.2 Intermediate Level <a name="books3.2"></a>  

#### 🔝 [Go To TOC](#TOC). 

| Cover |  Title | Authors   |  Publication(Year)  | Publisher | Store |
| :----: |  :----: | :----:      | :----:     | :----:     | :----: |
| <img src="https://m.media-amazon.com/images/P/1943872740.01._SCLZZZZZZZ_SX500_.jpg" width="60px"/> |  Murach's Python Programming, 2nd Edition.  <a name="books3.2.1"></a>  | Michael Urban | `2021` | [`Mike Murach & Associates`][3.2.1] |  [`Amazon`][3.2.1.1] |
| <img src="https://m.media-amazon.com/images/P/B094CMKN2J.01._SCLZZZZZZZ_SX500_.jpg" width="60px"/> |  Python Distilled (Developer's Library) 1st Edition.  <a name="books3.2.2"></a>  | David Beazley | `2021` | [`Addison-Wesley Professional`][3.2.2] |  [`Amazon`][3.2.1.2] |
| <img src="https://m.media-amazon.com/images/P/B07ZG18BH3.01._SCLZZZZZZZ_SX500_.jpg" width="60px"/> |  Effective Python, 2nd Edition.  <a name="books3.2.3"></a>  | Brett Slatkin | `2019` | [`Addison-Wesley Professional`][3.2.3] |  [`Amazon`][3.2.1.3] |
| <img src="https://images-na.ssl-images-amazon.com/images/I/418fhXtvPML._SX331_BO1,204,203,200_.jpg" width="60px"/> |  Python Tricks, 1st edition.  <a name="books3.2.4"></a>  | Dan Bader | `2017` | [`Dan Bader`][3.2.4] |  [`Amazon`][3.2.1.4] |
| <img src="https://d2sofvawe08yqg.cloudfront.net/intermediatepython/hero?1549457569" width="60px"/> |  Intermediate Python, 1st edition.  <a name="books3.2.5"></a>  | Obi Ike-Nwosu | `2016` | [`leanpub`][3.2.5] |  --- |
| <img src="https://m.media-amazon.com/images/P/1801077266.01._SCLZZZZZZZ_SX500_.jpg" width="60px"/> | Python Object-Oriented Programming, 4th Edition.  <a name="books3.2.6"></a>  | Steven F. Lott, Dusty Phillips | `2021` | [`Packt Publishing`][3.2.6] |  [`Amazon`][3.2.1.6] |
| <img src="https://images-na.ssl-images-amazon.com/images/I/51YORtBDG4L._SX405_BO1,204,203,200_.jpg" width="60px"/> | Problem Solving with Algorithms and Data Structures Using Python, Kindle Edition.  <a name="books3.2.7"></a>  | Bradley N. Miller, David L. Ranum | `2021` | [`Franklin, Beedle & Associates`][3.2.7] |  [`Amazon`][3.2.1.7] |
| <img src="https://learning.oreilly.com/library/cover/9781617296086/250w/" width="60px"/> | Practices of the Python Pro 1st Edition. <a name="books3.2.7"></a>  | Dane Hillard | `2020` | [`Manning`][3.2.8] |  [`Amazon`][3.2.1.8] |

---

## 3.3 Reference <a name="books3.3"></a>  


#### 🔝 [Go To TOC](#TOC). 

| Cover |  Title | Authors   |  Publication(Year)  | Publisher | Store |
| :----: |  :----: | :----:      | :----:     | :----:     | :----: |
| <img src="https://images-na.ssl-images-amazon.com/images/I/412Er-QBlAL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg" width="60px"/> |  Fluent Python, 2nd Edition.  <a name="books3.3.1"></a>  | Luciano Ramalho | `2022` | [`O'Reilly Media`][3.3.1] |  [`Amazon`][3.3.1.1] |
| <img src="https://images-na.ssl-images-amazon.com/images/I/51s01jZ8IQL._SX404_BO1,204,203,200_.jpg" width="60px"/> |  Mastering Python High Performance.  <a name="books3.3.2"></a>  | Fernando Doglio | `2015` | [`Packt Publishing`][3.3.2] |  [`Amazon`][3.3.2.1] |
| <img src="https://images-na.ssl-images-amazon.com/images/I/41ydjWD5exL._SX415_BO1,204,203,200_.jpg" width="60px"/> |  Python Testing with pytest, 2nd Edition  <a name="books3.3.3"></a>  |  Brian Okken | `2022` | [`Pragmatic Bookshelf`][3.3.3] |  [`Amazon`][3.3.3.1] |

---

#### 🔝 [Go To TOC](#TOC). 

<p align="center">
    © 2022 Mahmoud Harmouch, all rights reserved. Made with ❤️<br/>
    Contributions are welcome!
</p>

<!-- Links -->

[0]: https://harmouch101.github.io/awesome-python/notes/chapter-01:%20The-Language-Basics.html
[1]: https://harmouch101.github.io/awesome-python/notes/chapter-02:%20Built-In-func-&-Std-Modules.html

[00]: https://harmouch101.github.io/awesome-python/CONTRIBUTING.html
[01]: https://github.com/harmouch101

[010]: https://www.youtube.com/watch?v=6zu8lrYn6t8
[0100]: https://intro2017.trey.io/

[000]: https://www.youtube.com/watch?v=Uyj2UFTL_vg
[001]: https://www.youtube.com/watch?v=6inqFd1bUkE
[002]: https://www.youtube.com/watch?v=oQca6eDcjA8
[003]: https://www.youtube.com/watch?v=-kqZtZj4Ky0&t=840s
[0000]: https://www.dropbox.com/s/az1gnn92u8y6eh3/PyCon%202015%20-%20Python%20Epiphanies.pdf?dl=0
[0001]: https://www.dropbox.com/s/dgks2bgnzpycruz/PyCon-2016-Python-Epiphanies.zip?dl=0
[0002]: https://www.dropbox.com/s/xkyk3sgbq5fwdzh/PyCon-2018-Python-Epiphanies.zip?dl=0
[00000]: https://mega.nz/folder/XP4XCIiB#KEex7dWMu6FLAcIOH09H_g

[110]: https://www.youtube.com/watch?v=mUu_4k6a5-I
[1100]: https://speakerdeck.com/ramalho/idiomatic-apis-with-the-python-data-model
[1101]: https://github.com/ramalho/pyob
[11000]: https://mega.nz/file/2XwGiaqB#jL8M3xrlnAYwwFgRvwXZJThi_B_pn-2n3-r-0hmvyWk

[120]: https://www.youtube.com/watch?v=k55d3ZUF3ZQ
[1200]: https://speakerdeck.com/ramalho/pythonic-apis-1
[1201]: https://github.com/fluentpython/example-code
[12000]: https://mega.nz/file/LG5gBC6I#LSU06PQHH_893orecD_PZfeTmX9jaT8uyhSBZ-3daoU

[130]: https://www.youtube.com/watch?v=81S01c9zytE
[1300]: https://speakerdeck.com/ramalho/decorators-decoded 
[13000]: https://mega.nz/file/DfgATCrS#xM4ss0XtUbw86iJTY4yrujC8mrLhyZUE5wtpcl74VQE

[140]: https://www.youtube.com/watch?v=ixiRkUwPI2A
[1400]: https://pycon2019.trey.io/

[150]: https://www.youtube.com/watch?v=_6U1XoxyyBY
[1500]: https://pycon2018.trey.io/

[160]: https://www.youtube.com/watch?v=W4ReH9IPH-Q
[1600]: https://pycon2016.regex.training/

[161]: https://www.youtube.com/watch?v=0sOfhhduqks
[1601]: https://pycon2017.regex.training/

[162]: https://www.youtube.com/watch?v=aTZalKdYB44
[1602]: https://pycon2021.regex.training/

[170]: https://www.youtube.com/watch?v=T-TwcmT6Rcw

[180]: https://www.youtube.com/watch?v=8moWQ1561FY
[1800]: https://colab.research.google.com/drive/1DoRrfo839lT_nqmLU6cVLdZJV9wCR2BW?usp=sharing#scrollTo=bYulP3G2XFwJ

[190]: https://www.youtube.com/watch?v=o1FZ_Bd4DSM
[1900]: https://arielortiz.info/s201911/pycon2019/docs/design_patterns.html

[210]: https://www.youtube.com/watch?v=RZ4Sn-Y7AP8
[2100]: https://speakerdeck.com/pycon2014/discovering-python-by-david-beazley
[21000]: https://mega.nz/file/PWxQiCBZ#bEm7uY_JkPz4kxVYgoSlVdaoMKFOtzgpEDRK3L7HHvk

[220]: https://www.youtube.com/watch?v=js_0wjzuMfc
[221]: https://www.youtube.com/watch?v=5nXmq1PsoJ0
[2200]: https://speakerdeck.com/dabeaz/the-fun-of-reinvention
[22000]: https://mega.nz/file/nLwkGaKT#o0e1aVV98PbOJx1h2BP7gEC77M7p-1coKua4LB3pTW8

[230]: https://www.youtube.com/watch?v=Bm96RqNGbGo
[231]: https://www.youtube.com/watch?v=E-1Y4kSsAFc
[2300]: https://speakerdeck.com/dabeaz/fear-and-awaiting-in-async-a-savage-journey-to-the-heart-of-the-coroutine-dream
[23000]: https://mega.nz/file/yTgSzIoY#R3VR6lLAj8RJ7jugMy6PDPoq-3N1L4j-4RUG9d6vBmo

[240]: https://www.youtube.com/watch?v=j6VSAsKAj98
[241]: https://www.youtube.com/watch?v=lyDLAutA88s
[2400]: https://speakerdeck.com/dabeaz/builtin-superheroes
[24000]: https://mega.nz/file/uf5mWYQK#6k0-a2VKMyfBvA5viWggASC-6Apgehvoh13aDYb3vLM

[020]: https://www.youtube.com/watch?v=MirG-vJOg04

[310]: https://www.youtube.com/watch?v=Ebyz66jPyJg
[311]: https://www.youtube.com/watch?v=f_6vDi7ywuA
[3100]: https://speakerdeck.com/pyconslides/python-3-dot-3-trust-me-its-better-than-python-2-dot-7-by-dr-brett-cannon

[320]: https://www.youtube.com/watch?v=KPzDX5TX5HE
[3200]: https://speakerdeck.com/pycon2015/3-compatible

[410]: https://youtu.be/fYlnfvKVDoM?t=330
[4100]: https://rhodesmill.org/brandon/slides/2014-04-pycon/data-structures/

[420]: https://www.youtube.com/watch?v=nEquiifH33w
[4200]: https://speakerdeck.com/pycon2014/computer-science-fundamentals-for-self-taught-programmers-by-justin-abrahms

[430]: https://www.youtube.com/watch?v=_GP9OpZPUYc
[4300]: https://rhettinger.github.io/

[440]: https://www.youtube.com/watch?v=S_ipdVNSFlo

[450]: https://www.youtube.com/watch?v=52zM4GgmqDE
[4500]: https://speakerdeck.com/pycon2018/claudio-freire-efficient-shared-memory-data-structures

[460]: https://www.youtube.com/watch?v=HN5-7Kn_XsI

[470]: https://www.youtube.com/watch?v=WiQqqB9MlkA
[4700]: https://www.slideshare.net/nnja/elegant-solutions-for-everyday-python-problems-pycon-2018

[480]: https://www.youtube.com/watch?v=kTS2b6pGElE
[4800]: https://github.com/itsJiaqi/fuzzy-search-talk

<!-- Books -->

[3.1.1]: https://www.oreilly.com/library/view/head-first-python/9781491919521/
[3.1.1.1]: https://www.amazon.com/_/dp/1491919531?tag=oreilly20-20

[3.1.2]: https://www.py4e.com/book
[3.1.2.1]: https://www.amazon.com/Python-Everybody-Exploring-Data/dp/1530051126

[3.1.3]: https://learnpythonthehardway.org/python3/
[3.1.3.1]: https://www.amazon.com/dp/0134692888/?tag=devdetailpage02-20

[3.1.4.1]: https://www.amazon.com/Python-Programming-Absolute-Beginner-3rd/dp/1435455002

[3.1.5]: https://mitpress.mit.edu/books/introduction-computation-and-programming-using-python-second-edition
[3.1.5.1]: https://www.amazon.com/Introduction-Computation-Programming-Using-Python/dp/0262529629

[3.1.6.1]: https://www.amazon.com/Python-Programming-Introduction-Computer-Science-dp-1590282752/dp/1590282752

[3.1.7]: https://www.oreilly.com/library/view/python-crash-course/9781492071266/
[3.1.7.1]: https://www.amazon.com/Python-Crash-Course-2nd-Edition-dp-1593279280/dp/1593279280

[3.1.8]: https://nostarch.com/pythonforkids
[3.1.8.1]: https://www.amazon.com/dp/1593274076/?tag=devdetailpage02-20

[3.1.9]: https://www.oreilly.com/library/view/core-python-programming/0132269937/
[3.1.9.1]: https://www.amazon.com/Core-Python-Programming-Wesley-Chun/dp/0132269937

[3.1.10]: https://www.oreilly.com/library/view/programming-python-4th/9781449398712/
[3.1.10.1]: https://www.amazon.com/_/dp/0596158106?tag=oreilly20-20

[3.1.11]: https://www.oreilly.com/library/view/programming-python-4th/9781449398712/
[3.1.11.1]: https://www.amazon.com/_/dp/0596158106?tag=oreilly20-20

[3.1.12]: https://greenteapress.com/wp/think-python-2e/
[3.1.12.1]: https://www.amazon.com/Think-Python-Like-Computer-Scientist/dp/1491939362

[3.2.1]: https://www.murach.com/shop/murach-s-python-programming-2nd-edition-detail
[3.2.1.1]: https://www.amazon.com/Murachs-Python-Programming-Joel-Murach-dp-1943872740/dp/1943872740

[3.2.2]: https://www.oreilly.com/library/view/python-distilled/9780134173399/
[3.2.1.2]: https://www.amazon.com/Python-Essential-Reference-Developers-Library-dp-0134173279/dp/0134173279

[3.2.3]: https://www.oreilly.com/library/view/python-distilled/9780134173399/
[3.2.1.3]: https://www.amazon.com/Effective-Python-Specific-Software-Development-dp-0134853989/dp/0134853989

[3.2.4]: https://realpython.com/products/real-python-course/
[3.2.1.4]: https://www.amazon.com/Python-Tricks-Buffet-Awesome-Features/dp/1775093301

[3.2.5]: https://leanpub.com/intermediatepython

[3.2.6]: https://www.packtpub.com/product/python-3-object-oriented-programming-third-edition/9781789615852
[3.2.1.6]: https://www.amazon.com/Python-Object-Oriented-Programming-maintainable-object-oriented-dp-1801077266/dp/1801077266

[3.2.7]: https://fbeedle.com/our-books/10-problem-solving-with-algorithms-and-data-structures-using-python-2nd-ed-9781590282571.html
[3.2.1.7]: https://www.amazon.com/Problem-Solving-Algorithms-Structures-Python-ebook/dp/B09NF2TXSZ

[3.2.8]: https://www.oreilly.com/library/view/practices-of-the/9781617296086/
[3.2.1.8]: https://www.amazon.com/Practices-Python-Pro-Dane-Hillard/dp/1617296082

[3.3.1]: https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/
[3.3.1.1]: https://www.amazon.com/Fluent-Python-Concise-Effective-Programming-dp-1492056359/dp/1492056359

[3.3.2]: https://www.packtpub.com/product/mastering-python-high-performance/9781783989300
[3.3.2.1]: https://www.amazon.com/Mastering-Python-Performance-Fernando-Doglio/dp/1783989300

[3.3.3]: https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/
[3.3.3.1]: https://www.amazon.com/Python-Testing-pytest-Effective-Scalable-dp-1680508601/dp/1680508601

