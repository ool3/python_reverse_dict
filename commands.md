# Commands

## Python 3
### Method 1: Py3, dict comprehension
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_01_py3 -ni 1000 -nt 100000 -p 8`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_01_py3 -ni 10000 -nt 1000 -p 8`  

**100k items, 1k times**:  
`python compute_avg_run_time.py -m method_01_py3 -ni 100000 -nt 1000 -p 8`  

### Method 2: Py3, dict.get
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_02_py3 -ni 1000 -nt 100000 -p 8 -unu`  

**10k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py3 -ni 10000 -nt 1000 -p 8 -unu`  

**100k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py3 -ni 100000 -nt 1000 -p 8 -unu`    

### Method 2: Py3, setdefault  
**1k items, 100k times**:   
`python compute_avg_run_time.py  -m method_02_py3 -ni 1000 -nt 100000 -p 8 -unu -usd`    

**10k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py3 -ni 10000 -nt 1000 -p 8 -unu -usd`    
  
**100k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py3 -ni 100000 -nt 1000 -p 8 -unu -usd`      

### Method 3: Py3, map(reversed,)  
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_03_py3 -ni 1000 -nt 100000 -p 8`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_03_py3 -ni 10000 -nt 1000 -p 8`    

**100k items, 1k times**:  
`python compute_avg_run_time.py -m method_03_py3 -ni 100000 -nt 1000 -p 8`  

## Python 2
### Method 1: Py2, dict comprehension, iteritems
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_01_py2 -ni 1000 -nt 100000 -p 8`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_01_py2 -ni 10000 -nt 1000 -p 8`  

**100k items, 1k times**:  
`python compute_avg_run_time.py -m method_01_py2 -ni 100000 -nt 1000 -p 8`  

### Method 1: Py2, dict comprehension, items
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_01_py2 -ni 1000 -nt 100000 -p 8 -ui`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_01_py2 -ni 10000 -nt 1000 -p 8 -ui`    

**100k items, 1k times**:     
`python compute_avg_run_time.py -m method_01_py2 -ni 100000 -nt 1000 -p 8 -ui`    

### Method 2: Py2, dict.get, iteritems
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_02_py2 -ni 1000 -nt 100000 -p 8 -unu`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_02_py2 -ni 10000 -nt 1000 -p 8 -unu`  

**100k items, 1k times**:  
`python compute_avg_run_time.py -m method_02_py2 -ni 100000 -nt 1000 -p 8 -unu`  

### Method 2: Py2, setdefault, iteritems
**1k items, 100k times**:  
`python compute_avg_run_time.py  -m method_02_py2 -ni 1000 -nt 100000 -p 8 -unu -usd`  

**10k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py2 -ni 10000 -nt 1000 -p 8 -unu -usd`  

**100k items, 1k times**:  
`python compute_avg_run_time.py  -m method_02_py2 -ni 100000 -nt 1000 -p 8 -unu -usd`  

### Method 3: Py2, map(reversed,), iteritems
**1k items, 100k times**:  
`python compute_avg_run_time.py -m method_03_py2 -ni 1000 -nt 100000 -p 8`  

**10k items, 1k times**:  
`python compute_avg_run_time.py -m method_03_py2 -ni 10000 -nt 1000 -p 8`  

**100k items, 1k times**:  
`python compute_avg_run_time.py -m method_03_py2 -ni 100000 -nt 1000 -p 8`  
