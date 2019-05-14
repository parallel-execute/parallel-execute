"""useful things that will come from lib in near term"""

import logging

LOGGER = logging.getLogger(__name__)


class _ContextLogger(logging.LoggerAdapter):
    """
    LoggerAdapter to prepend '[context] ' to the logged message
    https://docs.python.org/2/howto/logging-cookbook.html

    See usage in adapt
    """
    warn = logging.LoggerAdapter.warning

    def process(self, msg, kwargs):
        return '[%s] %s' % (self.extra['context'], msg), kwargs


def adapt_log(logger, context):
    """Add context to an existing logger instance"""
    return _ContextLogger(logger, {'context': context})

