# parallel-execute
python wrappers for easy multiprocessing and threading



#### Usage:

```.env python
# To use threading
from parallel.thread import ThreadLoom
```

```.env python
# To use multiprocessing
from parallel.process import ProcessLoom
```
##### 1. Create Loom object
This takes a number of tasks and executes them using a pool of threads/process.
```
# Provide max_runner_cap
loom = ThreadLoom(max_runner_cap=20)
```

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

This does not support timeouts, so all runners must complete.  To handle
timeouts, each runner would have to keep track of its own timeout time,
and throw an exception to signal an error to the Loom

