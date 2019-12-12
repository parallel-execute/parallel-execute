import abc
import logging
from datetime import datetime

from .log_adapter import adapt_log

LOGGER = logging.getLogger(__name__)


class RunnerWrapper(abc.ABC):
    """ Runner wrapper class """

    log = adapt_log(LOGGER, 'RunnerWrapper')

    def __init__(self, func_runner, runner_id, key, tracker, log_exception=True):
        """ Runner wrapper initializer

        Args:
            func_runner (FuncRunner): FuncRunner instance
            runner_id (int): runner id
            key (str): key to store the function output in output dict
            tracker (dict): tracker dict
        """

        self.func_runner = func_runner
        self.id = runner_id
        self.tracker = tracker
        self.log_exception = log_exception
        self.key = key
        self.runner = None
        self.__initialize_tracker()

    def __str__(self):
        return "<RunnerWrapper %s[#%s] %s>" % (self.key, self.id, self.func_runner)

    def __initialize_tracker(self):

        self.tracker[self.key] = dict()

    def __update_tracker(self, started, finished, output, got_error, error):
        """ Updates status in output dict """

        self.tracker[self.key] = {
            "started_time": started,
            "finished_time": finished,
            "execution_time": (finished - started).total_seconds(),
            "output": output,
            "got_error": got_error,
            "error": error
        }

    def is_tracker_updated(self):

        return True if self.tracker[self.key] else False

    def run(self):
        """ Runs function runner """

        output, error, got_error = None, None, False
        started = datetime.now()

        try:
            output = self.func_runner.run()
        except Exception as e:
            got_error = True
            error = str(e)
            if self.log_exception:
                self.log.exception("Encountered an exception on {} {}".format(self, e))
        finally:
            finished = datetime.now()
            self.__update_tracker(started, finished, output, got_error, error)

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
