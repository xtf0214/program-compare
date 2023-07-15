# program-compare-UI

A program-comparer Based on PyQt5.

## Usage

![](img/GUI.png)

### prepare `setData.py`

`writeln` Pass in a list and write it on one line.

```python
from random import randint


def randPair(a, b):
    l = randint(a, b)
    r = randint(a, b)
    return (l, r) if l < r else (r, l)


def setData(writeln, id=1):
    a = randint(1, 2e9)
    b = randint(1, 2e9)
    writeln([a, b])
```

# program-compare

This is a program-comparer for programming competition. It's base on `cyaron`, but some simple encapsulation was made.

## Usage

1. Copy `ProgramCompare.py` to you workspace.
2. New a python file and write `from ProgramCompare import *`
3. New a `ProgramCompare` class and appoint the `std_cpp` path and the `cmp_cpp` path.
4. Write the `setData` methods, it is a function object for making data according to the problem.

### compare

`compare` using `os.popen()` to get the output from two exe files and comparing the text of two.
* set `show_input = False` , `show_output = False`
![](img/compare.png)		

* set `show_input = True` , `show_output = True`
![](img/show_data.png)

### makeData

If you only want to gain `test.in` and `test.out` as data from `std_exe`, you can use `makeData`.

```python
######## make data
compare.makeData(1e1)
compare.makeData(1e2)
compare.makeData(1e3)
compare.makeData(1e4)
compare.makeData(1e5)
```

### lower_bound

If there is a boundary, an error will occur when the data is greater than it, and no error will occur when it is not greater than it. You can use `lower_bound` to find this boundary
![](img/lower_bound.png)

### run

If you want to make many tests at a time, try `run`.

### clear

Finally, to clear the temporary file, `clear`!
