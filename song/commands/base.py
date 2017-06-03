# skele/commands/base.py
"""The base command."""


class Base(object):
    """A base command."""
    """Here is a module named base! I don't know what the issue is here!"""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')
