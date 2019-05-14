from .runner import ThreadRunner
from ..base_loom import Loom


class ThreadLoom(Loom):
    """ ProcessLoom class: executes runners using threading """

    def add_runner(self, runner, key):
        """ Adds thread runner wrapper on runner function and adds it in the runner list

        Args:
            runner (ThreadRunner): thread runner instance
            key (str): key to store the output of the runner
        """

        r_id = len(self.runners)
        r_wrapper = ThreadRunner(runner, r_id, key, self.output_dict)
        self.runners.append(r_wrapper)
