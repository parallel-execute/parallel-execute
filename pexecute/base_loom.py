import logging
import abc

from .func_runner import FuncRunner

LOGGER = logging.getLogger(__name__)


class Loom(abc.ABC):
    """ Loom class """

    def __init__(self, max_runner_cap):
        """ Base Loom Initializer """

        self.max_runner_cap = max_runner_cap
        self.runners = list()
        self.output_dict = dict()

    @abc.abstractmethod
    def add_runner(self, runner, key):
        """ this method is overridden in child classes """

        pass

    def add_function(self, func, args=None, kwargs=None, key=None):
        """ Adds function in the Loom

        Args:
            func (reference): reference to the function
            args (list): function args
            kwargs (dict): function kwargs
            key (str): ket to store the function output in dictionary
        """

        if args is None:
            args = list()
        if kwargs is None:
            kwargs = dict()

        if key is None:
            key = len(self.runners)
        fr = FuncRunner(func, *args, **kwargs)
        self.add_runner(fr, key)

    def add_func(self, func, *args, **kwargs):
        """ Adds function in the Loom

        Args:
            func (reference): function reference
            *args: function args
            **kwargs: function kwargs
        """

        key = kwargs.pop('key', None)
        self.add_function(func, args, kwargs, key=key)

    def add_work(self, workload):
        """ Adds work to the loom

        Args:
            workload (list): list of works [(func, args, kwargs, key), (func2, args2, kwargs2), ...]
        """

        for work in workload:
            # Allow an optional key in the workload
            # e.g.:  [(func, args, kwargs, key), (func2, args2, kwargs2), ...]
            if len(work) > 4 or len(work) == 0:
                raise ValueError('Need 1 to 4 values to unpack')

            key = work[3] if len(work) == 4 else None
            kwargs = work[2] if len(work) > 2 else None
            args = work[1] if len(work) > 1 else None
            self.add_function(work[0], args, kwargs, key=key)

    def execute(self):
        """ Executes runners and returns output dict """

        # TODO: Override this method in child classes and use multiprocessing.Pool

        started = list()
        for runner in self.runners:
            runner.start()
            started.append(runner)
            if len(started) >= self.max_runner_cap:
                for started_runner in started:
                    started_runner.join()
                started = list()
        if started:
            for started_runner in started:
                started_runner.join()

        return dict(self.output_dict)

    @staticmethod
    def start_runner(runner):
        """ Starts runner """

        runner.run()
