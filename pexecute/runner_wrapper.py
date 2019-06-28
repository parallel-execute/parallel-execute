import abc
import logging
from datetime import datetime

from .log_adapter import adapt_log


LOGGER = logging.getLogger(__name__)


class RunnerWrapper(abc.ABC):
    """ Runner wrapper class """

    log = adapt_log(LOGGER, 'RunnerWrapper')

    def __init__(self, func_runner, runner_id, key):
        """ Runner wrapper initializer

        Args:
            func_runner (FuncRunner): FuncRunner instance
            runner_id (int): runner id
            key (str): key to store the function output in output dict
            output_dict (dict): output dict
        """

        self.func_runner = func_runner
        self.id = runner_id
        self.tracker = self.initialize_tracker()
        self.key = key
        self.runner = None
        self.__update_tracker()

    def run(self):
        """ Runs function runner """

        output, error, got_error = None, None, False
        started = datetime.now()

        try:
            output = self.func_runner.run()
        except Exception as e:
            got_error = True
            error = e
            self.log.exception(f"Encountered an exception on {self} {e}")
        finally:
            finished = datetime.now()
            self.__update_tracker(started, finished, output, got_error, error)

    def __str__(self):
        return "<RunnerWrapper %s[#%s] %s>" % (self.key, self.id, self.func_runner)

    def join(self):
        self.runner.join()

    def __update_tracker(self, started=None, finished=None, output=None, got_error=None, error=None):
        """ Updates status in output dict """

        execution_time = (finished - started).total_seconds() if started and finished else None
        self.tracker.update({
            "started_time": started,
            "finished_time": finished,
            "execution_time": execution_time,
            "output": output,
            "got_error": got_error,
            "error": error
        })

    @abc.abstractmethod
    def start(self):
        """ Starts runner thread """

        pass

    @abc.abstractmethod
    def is_running(self):
        """ Returns True if runner is active else False """

        pass

    @abc.abstractmethod
    def initialize_tracker(self):
        """ Initializes tracker dict """

        pass
