# GWR kernel function specifications

__author__ = "Taylor Oshan tayoshan@gmail.com"

import scipy
from scipy.spatial.kdtree import KDTree
import numpy as np
from scipy.spatial.distance import cdist as cdist_scipy
#import numba as nb
#adaptive specifications should be parameterized with nn-1 to match original gwr
#implementation. That is, pysal counts self neighbors with knn automatically.

def fix_gauss(i, coords, bw, points=None, spherical=False):
    """
        Fixed Gaussian kernel.
        """
    w = _Kernel(i, coords, function='gwr_gaussian', bw=bw, truncate=False, points=points, spherical=spherical)
    return w.kernel

def adapt_gauss(i, coords, nn, points=None,spherical=False):
    """
        Spatially adaptive Gaussian kernel.
        """
    w = _Kernel(i, coords, fixed=False, bw=nn, function='gwr_gaussian', truncate=False, points=points, spherical=spherical)
    return w.kernel

def fix_bisquare(i, coords, bw, points=None, spherical=False):
    """
        Fixed bisquare kernel.
        """
    w = _Kernel(i, coords, function='bisquare', bw=bw, points=points, spherical=spherical)
    return w.kernel

def adapt_bisquare(i, coords, nn, points=None, spherical=False):
    """
        Spatially adaptive bisquare kernel.
        """
    w = _Kernel(i, coords, fixed=False, bw=nn, function='bisquare', points=points, spherical=spherical)
    return w.kernel

def fix_exp(i, coords, bw, points=None, spherical=False):
    """
        Fixed exponential kernel.
        """
    w = _Kernel(i, coords, function='exponential', bw=bw, truncate=False, points=points, spherical=spherical)
    return w.kernel

def adapt_exp(i, coords, nn, points=None, spherical=False):
    """
        Spatially adaptive exponential kernel.
        """
    w = _Kernel(i, coords, fixed=False, bw=nn, function='exponential', truncate=False, points=points, spherical=spherical)
    return w.kernel


#Customized Kernel class user for GWR because the default PySAL kernel class
#favors memory optimization over speed optimizations and GWR often needs the 
#speed optimization since it is not always assume points far awary
# are truncated #to zero

#@nb.njit()
def cdist(coords_i,coords,spherical):
    if spherical:
        dLat = np.radians(coords[:,1] - coords_i[1])
        dLon = np.radians(coords[:,0] - coords_i[0])
        lat1 = np.radians(coords[:,1])
        lat2 = np.radians(coords_i[1])
        a = np.sin(dLat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dLon/2)**2
        c = 2*np.arcsin(np.sqrt(a))
        R = 6371.0
        return R * c

        '''
        for j in range(m):
            dmat[j] = _haversine(coords_i[0], coords_i[1], coords[j][0], coords[j][1])
        '''
    else:
        dmat = np.sqrt(np.sum((coords_i - coords)**2,axis=1))
        return dmat
        
        '''
        for j in range(m):
            dmat[j] = np.sqrt((coords_i[0]-coords[j][0])**2 + (coords_i[1] - coords[j][1])**2)
        '''

class _Kernel(object):
    """
    GWR kernel function specifications.

    """
    def __init__(self, i, data, bw=None, fixed=True,
                 function='triangular', eps=1.0000001, ids=None, truncate=True,
                 points=None, spherical=False): #Added truncate flag
        
        
        if points is None:
            self.dvec = cdist(data[i], data, spherical).reshape(-1)
        else:
            self.dvec = cdist(points[i], data, spherical).reshape(-1)

        self.function = function.lower()

        if fixed:
            self.bandwidth = float(bw)
        else:
            self.bandwidth = np.partition(self.dvec, int(bw)-1)[int(bw)-1] * eps #partial sort in O(n)

        self.kernel = self._kernel_funcs(self.dvec/self.bandwidth)

        if truncate:
            self.kernel[(self.dvec >= self.bandwidth)] = 0

    
    def _kernel_funcs(self, zs):
        # functions follow Anselin and Rey (2010) table 5.4
        if self.function == 'triangular':
            return 1 - zs
        elif self.function == 'uniform':
            return np.ones(zi.shape) * 0.5
        elif self.function == 'quadratic':
            return (3. / 4) * (1 - zs ** 2)
        elif self.function == 'quartic':
            return (15. / 16) * (1 - zs ** 2) ** 2
        elif self.function == 'gaussian':
            c = np.pi * 2
            c = c ** (-0.5)
            return c * np.exp(-(zs ** 2) / 2.)
        elif self.function == 'gwr_gaussian':
            return np.exp(-0.5*(zs)**2)
        elif self.function == 'bisquare':
            return (1-(zs)**2)**2
        elif self.function =='exponential':
            return np.exp(-zs)
        else:
            print('Unsupported kernel function', self.function)


