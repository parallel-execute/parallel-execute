import warnings
from concurra import TaskRunner


class ProcessLoom(TaskRunner):
    """Deprecated Loom interface using multi-processing.
    Use the new Concurra library with TaskRunner for more features: https://pypi.org/project/concurra/
    """

    def __init__(self, max_runner_cap=4, **kwargs):
        kwargs.pop('max_concurrency', None)
        kwargs.pop('use_multiprocessing', None)
        super().__init__(max_concurrency=max_runner_cap, use_multiprocessing=True, **kwargs)
