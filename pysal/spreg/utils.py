"""
Tools for different procedure estimations
"""

__author__ = "Luc Anselin luc.anselin@asu.edu, \
        Pedro V. Amaral pedro.amaral@asu.edu, \
        David C. Folch david.folch@asu.edu, \
        Daniel Arribas-Bel darribas@asu.edu,\
        Levi Wolf levi.john.wolf@gmail.com"

import numpy as np
from scipy import sparse as SP
from scipy.sparse import linalg as SPla
import scipy.optimize as op
import numpy.linalg as la
from .sputils import *
import copy


class RegressionPropsY(object):

    """
    Helper class that adds common regression properties to any regression
    class that inherits it.  It takes no parameters.  See BaseOLS for example
    usage.

    Parameters
    ----------

    Attributes
    ----------
    mean_y  : float
              Mean of the dependent variable
    std_y   : float
              Standard deviation of the dependent variable

    """

    @property
    def mean_y(self):
        try:
            return self._cache['mean_y']
        except AttributeError:
            self._cache = {}
            self._cache['mean_y'] = np.mean(self.y)
        except KeyError:
            self._cache['mean_y'] = np.mean(self.y)
        return self._cache['mean_y']
    
    @mean_y.setter
    def mean_y(self, val):
        try:
            self._cache['mean_y'] = val
        except AttributeError:
            self._cache = {}
            self._cache['mean_y'] = val
        except KeyError:
            self._cache['mean_y'] = val

    @property
    def std_y(self):
        try:
            return self._cache['std_y']
        except AttributeError:
            self._cache = {}
            self._cache['std_y'] = np.std(self.y, ddof=1)
        except KeyError:
            self._cache['std_y'] = np.std(self.y, ddof=1)
        return self._cache['std_y']
    
    @std_y.setter
    def std_y(self, val):
        try:
            self._cache['std_y'] = val
        except AttributeError:
            self._cache = {}
            self._cache['std_y'] = val
        except KeyError:
            self._cache['std_y'] = val
