import multiprocessing

from .runner import ProcessRunner
from ..base_loom import Loom


class ProcessLoom(Loom):
    """ ProcessLoom class: executes runners using multi-processing """

    def __init__(self, max_runner_cap):
        """ ProcessLoom Initializer """

        Loom.__init__(self, max_runner_cap)
        manager = multiprocessing.Manager()
        self.output_dict = manager.dict()

    def add_runner(self, runner, key):
        """ Adds process runner wrapper on runner function and adds it in the runner list

        Args:
            runner (ProcessRunner): process runner instance
            key (str): key to store the output of the runner
        """

        r_id = len(self.runners)
        r_wrapper = ProcessRunner(runner, r_id, key, self.output_dict)
        self.runners.append(r_wrapper)
