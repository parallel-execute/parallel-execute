# parallel-execute
Python wrappers for easy multiprocessing and threading

Run multiple functions in parallel using threading or multiprocessing

![GitHub](https://img.shields.io/github/license/parallel-execute/parallel-execute.svg)

## Installation
```
pip install parallel-execute
```

## Usage Example

##### 1. Create a loom object:
This takes a number of tasks and executes them using a pool of threads/process.


```.env python
# To use threading
from parallel.thread import ThreadLoom
loom = ThreadLoom(max_runner_cap=10)
```

```.env python
# To use multiprocessing
from parallel.process import ProcessLoom
loom = ProcessLoom(max_runner_cap=10)
```

max_runner_cap: is the number of maximum threads/processes to run at a time.
You can add as many as functions you want, but only `n` functions will run at a time in parallel, `n` is the max_runner_cap

##### 2. Add tasks in loom
Use `add_func(func, arg1, arg2, ..., kwarg1=foo, kwarg2=bar, ...)` or `add_function(func, arglist, kwargdict)` to add a single function to be done.
```.env python
loom.add_function(f1, args1, kw1)
loom.add_function(f2, args2, kw2)
loom.add_function(f3, args3, kw3)
```
##### 3. Add multiple tasks together
Use `add_work([f1, a1, kw1), (f2, a2, kw2), ...])` to add a list of functions and kwargs.
```.env python
work = [(f1, args1, kwargs1), (f2, args2, kwargs2), (f3, args3, kwargs3)]
loom.add_work(work)
```
##### 4. Execute all tasks
After adding tasks, calling execute will return a dictionary of results corresponding to the 
keys or the order in which the tasks were added.
```
output = loom.execute()
```
output is a dictionary of results corresponding to function, key is the index/order in which the function was added and value is the return data of the function.

```
# Example:

def fun1():
   return "Hello World"
  
def fun2(a):
   return a

def fun3(a, b=0)
   return f"a={a}, b={b}"


loom = ThreadLoom(max_runner_cap=10)
loom.add_function(fun1, [], {})
loom.add_function(fun2, [1], {})
loom.add_function(fun3, [1], {'b': 3})

output = loom.execute()
>>> output
{1: 'Hello World', 2: 1, 3: 'a=1, b=3'}

```
While adding functions, we can provide a `key` to store the function return data.
example:
```
loom = ThreadLoom(3)
loom.add_function(fun1, [], {}, 'key1')
loom.add_function(fun2, [1], {}, 'fun2')
loom.add_function(fun3, [1], {'b': 3}, 'c')

output = loom.execute()
>>> output
{'key1': 'Hello World', 'fun2': 1, 'c': 'a=1, b=3'}
```
