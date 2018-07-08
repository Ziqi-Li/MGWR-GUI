"""Internal helper files for user output."""

__author__ = ("Luc Anselin luc.anselin@asu.edu, "
              "David C. Folch david.folch@asu.edu, "
              "Levi John Wolf levi.john.wolf@gmail.com, "
              "Jing Yao jingyao@asu.edu")

import numpy as np
from . import sputils as spu
import scipy
from scipy.sparse import csr_matrix
__all__ = []


def check_arrays(*arrays):
    """Check if the objects passed by a user to a regression class are
    correctly structured. If the user's data is correctly formed this function
    returns nothing, if not then an exception is raised. Note, this does not 
    check for model setup, simply the shape and types of the objects.

    Parameters
    ----------

    *arrays : anything
              Objects passed by the user to a regression class; any type
              object can be passed and any number of objects can be passed

    Returns
    -------

    Returns : int
              number of observations

    Examples
    --------

    >>> import numpy as np
    >>> import libpysal.api as lps
    >>> db = lps.open(lps.get_path('columbus.dbf'),'r')
    >>> # Extract CRIME column from the dbf file
    >>> y = np.array(db.by_col("CRIME"))
    >>> y = np.reshape(y, (49,1))
    >>> X = []
    >>> X.append(db.by_col("INC"))
    >>> X.append(db.by_col("HOVAL"))
    >>> X = np.array(X).T
    >>> n = check_arrays(y, X)
    >>> print n
    49

    """
    rows = []
    for i in arrays:
        if i is None:
            continue
        if not isinstance(i, (np.ndarray, csr_matrix)):
            raise Exception("all input data must be either numpy arrays or sparse csr matrices")
        shape = i.shape
        if len(shape) > 2:
            raise Exception("all input arrays must have exactly two dimensions")
        if len(shape) == 1:
            raise Exception("all input arrays must have exactly two dimensions")
        if shape[0] < shape[1]:
            raise Exception("one or more input arrays have more columns than rows")
        if not spu.spisfinite(i):
            raise Exception("one or more input arrays have missing/NaN values")
        rows.append(shape[0])
    if len(set(rows)) > 1:
        raise Exception("arrays not all of same length")
    return rows[0]


def check_y(y, n):
    """Check if the y object passed by a user to a regression class is
    correctly structured. If the user's data is correctly formed this function
    returns nothing, if not then an exception is raised. Note, this does not 
    check for model setup, simply the shape and types of the objects.

    Parameters
    ----------

    y       : anything
              Object passed by the user to a regression class; any type
              object can be passed

    n       : int
              number of observations

    Returns
    -------

    Returns : nothing
              Nothing is returned

    Examples
    --------

    >>> import numpy as np
    >>> import libpysal.api as lps
    >>> db = lps.open(lps.get_path('columbus.dbf'),'r')
    >>> # Extract CRIME column from the dbf file
    >>> y = np.array(db.by_col("CRIME"))
    >>> y = np.reshape(y, (49,1))
    >>> check_y(y, 49)
    >>> # should not raise an exception

    """
    if not isinstance(y, np.ndarray):
        print(y.__class__.__name__)
        raise Exception("y must be a numpy array")
    shape = y.shape
    if len(shape) > 2:
        raise Exception("all input arrays must have exactly two dimensions")
    if len(shape) == 1:
        raise Exception("all input arrays must have exactly two dimensions")
    if shape != (n, 1):
        raise Exception("y must be a single column array matching the length of other arrays")

    
