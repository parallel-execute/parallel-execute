import warnings
from concurra import TaskRunner


class ThreadLoom(TaskRunner):
    """Deprecated Loom interface using threading.
    Use the new Concurra library with TaskRunner for more features: https://pypi.org/project/concurra/
    """

    def __init__(self, max_runner_cap=4, **kwargs):
        kwargs.pop('max_concurrency', None)
        kwargs.pop('use_multiprocessing', None)
        super().__init__(max_concurrency=max_runner_cap, use_multiprocessing=False, **kwargs)
