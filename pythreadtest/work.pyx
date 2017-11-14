

import numpy as np
cimport numpy as np
cimport scipy.linalg.cython_lapack as cython_lapack

from libc.stdlib cimport malloc, free
from libc.string cimport memset
from libc.math cimport sqrt

f64 = np.float64
i64 = np.int64
i32 = np.int32

ctypedef np.float64_t f64_t
ctypedef np.int64_t i64_t
ctypedef np.int32_t i32_t


def work1(np.ndarray[f64_t, ndim=1] data):
    cdef i64_t n = data.shape[0]
    cdef i64_t i
    cdef i64_t j

    cdef double * cdata = <double*>malloc(n*sizeof(double))
    memset(cdata, 0, n*sizeof(double))

    with nogil:
        for i in range(100):
            for j in range(n):
                cdata[j] = sqrt(i) + sqrt(j)

    for i in range(n):
        data[i] = cdata[i]
    
    free(cdata)
    return


