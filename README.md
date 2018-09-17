# python_reverse_dict

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Introduction](#introduction)
- [Directories and files description](#directories-and-files-description)
- [Installation](#installation)
- [Usage](#usage)
	- [Options](#options)
	- [Examples of usage](#examples-of-usage)
		- [Example 1: method 1](#example-1-method-1)
		- [Example 2: method 2](#example-2-method-2)
		- [Example 3: method 3](#example-3-method-3)
- [Results: Comparaisons between methods](#results-comparaisons-between-methods)
	- [Major updates](#major-updates)
	- [Table 1: Python2-based methods](#table-1-python2-based-methods)
	- [Table 2: Python3-based methods](#table-2-python3-based-methods)
- [Methods: Python code](#methods-python-code)
	- [Method 1: unique-values, solution based on `dict`](#method-1-unique-values-solution-based-on-dict)
	- [Method 2: non-unique values](#method-2-non-unique-values)
	- [Method 3: type and order preserved](#method-3-type-and-order-preserved)
- [References](#references)
- [License](#license)

<!-- /TOC -->

## Introduction
This project's goal is to compute average run times of different methods of reversing a
dictionary's keys and values in **Python 2.7 &amp; 3**:
* **method 1**<a id="method01"></a>: makes use of dictionary comprehension, and
the dictionary must contain unique values
* **method 2**<a id="method02"></a>: the dictionary doesn't contain unique
values and saves all the keys with the same values in a list
* **method 3**<a id="method03"></a>: makes use of `map(reversed, iter)`, useful when
the type and order of the original dictionary must be preserved (e.g.
`OrderedDict`)

I ran some tests, and **method 1 is the one that provides the best average run
time** for reversing the keys and values of a dictionary. See section
[Comparaisons between different methods](#results-comparaisons-between-methods)
for the average run times of the different methods based on the number of items.

You can also check my blog post [Python tips: reverse a dictionary](https://progsharing.blogspot.com/2018/09/python-tips-reverse-dictionary.html) where I discuss
the implementation of the different methods and the results of the comparaisons of
the methods based on their average run times.

**Note**: I tested the code with **Python 2.7.15** and **3.6.5**

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

## Directories and files description
* [`compute_avg_run_time.py`](https://github.com/raul23/python_reverse_dict/blob/master/compute_avg_run_time.py)
<a id="compute_avg_run_time_description"></a>: it is the **main** script that will build the right `shell`-based python 
command for computing the average run time of a dict-reversing method. It is run by providing it the right [options](#options)
through the command-line.  It will execute either `run_python2_method.py` if the wanted method is Python2-based or
`run_python3_method.py` if the method is Python3-based. It can be called with `python2` or `python3` through the
command-line.   
* [`run_python2_method.py`](https://github.com/raul23/python_reverse_dict/blob/master/run_python2_method.py): gets
executed by `compute_avg_run_time.py`, and calls the right **Python 2** dict-reversing method that is defined in
[`methods.py`](https://github.com/raul23/python_reverse_dict/blob/master/reverse_dict/methods.py).  
* [`run_python3_method.py`](https://github.com/raul23/python_reverse_dict/blob/master/run_python3_method.py): gets
executed by `compute_avg_run_time.py`, and calls the right **Python 3** dict-reversing method that is defined in
[`methods.py`](https://github.com/raul23/python_reverse_dict/blob/master/reverse_dict/methods.py).  
* [`reverse_dict/`](https://github.com/raul23/python_reverse_dict/tree/master/reverse_dict): a package where everything
that is needed to compute the average run time of a method is defined such as the dict-reversing
[methods](https://github.com/raul23/python_reverse_dict/blob/master/reverse_dict/methods.py), and the
[arguments](https://github.com/raul23/python_reverse_dict/blob/master/reverse_dict/arguments.py) accepted by the methods
through the command-line.   

## Installation
To use the **main** Python script
[`compute_avg_run_time.py`](https://github.com/raul23/python_reverse_dict/blob/master/compute_avg_run_time.py):

* Clone the repository and extract it
* You can now run the main script by providing it the right options:  
**`$ python compute_avg_run_time.py [-h] [--version] [OPTIONS]`**  

Go to the section [Usage](#usage) for more details on the script [options](#options) and
[examples of usage](#examples-of-usage).

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

## Usage
`python compute_run_time.py [-h] [--version] [OPTIONS]`

### Options
* **`-h`**, **`--help`**  
  show the help message and exit

* **`-m METHOD_NAME`**, **`--method_name METHOD_NAME`**  
  Name of the method that reverses a dictionary's keys and values:

  `method_01_py2`: **Python 2.7** version of [method 1](#method01)   
  `method_02_py2`: **Python 2.7** version of [method 2](#method02)  
  `method_03_py2`: **Python 2.7** version of [method 3](#method03)  
  `method_01_py3`: **Python 3** version of [method 1](#method01)  
  `method_02_py3`: **Python 3** version of [method 2](#method02)   
  `method_03_py3`: **Python 3** version of [method 3](#method03)   
   (**default**: `method_01_py3`)  

* **`-ui`**, **`--use_items`**  
  When working on Python 2, uses `dict.items()` instead of the more efficient `dict.iteritems()`.  
  (**default**: `False`)  

* **`-usd`**, **`--use_setdefault`**  
  Use `dict.setdefault()` instead of `dict.get()` when populating the dictionary.  
  (**default**: `False`)

* **`-ni NUMBER_ITEMS`**, **`--number_items NUMBER_ITEMS`**  
  Number of items in the dictionary.  
  (**default**: `1000`)

* **`-nt NUMBER_TIMES`**, **`--number_times NUMBER_TIMES`**  
  Number of times the dictionary's keys and values will be reversed. Each time, the run time of the reversal is computed
  and at the end of all the tries, the average run time is computed.  
  (**default**: `10`)

* **`-p PRECISION`**, **`--precision PRECISION`**  
  Decimal precision used when displaying number results.  
  (**default**: `8`)

* **`-pd`**, **`--print_dicts`**  
  Print the original and reversed dictionaries at the end.  
  (**default**: `False`)

* **`-unu`**, **`--use_non_uniques`**  
  Initialize the original dictionary with non-unique values.  
  (**default**: `False`)

* **`-uod`**, **`--use_ordered_dict`**  
  Use `OrderedDict` instead of `dict` for both dictionaries (original and inverse).   
  (**default**: `False`)

* **`-v`**, **`--version`**  
Show program's version and exit.

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

### Examples of usage

#### Example 1: method 1
Try 1000 times the [method 1](#method01) with **Python 2** on 10 items using
`dict.items()`:  
`$ python3 compute_avg_run_time.py -m method_01_py2 -ni 10 -nt 1000 -ui -pd`

**Output**:
```commandline
Method name: method_01_py2
#1 Run time: 0.00001287
#2 Run time: 0.00000787
#3 Run time: 0.00000286
#4 Run time: 0.00000310
#5 Run time: 0.00000310
[...]
#995 Run time: 0.00000286
#996 Run time: 0.00000191
#997 Run time: 0.00000310
#998 Run time: 0.00000286
#999 Run time: 0.00000191
#1000 Run time: 0.00000310
Avg run time: 0.00000289 seconds

Original dict:
{'k10': 'v10', 'k3': 'v3', 'k2': 'v2', 'k1': 'v1', 'k7': 'v7', 'k6': 'v6', 'k5': 'v5', 'k4': 'v4', 'k9': 'v9', 'k8': 'v8'}
Inverse dictionary:
{'v10': 'k10', 'v1': 'k1', 'v2': 'k2', 'v3': 'k3', 'v4': 'k4', 'v5': 'k5', 'v6': 'k6', 'v7': 'k7', 'v8': 'k8', 'v9': 'k9'}
```

**Notes**:
* The main script `compute_avg_run_time.py` was called with `python3` even
though we are executing a **Python2-based** dict-reversing method
(`method_01_py2`). As was [explained](#compute_avg_run_time_description)
previously, `compute_avg_run_time.py`, which can be run with `python2` or
`python3`, executes `run_python2_method.py` (a Python 2 script) which will call
`method_01_py2`.
* From the content of the dictionaries, we see that the order of
insertion was not fully respected (`{'v10': 'k10'}` is at the beginning) as can
be expected since `method_01_py2` is a Python2-based method that is using a
`dict` as the data structure. If an `OrderedDict` would have been used (with the
option `-uod`), then the initial order of insertion would have been maintained
in the dictionaries.

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

#### Example 2: method 2
Try 1000 times the [method 2](#method02) with **Python 3** on 9 items using
`dict.setdefault()`:  
`$ python compute_avg_run_time.py -m method_02_py3 -ni 9 -nt 1000 -usd -pd -unu`

**Output**:
```commandline
Method name: method_02_py3
#1 Run time: 0.00000782
#2 Run time: 0.00000583
#3 Run time: 0.00000477
#4 Run time: 0.00000446
#5 Run time: 0.00000461
[...]
#995 Run time: 0.00000426
#996 Run time: 0.00000430
#997 Run time: 0.00000419
#998 Run time: 0.00000426
#999 Run time: 0.00000421
#1000 Run time: 0.00000428
Avg run time: 0.00000538 seconds

Original dict:
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v1', 'k6': 'v2', 'k7': 'v3', 'k8': 'v4', 'k9': 'v5'}
Inverse dictionary:
{'v1': ['k1', 'k5'], 'v2': ['k2', 'k6'], 'v3': ['k3', 'k7'], 'v4': ['k4', 'k8'], 'v5': ['k9']}
```

**Notes**:
* In my work environment, `python` points to `Python 3.6.5`
* [Method 2](#method02) works also with non-unique values (`-unu`) where keys
having the same values are added to a list in the reversed dictionary.

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

#### Example 3: method 3
Try 100 times the [method 3](#method03) with **Python 3** on 10 items using
`OrderedDict`:  
`$ python compute_avg_run_time.py -m method_03_py3 -ni 10 -nt 1000 -uod -pd`

**Output**:
```commandline
Method name: method_03_py3
#1 Run time: 0.00001224
#2 Run time: 0.00000586
#3 Run time: 0.00000535
#4 Run time: 0.00000493
#5 Run time: 0.00000493
[...]
#995 Run time: 0.00000455
#996 Run time: 0.00000458
#997 Run time: 0.00000461
#998 Run time: 0.00000461
#999 Run time: 0.00000456
#1000 Run time: 0.00000462
Avg run time: 0.00000486 seconds

Original dict:
OrderedDict([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3'), ('k4', 'v4'), ('k5', 'v5'), ('k6', 'v6'), ('k7', 'v7'), ('k8', 'v8'), ('k9', 'v9'), ('k10', 'v10')])
Inverse dictionary:
OrderedDict([('v1', 'k1'), ('v2', 'k2'), ('v3', 'k3'), ('v4', 'k4'), ('v5', 'k5'), ('v6', 'k6'), ('v7', 'k7'), ('v8', 'k8'), ('v9', 'k9'), ('v10', 'k10')])
```

**Note**:
* An `OrderedDict()` is used instead but if a simple `dict` would have been used,
the inverse dictionary would have respected the original insertion order also
since starting from Python 3.6, the insertion order is an implementation detail
(though **not a guarantee** in Python 3.6). However,
[as of Python 3.7](https://stackoverflow.com/a/39980744), you can be guaranteed
that insertion order is supported for `dict`.

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

## Results: Comparaisons between methods
### Major updates  
**2018-09-16:** 
- I updated the [code base](https://github.com/raul23/python_reverse_dict/commit/a163e9df9d5001704c5f2836f1febe4a96e77e0a) 
and re-ran the [python commands](https://github.com/raul23/python_reverse_dict/blob/master/commands.md#commands) to 
re-populate the following [two tables](#table_01) with new results. I factorized 
[methods.py](https://github.com/raul23/python_reverse_dict/blob/master/reverse_dict/methods.py) where the different 
`dict`-reversing methods are defined by putting all the common code from Python 2 & 3 methods into base classes.

- I also implemented the important missing option `--use_setdefault` which I thought was already implemented when I 
generated the [first results](https://github.com/raul23/python_reverse_dict/blob/master/old_results.md). Big mistake on 
my part! Thus the old results for the row **Method 2: setdefault, iteritems()** were generated actually with 
`dict.get()` instead of `dict.setdefault()` :(

<br/>

The following tables present the average run times (in µ seconds) of the different methods of reversing a dictionary. 
As it can be seen, **method 1 is the big winner**, offering the best average run times in Python 2 & 3. More details on 
the results can be found on my blog post 
[Python tips: reverse a dictionary](https://progsharing.blogspot.com/2018/09/python-tips-reverse-dictionary.html#average_running_times).

The python commands for each methods are to be found in [commands.md](https://github.com/raul23/python_reverse_dict/blob/master/commands.md#commands).

### Table 1: Python2-based methods
<div align="center">  
<b>Table 1<b/> Average running times of different methods <br/>
of reversing a <code>dict</code> in <b>Python 2.7</b>
</div>

| Py2 Method | Avg time (µsec),  1k items, 100k times | Avg time (µsec), 10k items, 1k times | Avg time (µsec), 100k items, 1k times |
|:---------------------------------------------:|:-------------------------------------:|:-----------------------------------:|:------------------------------------:|
| [Method 1: `dict` comprehension, `iteritems()`](#python-27-with-dictiteritems) | <h3>217.96</h3> | <h3>2665.56</h3> | <h3>45301.06</h3> |
| [Method 1: `dict` comprehension,  `items()`](#python-27-with-dictitems) | 256.79 | 4125.60 | 70901.29 |
| [Method 2: `dict.get`, `iteritems()`](#python-27-with-dictget) | 838.27 | 10410.03 | 127703 |
| [Method 2: `setdefault`, `iteritems()`](#python-27-with-dictsetdefault) | 656.03 | 8539.27 | 108347.76 |
| <a href="#python-27">Method 3: `map(reversed, iterable)`,  `iteritems()`</a> | 895.95 | 10788.73 | 146115.25 |

### Table 2: Python3-based methods
<div align="center">  
<b>Table 2<b/> Average running times of different methods <br/>
of reversing a <code>dict</code> in <b>Python 3</b>
</div>

| Py3 Method | Avg time (µsec),  1k items, 100k times | Avg time (µsec), 10k items, 1k times | Avg time (µsec), 100k items, 1k times |
|:-----------------------------:|:-------------------------------------:|:-----------------------------------:|:------------------------------------:|
| [Method 1: `dict` comprehension](#python-3) | <h3>89.97</h3> | <h3>905.46</h3> | <h3>18487.63</h3> |
| [Method 2: `dict.get`](#python-3-with-dictget) | 417.17 | 4949.22 | 66599.29 |
| [Method 2: `setdefault`](#python-3-with-dictsetdefault) | 333.02 | 4171.31 | 58628.69 |
| [Method 3: `map(reversed,)`](#python-3-1) | 311.59 | 3366.20 | 46960.80 |

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

## Methods: Python code
### Method 1: unique-values, solution based on `dict`
<a id="python-27-with-dictiteritems"></a>
<div align="center">  
	<b>Method 1: Python 2.7 with <code>dict.iteritems()</code></b>
</div>  

```python
my_dict = { 'a': 1, 'b':2, 'c': 3, 'd':4, 'e':5}
inv_dict = {v: k for k, v in my_dict.iteritems()}
```

<br/>
<a id="python-27-with-dictitems"></a>
<div align="center">  
	<b>Method 1: Python 2.7 with <code>dict.items()</code></b>
</div>  

```python
my_dict = { 'a': 1, 'b':2, 'c': 3, 'd':4, 'e':5}
inv_dict = {v: k for k, v in my_dict.items()}
```

<br/>
<a id="python-3"></a>
<div align="center">  
	<b>Method 1: Python 3</b>
</div>  

```python
my_dict = { 'a': 1, 'b':2, 'c': 3, 'd':4, 'e':5}
inv_dict = {v: k for k, v in my_dict.items()}
```

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

### Method 2: non-unique values
<a id="python-27-with-dictget"></a>
<div align="center">  
	<b>Method 2: Python 2.7 with <code>dict.get()</code></b>
</div>  

```python
my_dict = {1: 'a', 2:'b', 3: 'c', 4: 'a', 5: 'c'}
inv_dict = {}
for k, v in my_dict.iteritems():
    inv_dict[v] = inv_dict.get(v, [])
    inv_dict[v].append(k)
```

<br/>
<a id="python-3-with-dictget"></a>
<div align="center">  
	<b>Method 2: Python 3 with <code>dict.get()</code></b>
</div>  

```python
from collections import OrderedDict

def reverse_dict(orig_dict):
    inv_dict = {}
    for k, v in orig_dict.items():
        inv_dict[v] = inv_dict.get(v, [])
        inv_dict[v].append(k)

my_dict = OrderedDict({1: 'a', 2:'b', 3: 'c', 4: 'a', 5: 'c'})
reverse_dict(my_dict)
```

<br/>
<a id="python-27-with-dictsetdefault"></a>
<div align="center">  
	<b>Method 2: Python 2.7 with <code>dict.setdefault()</code></b>
</div>  

```python
my_dict = {1: 'a', 2:'b', 3: 'c', 4: 'a', 5: 'c'}
inv_dict = {}
for key, value in my_dict.iteritems():
    inv_dict.setdefault(value, []).append(key)
```

<br/>
<a id="python-3-with-dictsetdefault"></a>
<div align="center">  
	<b>Method 2: Python 3 with <code>dict.setdefault()</code></b>
</div>  

```python
my_dict = {1: 'a', 2:'b', 3: 'c', 4: 'a', 5: 'c'}
inv_dict = {}
for key, value in my_dict.items():
    inv_dict.setdefault(value, []).append(key)
```

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

### Method 3: type and order preserved 
<a id="python-27"></a>
<div align="center">  
<b>Method 3: Python 2.7</b>
</div>  

```python
def reverse_mapping(f):
    return f.__class__(map(reversed, f.iteritems()))

my_dict = {1: 'a', 2:'b', 3: 'c', 4: 'd', 5: 'e'}
inv_dict = reverse_mapping(my_dict)
```

<br/>
<a id="python-3-1"></a>
<div align="center">  
<b>Method 3: Python 3</b>
</div>  

```python
def reverse_mapping(f):
    return f.__class__(map(reversed, f.items()))

my_dict = {1: 'a', 2:'b', 3: 'c', 4: 'd', 5: 'e'}
inv_dict = reverse_mapping(my_dict)
``` 

## References

* [Method 1 code](https://stackoverflow.com/a/483833)
* [Method 2 code with `dict.get()`](https://stackoverflow.com/a/485368)
* [Method 2 code with `dict.setdefault()`](https://stackoverflow.com/a/13057382)
* [Method 3 code](https://stackoverflow.com/a/1679702)

## License

The code is licensed under the MIT license. See the
[license](https://github.com/raul23/python_reverse_dict/blob/master/LICENSE) for more details.

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>
