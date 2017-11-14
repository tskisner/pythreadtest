
import sys

import time

import concurrent.futures

import numpy as np

from pythreadtest.work import work1


def do_work(n, work_id):
    data = np.zeros(n, dtype=np.float64)
    # This work function is in cython, but could be in pure C...
    work1(data)
    return data


samples = 100000
nwork = 100

nthread = int(sys.argv[1])

start = time.monotonic()

with concurrent.futures.ThreadPoolExecutor(max_workers=nthread) as executor:
    future_to_work = { executor.submit(do_work, samples, workid): workid for \
        workid in range(nwork) }
    
    for future in concurrent.futures.as_completed(future_to_work):
        task = future_to_work[future]
        data = future.result()

stop = time.monotonic()
elapsed = stop - start

print("Run with {} threads took {} seconds".format(nthread, elapsed))

