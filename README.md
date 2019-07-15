Python practise
===

* be operationally fluent in Python, including the use and design of 'functions' and 'classes'
* and comfortable using standard numerical libraries such as 'NumPy', 'SciPy', and 'Pandas'. 
* Additionally, familiarity with basic concepts in algorithm design (for example, 'time and memory complexity'), 'machine learning' (classification, regression, and clustering), and 'statistics' is useful.
* matplotlib

## Object-Oriented Programming and Functional Programming

## Random walk

## numpy
> [Quickstart Tutorial by numpy.org](https://www.numpy.org/devdocs/user/quickstart.html)<br>
> About axis = 0 and 1: <br> axis = 0 对一行中的每一列进行操作 <br>  axis = 1 对一列中的每一行进行操作 <br>


### Stacking together different arrays

* hstack
```python
import numpy as np
from numpy import newaxis

a=np.array([4.,7.])
b=np.array([2.,8.])
print(a,b)
c = a[:, newaxis]
d = b[:, newaxis]
print(c)

e = np.column_stack((a,b))
f = np.column_stack((c,d))
print(e,'\n\n',f)
```
* vstack

* column_stack

* row_stack

* concatenate

* c_

* r_

## pandas
