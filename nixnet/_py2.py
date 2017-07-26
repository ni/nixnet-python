from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class abstractclassmethod(classmethod):  # NOQA: N801
    """Backport from Python 3.2

    Once we are only on Python 3.3+, `abstractmethod` should be sufficient.
    """

    __slots__ = ()
    __isabstractmethod__ = True

    def __init__(self, callable):
        callable.__isabstractmethod__ = True
        super(abstractclassmethod, self).__init__(callable)
