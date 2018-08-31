# python_reverse_dict
Computes average running times of different methods of reversing a `dict`'s keys and values in **Python 2.7 &amp; 3**:
* **method 1**: makes use of `dict` comprehension, and your `dict` must contain unique values
* **method 2**: makes use of `dict.get()`, and your `dict` doesn't contain unique values
* **method 3**: makes use of `map(reversed,)`

## Usage
`compute_running_times.py [-h] [--version] [OPTIONS]`

## Options
* `-h`, `--help`  
  show this help message and exit

* `-m METHOD_NAME`, `--method_name METHOD_NAME`   
  Name of the method that reverses a `dict`'s keys and values:

  `method_01_py2`: makes use of `dict` comprehension, and the `dict` must contain
                   unique values. Works on **Python 2.7**  
  `method_01_py2`: makes use of `dict.get()`, and the `dict` doesn't contain
                   unique values. Works on **Python 2.7**  
  `method_01_py2`: makes use of `map(reversed,)`, and the type and order of the original dict are  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preserved (if for example it is an `OrderedDict`). Works on **Python 2.7**  

  `method_01_py3`: **Python 3** version of `method-01-py2`  
  `method_01_py3`: **Python 3** version of `method-02-py3`  
  `method_01_py3`: **Python 3** version of `method-03-py2`  

* `-ui`, `--use_items`  
  When working on Python 2, use `dict.items()` instead of the more efficient `dict.iteritems()`.

* `-usd`, `--use_setdefault`  
  Use `dict.setdefault()` instead of `dict.get()` when populating the dictionary.

* `-s`, `--small_test`            
  Use a small dictionary with few items which the keys and values will be reversed.

* `-i NUMBER_ITEMS`, `--number_items NUMBER_ITEMS`  
  Number of items in the dictionary.

* `-n NUMBER_TIMES`, `--number_times NUMBER_TIMES`  
  Number of times the dictionary's keys and values will be reversed.

* `-p PRECISION`, `--precision PRECISION`  
  Decimal precision used when displaying number results.

## Examples
