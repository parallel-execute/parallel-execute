import threading

from ..runner_wrapper import RunnerWrapper


class ThreadRunner(RunnerWrapper):
    """ Thread Runner class """

    def start(self):
        """ Starts runner thread """

        if self.is_running():
            raise RuntimeError("Can't start an already-running runner")
        self.runner = threading.Thread(target=self.run)
        self.runner.setDaemon(True)
        self.runner.start()

    def is_running(self):
        """ Returns True if runner is active else False """

        return self.runner and self.runner.isAlive()
