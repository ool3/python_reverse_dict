# python_reverse_dict
<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Introduction](#introduction)
- [Directories and files description](#directories-and-files-description)
- [Installation](#installation)
- [Usage](#usage)
	- [Options](#options)
	- [Examples of usage](#examples-of-usage)
- [Results](#results)

<!-- /TOC -->
## Introduction
Computes average run times of different methods of reversing a dictionary's keys and values in **Python 2.7 &amp; 3**:
* **method 1**: makes use of dictionary comprehension, and the dictionary must contain unique values
* **method 2**: the dictionary doesn't contain unique values and saves all the keys with the same values in a list
* **method 3**: makes use of `map(reversed,)`, useful when the type and order of the original dictionary must be preserved (e.g. `OrderedDict`)


<p align="right"> <a href="#python_reverse_dict"> ^top </a> </p>

## Directories and files description
* [`compute_avg_run_time.py`](https://github.com/raul23/python_reverse_dict/blob/master/compute_avg_run_time.py): it is the **main** script that will build the right `shell` command for computing the average run time of a dict-reversing method. It is run by providing it the right [options](#options) through the command-line.  It will call either `run_python2_method.py` if the wanted method is Python2-based or `run_python3_method.py` if the method is Python3-based. It can be called with `python2` or `python3` through the command-line.   
* [`run_python2_method.py`](https://github.com/raul23/python_reverse_dict/blob/master/run_python2_method.py): gets executed by `compute_avg_run_time.py`, and calls the right **Python 2** dict-reversing method that is defined in [`methods.py`](https://github.com/raul23/python_reverse_dict/blob/master/reverse_dict/methods.py).  
* [`run_python3_method.py`](https://github.com/raul23/python_reverse_dict/blob/master/run_python3_method.py): gets executed by `compute_avg_run_time.py`, and calls the right **Python 3** dict-reversing method that is defined in [`methods.py`](https://github.com/raul23/python_reverse_dict/blob/master/reverse_dict/methods.py).  
* [`reverse_dict/`](https://github.com/raul23/python_reverse_dict/tree/master/reverse_dict): a package where everything that is needed to compute the average run time of a method is defined such as the dict-reversing [methods](https://github.com/raul23/python_reverse_dict/blob/master/reverse_dict/methods.py), and the [arguments](https://github.com/raul23/python_reverse_dict/blob/master/reverse_dict/arguments.py) accepted by the methods through the command-line.   

<p align="right"> <a href="#python_reverse_dict"> ^top </a> </p>

## Installation
To use the **main** Python script [`compute_avg_run_time.py`](https://github.com/raul23/python_reverse_dict/blob/master/compute_avg_run_time.py):

* Clone the repository and extract it
* Change permission to the two files [`run_python2_method.py`](https://github.com/raul23/python_reverse_dict/blob/master/run_python3_method.py) and [`run_python3_method.py`](https://github.com/raul23/python_reverse_dict/blob/master/run_python2_method.py) so they can be executed by `compute_avg_run_time.py`:  
**`$ chmod 744 run_python*`**
* You can now run the main script by providing it the right options:  
**`$ python compute_avg_run_time.py [-h] [--version] [OPTIONS]`**  

Go to the section [Usage](#usage) for more details on the script [options](#options) and [examples of usage](#examples-of-usage).

<p align="right"> <a href="#python_reverse_dict"> ^top </a> </p>

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
  Number of times the dictionary's keys and values will be reversed. Each time, the run time of the reversal is computed and at the end of all the tries, the average run time is computed.

* **`-p PRECISION`**, **`--precision PRECISION`**  
  Decimal precision used when displaying number results.

### Examples of usage

<div align="right"> <a href="#python_reverse_dict"> ^top </a> </div>

## Results
