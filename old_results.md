**IMPORTANT:** The rows [Method 2: `setdefault`, `iteritems()`](#python-27-with-dictsetdefault) in **Table 1** and 
[Method 2: `setdefault`](#python-3-with-dictsetdefault) in **Table 2** were obtained actually with `dict.get()` instead of `dict.setdefault()`. 
As stated on the [2018-09-16 update](https://github.com/raul23/python_reverse_dict#major-updates), I thought the 
`--use_setdefault` option was implemented when I ran the main script 
[`compute_avg_run_time.py`](https://github.com/raul23/python_reverse_dict/blob/master/compute_avg_run_time.py) which was not 
the case. `dict.get()` was used instead of `dict.setdefault()`. Check the 
[newest results](https://github.com/raul23/python_reverse_dict#table-1-python2-based-methods) where I re-ran the 
[python commands](https://github.com/raul23/python_reverse_dict/blob/master/commands.md#commands) with the updated code. 

The following two tables present average run times that were obtained with 
[python scripts](https://github.com/raul23/python_reverse_dict/commit/c834169f4b7f74f21e3fe3006483baa44f83ef91) having 
*commit HASH* **c834169f4b7f74f21e3fe3006483baa44f83ef91**. 

<br/>

<div align="center">  
<b>Table 1<b/> Average running times of different methods <br/>
of reversing a <code>dict</code> in <b>Python 2.7</b>
</div>

| Py2 Method | Avg time (µsec),  1k items, 100k times | Avg time (µsec), 10k items, 1k times | Avg time (µsec), 100k items, 1k times |
|:---------------------------------------------:|:-------------------------------------:|:-----------------------------------:|:------------------------------------:|
| Method 1: `dict` comprehension, `iteritems()` | <h3>233.02</h3> | <h3>3009.04</h3> | <h3>45815.60</h3> |
| Method 1: `dict` comprehension,  `items()` | 273.22 | 4484.39 | 73327.81 |
| Method 2: `dict.get`, `iteritems()` | 772.42 | 10035.83 | 125039.90 |
| <a id="python-27-with-dictsetdefault"></a>Method 2: `setdefault`, `iteritems()` | 910.63 | 11369.59 | 131220.12 |
| Method 3: `map(reversed, iterable)`,  `iteritems()` | 856.57 | 10712.58 | 121904.58 |

<br/>
<br/>

<div align="center">  
<b>Table 2<b/> Average running times of different methods <br/>
of reversing a <code>dict</code> in <b>Python 3</b>
</div>

| Py3 Method | Avg time (µsec),  1k items, 100k times | Avg time (µsec), 10k items, 1k times | Avg time (µsec), 100k items, 1k times |
|:-----------------------------:|:-------------------------------------:|:-----------------------------------:|:------------------------------------:|
| Method 1: `dict` comprehension | <h3>96.81</h3> | <h3>946.01</h3> | <h3>20405.42</h3> |
| Method 2: `dict.get` | 373.60 | 4287.52 | 63150.73 |
| <a id="python-3-with-dictsetdefault"></a>Method 2: `setdefault` | 372.67 | 4321.50 | 63432.81 |
| Method 3: `map(reversed,)` | 312.13 | 3190.19 | 45776.68 |
