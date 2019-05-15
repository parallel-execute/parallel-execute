import logging
from .log_adapter import adapt_log

LOGGER = logging.getLogger(__name__)


class FuncRunner(object):
    """ Func Runner class """

    log = adapt_log(LOGGER, 'FuncRunner')

    def __init__(self, func, *args, **kwargs):
        """ FuncRunner Initializer

        Args:
            func (reference): function reference
            *args: function args
            **kwargs: function kwargs
        """

        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.name = getattr(func, '__name__', str(func))

    def run(self):
        """ Runs function and returns output """

        self.log.debug(f"{self.func}, {self.args}, {self.kwargs}")
        return self.func(*self.args, **self.kwargs)

    def __str__(self):
        return "<FuncRunner %s>" % self.name
