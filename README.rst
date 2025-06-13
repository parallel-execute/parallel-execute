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
------------

Install the latest release from PyPI:

::

    pip install parallel-execute

This will also install the lightweight `concurra` core engine as a dependency.

---

Quick Start
-----------

Step 1: Create a Loom
~~~~~~~~~~~~~~~~~~~~~

Use a `Loom` class to create a task executor.

- Thread-based execution:

  .. code-block:: python

      from pexecute.thread import ThreadLoom
      loom = ThreadLoom(max_runner_cap=5)

- Process-based execution:

  .. code-block:: python

      from pexecute.process import ProcessLoom
      loom = ProcessLoom(max_runner_cap=5)

**`max_runner_cap`** defines how many tasks run in parallel at once.


Step 2: Add Tasks
~~~~~~~~~~~~~~~~~

You can add tasks using `.add_function()`:

.. code-block:: python

    def say_hello(): return "Hello"
    def square(x): return x * x

    loom.add_function(say_hello)
    loom.add_function(square, args=(4,))
    loom.add_function(sum, args=([1, 2, 3],))

Or add multiple at once using `.add_work()`:

.. code-block:: python

    work = [
        (say_hello, [], {}, 'greeting'),
        (square, (4,), {}, 'squared'),
        (sum, ([1, 2, 3],), {}, 'total')
    ]
    loom.add_work(work)


Step 3: Execute
~~~~~~~~~~~~~~~

Execute all tasks and retrieve results:

.. code-block:: python

    output = loom.execute()

    >>> output
    {
        'greeting': 'Hello',
        'squared': 16,
        'total': 6
    }

If you didn’t provide keys, the results will be stored using the task order index:

.. code-block:: python

    output = loom.execute()
    >>> output
    {
        0: 'Hello',
        1: 16,
        2: 6
    }

---

Advanced Notes
--------------

- Any Python function can be passed as a task.
- Tasks run in parallel with thread or process workers.
- Results include execution time, errors, and output.
- Task execution blocks until all tasks are complete.
- If a task fails, it will still be recorded in the output dictionary with the error trace.

---

Migration Notice
================

parallel-execute is now powered by a newer, more powerful backend called `concurra <https://pypi.org/project/concurra/>`_.

New users are encouraged to use:

.. code-block:: python

    from concurra import TaskRunner

    runner = TaskRunner()
    runner.add_task(my_func, *args, **kwargs)
    results = runner.run()

Backward compatibility with `ThreadLoom` and `ProcessLoom` is maintained, but may be deprecated in future versions.

---

License
-------

MIT License. See `LICENSE <https://github.com/parallel-execute/parallel-execute/blob/master/LICENSE>`_.


Changelog
=========

2.0.1 (2025-06-13)
------------------

**Added**
- Introduced Concurra ``TaskRunner`` for unified parallel execution.
- `concurra <https://pypi.org/project/concurra/>`_.


**Changed**
- Deprecated ``ThreadLoom`` and ``ProcessLoom``, now backed by Concurra ``TaskRunner``.

**Fixed**
- Proper timeout handling and progress reporting.

