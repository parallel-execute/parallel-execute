import time
import abc
import logging

from .log_adapter import adapt_log


LOGGER = logging.getLogger(__name__)


class RunnerWrapper(abc.ABC):
    """ Runner wrapper class """

    log = adapt_log(LOGGER, 'RunnerWrapper')

    def __init__(self, func_runner, runner_id, key, output_dict):
        """ Runner wrapper initializer

        Args:
            func_runner (FuncRunner): FuncRunner instance
            runner_id (int): runner id
            key (str): key to store the function output in output dict
            output_dict (dict): output dict
        """

        self.func_runner = func_runner
        self.id = runner_id
        self.output_dict = output_dict
        self.key = key

        self.got_error = None
        self.started = None
        self.finished = None
        self.runner = None

    def run(self):
        """ Runs function runner """

        self.got_error = False
        self.started = time.time()
        try:
            self.output_dict[self.key] = self.func_runner.run()
        except Exception as e:
            self.got_error = True
            self.output_dict[self.key] = e
            self.log.exception(f"Encountered an exception on {self} {e}")
        finally:
            self.finished = time.time()

    def __str__(self):
        return "<RunnerWrapper %s[#%s] %s>" % (self.key, self.id, self.func_runner)

    def join(self):
        self.runner.join()

    @abc.abstractmethod
    def start(self):
        """ Starts runner thread """

        pass

    @abc.abstractmethod
    def is_running(self):
        """ Returns True if runner is active else False """

        pass
