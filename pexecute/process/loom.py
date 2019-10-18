import multiprocessing

from .runner import ProcessRunner
from ..base_loom import Loom


class ProcessLoom(Loom):
    """ ProcessLoom class: executes runners using multi-processing """

    def initialize_tracker_dict(self):

        manager = multiprocessing.Manager()
        self.tracker_dict = manager.dict()

    def add_runner(self, runner, key, log_exception=True):
        """ Adds process runner wrapper on runner function and adds it in the runner list

        Args:
            runner (ProcessRunner): process runner instance
            key (str): key to store the output of the runner
            log_exception (bool): flag to suppress the exception
        """

        r_id = len(self.runners)
        r_wrapper = ProcessRunner(runner, r_id, key, self.tracker_dict, log_exception)
        self.runners.append(r_wrapper)
