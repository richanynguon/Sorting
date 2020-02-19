import random
import math


def detect_runs(min_run, arr):
    if len(arr) % min_run == 0:
        array = arr
    else:
        array = arr[:-1]
        odd_out = arr[-1]
    print(array)
    print(odd_out)
    # for i in range(len(arr)):
    #     print(arr[i])
    #     if arr[i+1] - arr[i] >= 0:
    #         # if increasing - save index
    #         # check next one
    #         pass
    #     else:
    #         pass

def tim_sort(arr):
    MAX_SPLIT = 32
    MIN_RUN = 4
            





print(tim_sort(random.sample(range(200), 65)))
