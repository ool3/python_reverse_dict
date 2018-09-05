0# Commands
<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Python 3](#python-3)
	- [Method 1: Py3, dict comprehension](#method-1-py3-dict-comprehension)
	- [Method 2: Py3, dict.get](#method-2-py3-dictget)
	- [Method 2: Py3, setdefault](#method-2-py3-setdefault)
	- [Method 3: Py3, map(reversed, iterable)](#method-3-py3-mapreversed-iterable)
- [Python 2](#python-2)
	- [Method 1: Py2, dict comprehension, iteritems](#method-1-py2-dict-comprehension-iteritems)
	- [Method 1: Py2, dict comprehension, items](#method-1-py2-dict-comprehension-items)
	- [Method 2: Py2, dict.get, iteritems](#method-2-py2-dictget-iteritems)
	- [Method 2: Py2, setdefault, iteritems](#method-2-py2-setdefault-iteritems)
	- [Method 3: Py2, map(reversed, iterable), iteritems](#method-3-py2-mapreversed-iterable-iteritems)

<!-- /TOC -->
## Python 3
### Method 1: Py3, dict comprehension
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_01_py3 -ni 1000 -nt 100000`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_01_py3 -ni 10000 -nt 1000`  

**100k items, 1k times**:  
`python compute_avg_run_time.py -m method_01_py3 -ni 100000 -nt 1000`  

### Method 2: Py3, dict.get
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_02_py3 -ni 1000 -nt 100000 -unu`  

**10k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py3 -ni 10000 -nt 1000 -unu`  

**100k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py3 -ni 100000 -nt 1000 -unu`    

### Method 2: Py3, setdefault  
**1k items, 100k times**:   
`python compute_avg_run_time.py  -m method_02_py3 -ni 1000 -nt 100000 -unu -usd`    

**10k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py3 -ni 10000 -nt 1000 -unu -usd`    

**100k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py3 -ni 100000 -nt 1000 -unu -usd`      

### Method 3: Py3, map(reversed, iterable)  
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_03_py3 -ni 1000 -nt 100000`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_03_py3 -ni 10000 -nt 1000`    

**100k items, 1k times**:  
`python compute_avg_run_time.py -m method_03_py3 -ni 100000 -nt 1000`  

## Python 2
### Method 1: Py2, dict comprehension, iteritems
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_01_py2 -ni 1000 -nt 100000`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_01_py2 -ni 10000 -nt 1000`  

**100k items, 1k times**:  
`python compute_avg_run_time.py -m method_01_py2 -ni 100000 -nt 1000`  

### Method 1: Py2, dict comprehension, items
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_01_py2 -ni 1000 -nt 100000 -ui`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_01_py2 -ni 10000 -nt 1000 -ui`    

**100k items, 1k times**:     
`python compute_avg_run_time.py -m method_01_py2 -ni 100000 -nt 1000 -ui`    

### Method 2: Py2, dict.get, iteritems
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_02_py2 -ni 1000 -nt 100000 -unu`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_02_py2 -ni 10000 -nt 1000 -unu`  

**100k items, 1k times**:  
`python compute_avg_run_time.py -m method_02_py2 -ni 100000 -nt 1000 -unu`  

### Method 2: Py2, setdefault, iteritems
**1k items, 100k times**:  
`python compute_avg_run_time.py  -m method_02_py2 -ni 1000 -nt 100000 -unu -usd`  

**10k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py2 -ni 10000 -nt 1000 -unu -usd`  

**100k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py2 -ni 100000 -nt 1000 -unu -usd`  

### Method 3: Py2, map(reversed, iterable), iteritems
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_03_py2 -ni 1000 -nt 100000`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_03_py2 -ni 10000 -nt 1000`  

**100k items, 1k times**:  
`python compute_avg_run_time.py -m method_03_py2 -ni 100000 -nt 1000`  
