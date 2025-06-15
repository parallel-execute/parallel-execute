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

    def execute(self, verify=True, raise_exception=False, error_message=None):
        output = self.run(verify=verify, raise_exception=raise_exception, error_message=error_message)
        for _, result in output.items():
            result['output'] = result.get('result', None)
            result['started_time'] = result.get('start_time', None)
            result['finished_time'] = result.get('end_time', None)
            result['execution_time'] = result.get('duration_seconds', None)
            result['got_error'] = result.get('has_failed', None)
        return output
