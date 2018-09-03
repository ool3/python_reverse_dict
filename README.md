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
- [Comparaisons between methods](#comparaisons-between-methods)
- [License](#license)

<!-- /TOC -->
## Introduction
Computes average run times of different methods of reversing a dictionary's keys
and values in **Python 2.7 &amp; 3**:
* **method 1**<a id="method01"></a>: makes use of dictionary comprehension, and
the dictionary must contain unique values
* **method 2**<a id="method02"></a>: the dictionary doesn't contain unique
values and saves all the keys with the same values in a list
* **method 3**<a id="method03"></a>: makes use of `map(reversed,)`, useful when
the type and order of the original dictionary must be preserved (e.g.
`OrderedDict`)

I ran some tests, and method 2 is the one that provides the best average run
for reversing the keys and values of a dictionary. See section [Comparaisons
between different methods](#comparaisons-between-different-methods) for the
average run times of the different methods based on the number of items.

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

## Directories and files description
* [`compute_avg_run_time.py`](https://github.com/raul23/python_reverse_dict/blob/master/compute_avg_run_time.py)
<a id="compute_avg_run_time_description"></a>: it is the **main** script that will build the right `shell` command for
computing the average run time of a dict-reversing method. It is run by providing it the right [options](#options)
through the command-line.  It will call either `run_python2_method.py` if the wanted method is Python2-based or
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

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

## Installation
To use the **main** Python script
[`compute_avg_run_time.py`](https://github.com/raul23/python_reverse_dict/blob/master/compute_avg_run_time.py):

* Clone the repository and extract it
* Change permission to the two files
[`run_python2_method.py`](https://github.com/raul23/python_reverse_dict/blob/master/run_python3_method.py) and
[`run_python3_method.py`](https://github.com/raul23/python_reverse_dict/blob/master/run_python2_method.py) so they can
be executed by `compute_avg_run_time.py`:  
**`$ chmod 744 run_python*`**
* You can now run the main script by providing it the right options:  
**`$ python compute_avg_run_time.py [-h] [--version] [OPTIONS]`**  

Go to the section [Usage](#usage) for more details on the script [options](#options) and
[examples of usage](#examples-of-usage).

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

## Usage
`compute_run_time.py [-h] [--version] [OPTIONS]`

### Options
* **`-h`**, **`--help`**  
  show the help message and exit

* **`-m METHOD_NAME`**, **`--method_name METHOD_NAME`**   
  Name of the method that reverses a dictionary's keys and values:

  `method_01_py2`: makes use of dictionary comprehension, and the dictionary must contain
                   unique values.  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Works on **Python 2.7**  
  `method_02_py2`: makes use of `dict.get()`, and the dictionary doesn't contain
                   unique values.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Works on **Python 2.7**    
  `method_03_py2`: makes use of `map(reversed,)`, and the type and order of the original dictionary are  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preserved (if for example it is an `OrderedDict`). Works on **Python 2.7**  
  `method_01_py3`: **Python 3** version of `method_01_py2`  
  `method_02_py3`: **Python 3** version of `method_02_py3`  
  `method_03_py3`: **Python 3** version of `method_03_py2`  

* **`-ui`**, **`--use_items`**  
  When working on Python 2, uses `dict.items()` instead of the more efficient `dict.iteritems()`.

* **`-usd`**, **`--use_setdefault`**  
  Uses `dict.setdefault()` instead of `dict.get()` when populating the dictionary.

* **`-ni NUMBER_ITEMS`**, **`--number_items NUMBER_ITEMS`**  
  Number of items in the dictionary.

* **`-nt NUMBER_TIMES`**, **`--number_times NUMBER_TIMES`**  
  Number of times the dictionary's keys and values will be reversed. Each time, the run time of the reversal is computed
  and at the end of all the tries, the average run time is computed.

* **`-p PRECISION`**, **`--precision PRECISION`**  
  Decimal precision used when displaying number results.

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

### Examples of usage

#### Example 1: method 1
Try [method 1](#method01) with **Python 2** on 10 items using `dict.items()`:  
`$ python3 compute_avg_run_time.py -m method_01_py2 -ni 10 -nt 5 -p 8 -ui -pd`

**Output**:
```commandline
Method name: method_01_py2
#1 Run time: 0.00000501
#2 Run time: 0.00000501
#3 Run time: 0.00000501
#4 Run time: 0.00000405
#5 Run time: 0.00000381
Avg run time: 0.00000458 seconds

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
`python3`, calls `run_python2_method.py` (a Python 2 script) which will run the
`method_01_py2` method.
* From the content of the reversed dictionary, we see that the order of
insertion was not fully respected (`{'v10': 'k10'}` is at the beginning) as can
be expected since `method_01_py2` is a Python2-based method.
* `-p 8` will display the results with 8 decimals

#### Example 2: method 2
Try [method 2](#method02) with Python 3 on 9 items using `dict.setdefault()`:  
`$ python compute_avg_run_time.py -m method_02_py3 -ni 9 -nt 5 -p 8 -usd -pd`

**Output**:
```commandline
Method name: method_02_py3
#1 Run time: 0.00000779
#2 Run time: 0.00000531
#3 Run time: 0.00000480
#4 Run time: 0.00000448
#5 Run time: 0.00000454
Avg run time: 0.00000538 seconds

Original dict:
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v5', 'k6': 'v6', 'k7': 'v7', 'k8': 'v8', 'k9': 'v9'}
Inverse dictionary:
{'v1': ['k1'], 'v2': ['k2'], 'v3': ['k3'], 'v4': ['k4'], 'v5': ['k5'], 'v6': ['k6'], 'v7': ['k7'], 'v8': ['k8'], 'v9': ['k9']}
```

**Note**: In my work environment, `python` points to `Python 3.6.5`

#### Example 3: method 3
Try [method 3](#method03) with Python 3 on 10 items using `OrderedDict`:  
`$ python compute_avg_run_time.py -m method_03_py3 -ni 10 -nt 5 -p 8 -uod -pd`

**Output**:
```commandline
Method name: method_03_py3
#1 Run time: 0.00001193
#2 Run time: 0.00000622
#3 Run time: 0.00000565
#4 Run time: 0.00000503
#5 Run time: 0.00000519
Avg run time: 0.00000681 seconds

Original dict:
OrderedDict([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3'), ('k4', 'v4'), ('k5', 'v5'), ('k6', 'v6'), ('k7', 'v7'), ('k8', 'v8'), ('k9', 'v9'), ('k10', 'v10')])
Inverse dictionary:
OrderedDict([('v1', 'k1'), ('v2', 'k2'), ('v3', 'k3'), ('v4', 'k4'), ('v5', 'k5'), ('v6', 'k6'), ('v7', 'k7'), ('v8', 'k8'), ('v9', 'k9'), ('v10', 'k10')])
```

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

## Comparaisons between methods

test
<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

## License

The code is licensed under the MIT license. See the
[license](https://github.com/raul23/python_reverse_dict/blob/master/LICENSE) for more details.

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>
