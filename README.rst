parallel-execute
================

Lightweight Python wrappers for easy multiprocessing and multithreading.

Run multiple functions in parallel using a simple API built on top of `threading` or `multiprocessing`. Supports error handling, result tracking, timeouts, and controlled concurrency.

.. image:: https://static.pepy.tech/badge/parallel-execute
   :target: https://pepy.tech/projects/parallel-execute
   :alt: PyPI Downloads

.. image:: https://img.shields.io/github/license/parallel-execute/parallel-execute.svg
   :target: https://github.com/parallel-execute/parallel-execute/blob/master/LICENSE
   :alt: License

.. image:: https://readthedocs.org/projects/parallel-ssh/badge/?version=latest
   :target: http://parallel-execute.readthedocs.org/en/latest/
   :alt: Docs

.. image:: https://img.shields.io/pypi/v/parallel-execute.svg?color=yellow
   :target: https://pypi.org/project/parallel-execute/
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/wheel/parallel-execute.svg
   :target: https://pypi.org/project/parallel-execute/
   :alt: PyPI wheel

.. image:: https://img.shields.io/pypi/pyversions/parallel-execute.svg
   :alt: Python versions

Installation
============

Install the package using pip:

.. code-block:: bash

    pip install parallel-execute

Usage Example
=============

1. Create a Loom
----------------

A **Loom** takes multiple tasks (functions) and executes them in parallel using either threads or processes.

**Using Threads:**

.. code-block:: python

    from pexecute.thread import ThreadLoom
    loom = ThreadLoom(max_runner_cap=10)

**Using Processes:**

.. code-block:: python

    from pexecute.process import ProcessLoom
    loom = ProcessLoom(max_runner_cap=10)

- **max_runner_cap**: The maximum number of threads/processes to run in parallel.
  You can queue as many functions as needed; only ``max_runner_cap`` will run at the same time.

2. Add Tasks to the Loom
-------------------------

**Add a Single Task:**

Use ``add_function`` to add individual functions:

.. code-block:: python

    loom.add_function(f1, args1, kw1)
    loom.add_function(f2, args2, kw2)
    loom.add_function(f3, args3, kw3)

**Add Multiple Tasks at Once:**

Use ``add_work`` to add a batch of functions:

.. code-block:: python

    work = [(f1, args1, kwargs1), (f2, args2, kwargs2), (f3, args3, kwargs3)]
    loom.add_work(work)

3. Execute Tasks
----------------

Once all tasks are added, call ``execute()`` to run them.
It returns a dictionary mapping each task to its result.

.. code-block:: python

    output = loom.execute()

By default, the keys are integers in the order the functions were added. Each value is a dictionary containing the result and execution metadata.

**Example:**

.. code-block:: python

    def fun1():
        return "Hello World"

    def fun2(a):
        return a

    def fun3(a, b=0):
        return a + b

    loom.add_function(fun1, [], {})
    loom.add_function(fun2, [1], {})
    loom.add_function(fun3, [1], {'b': 3})

    output = loom.execute()

.. code-block:: python

    >>> output
    {
      0: {
          'output': 'Hello World',
          'got_error': False,
          'error': None,
          'started_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 395002),
          'finished_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 396500),
          'execution_time': 0.001498,
         },
      1: {
          'output': 1,
          'got_error': False,
          'error': None,
          'started_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 396590),
          'finished_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 397651),
          'execution_time': 0.001061
         },
      2: {
          'output': 4,
          'got_error': False,
          'error': None,
          'started_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 400323),
          'finished_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 401749),
          'execution_time': 0.001426
         }
    }

4. Using Custom Keys
---------------------

You can assign a custom **key** to each task. This allows you to identify results more explicitly in the output dictionary.

.. code-block:: python

    loom.add_function(fun1, [], {}, 'key1')
    loom.add_function(fun2, [1], {}, 'fun2')
    loom.add_function(fun3, [1], {'b': 3}, 'xyz')

    output = loom.execute()

.. code-block:: python

    >>> output
    {
      'key1': {
          'output': 'Hello World',
          'got_error': False,
          'error': None,
          'started_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 395002),
          'finished_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 396500),
          'execution_time': 0.001498,
         },
      'fun2': {
          'output': 1,
          'got_error': False,
          'error': None,
          'started_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 396590),
          'finished_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 397651),
          'execution_time': 0.001061
         },
      'xyz': {
          'output': 4,
          'got_error': False,
          'error': None,
          'started_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 400323),
          'finished_time': datetime.datetime(2019, 6, 28, 19, 44, 58, 401749),
          'execution_time': 0.001426
         }
    }


Migration Notice
================

``parallel-execute`` is now powered by a newer, more powerful backend called `concurra <https://pypi.org/project/concurra/>`_.

New users are encouraged to switch to the new interface:

.. code-block:: python

    from concurra import TaskRunner

    runner = TaskRunner()
    runner.add_task(my_func, *args, **kwargs)
    results = runner.run()

Backward compatibility with ``ThreadLoom`` and ``ProcessLoom`` is currently maintained,
but may be **deprecated in future versions**.