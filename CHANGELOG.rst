Changelog
=========

2.0.0 (2025-06-13)
------------------

**Added**
- Introduced Concurra ``TaskRunner`` for unified parallel execution.

**Changed**
- Deprecated ``ThreadLoom`` and ``ProcessLoom``, now backed by Concurra ``TaskRunner``.

**Fixed**
- Proper timeout handling and progress reporting.
