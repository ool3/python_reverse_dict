**IMPORTANT:** The results for the row [Method 2: setdefault, iteritems()](#python-27-with-dictsetdefault) was 
done actually with `dict.get()` instead of `dict.setdefault()`. As stated on [2018-09-16 Update](), I thought the 
`--use_setdefault` option was implemented when I ran the main script `compute_avg_run_time.py` which was not the case.
`dict.get()` was used instead of `dict.setdefault()`. Check the [newest results]() where I re-ran the [shell commands](). 

The following two tables present average run times that were obtained with [python scripts](https://github.com/raul23/python_reverse_dict/commit/c834169f4b7f74f21e3fe3006483baa44f83ef91) having *commit HASH* 
**c834169f4b7f74f21e3fe3006483baa44f83ef91**. 

<br/>

<div align="center">  
<b>Table 1<b/> Average running times of different methods <br/>
of reversing a <code>dict</code> in <b>Python 2.7</b>
</div>

| Py2 Method | Avg time (µsec),  1k items, 100k times | Avg time (µsec), 10k items, 1k times | Avg time (µsec), 100k items, 1k times |
|:---------------------------------------------:|:-------------------------------------:|:-----------------------------------:|:------------------------------------:|
| [Method 1: `dict` comprehension, `iteritems()`](#python-27-with-dictiteritems) | <h3>233.02</h3> | <h3>3009.04</h3> | <h3>45815.60</h3> |
| [Method 1: `dict` comprehension,  `items()`](#python-27-with-dictitems) | 273.22 | 4484.39 | 73327.81 |
| [Method 2: `dict.get`, `iteritems()`](#python-27-with-dictget) | 772.42 | 10035.83 | 125039.90 |
| [Method 2: `setdefault`, `iteritems()`](#python-27-with-dictsetdefault) | 910.63 | 11369.59 | 131220.12 |
| <a href="#python-27">Method 3: `map(reversed, iterable)`,  `iteritems()`</a> | 856.57 | 10712.58 | 121904.58 |

<br/>
<br/>

<div align="center">  
<b>Table 2<b/> Average running times of different methods <br/>
of reversing a <code>dict</code> in <b>Python 3</b>
</div>

| Py3 Method | Avg time (µsec),  1k items, 100k times | Avg time (µsec), 10k items, 1k times | Avg time (µsec), 100k items, 1k times |
|:-----------------------------:|:-------------------------------------:|:-----------------------------------:|:------------------------------------:|
| [Method 1: `dict` comprehension](#python-3) | <h3>96.81</h3> | <h3>946.01</h3> | <h3>20405.42</h3> |
| [Method 2: `dict.get`](#python-3-with-dictget) | 373.60 | 4287.52 | 63150.73 |
| [Method 2: `setdefault`](#python-3-with-dictsetdefault) | 372.67 | 4321.50 | 63432.81 |
| [Method 3: `map(reversed,)`](#python-3-1) | 312.13 | 3190.19 | 45776.68 |
