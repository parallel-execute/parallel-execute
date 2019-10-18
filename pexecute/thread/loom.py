from .runner import ThreadRunner
from ..base_loom import Loom


class ThreadLoom(Loom):
    """ ProcessLoom class: executes runners using threading """

    def initialize_tracker_dict(self):

        self.tracker_dict = dict()

    def add_runner(self, runner, key, log_exception=True):
        """ Adds thread runner wrapper on runner function and adds it in the runner list

        Args:
            runner (ThreadRunner): thread runner instance
            key (str): key to store the output of the runner
            log_exception (bool): flag to suppress the exception
        """

        r_id = len(self.runners)
        r_wrapper = ThreadRunner(runner, r_id, key, self.tracker_dict, log_exception)
        self.runners.append(r_wrapper)
