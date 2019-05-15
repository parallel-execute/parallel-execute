import multiprocessing

from ..runner_wrapper import RunnerWrapper


class ProcessRunner(RunnerWrapper):
    """ Process Runner Wrapper """

    def start(self):
        """ Starts runner process """

        if self.is_running():
            raise RuntimeError("Can't start an already-running runner")
        self.runner = multiprocessing.Process(target=self.run)
        self.runner.daemon = True
        self.runner.start()

    def is_running(self):
        """ Returns True if runner is active else False """

        return self.runner and self.runner.is_alive()
