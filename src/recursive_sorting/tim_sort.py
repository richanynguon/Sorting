import random
import math


def runs_sort(MIN_RUN, arr):
    '''
    Check if arr[i+1] - arr[i]  if positive or negative
    if negative then run is decreasing
    if positive then run is increasing
        will need to set this to a variable to check for the next loop
        is_increasing = False
        need a value or continue_trend = True once false break while loop
    set if run is increasing or decreasing if a[i+1] + a[i+2] is similar in suite
    append value into the an empty array
    keep going until !is_increasing
    if appended values array is more than or equal to min_run is_increasing = False [::-1] reverse arr
    if less then perform use current number for binary search and insertion until chunk is completed
        then is_increasing = False reverse then flip
    return arrays of arrays
    '''
    pass


def binary_search_insertion(target, arr):
    '''
    split arr length into two to find middle
    if middle value > target go left of the middle values and find the middle again
    else: do the opposite until appropriate target is found
    check if there is the value that will conflict with finding the right value
    append target after that index
    '''
    pass


def merge_gallop(arrA, arrB):
    '''
    merged_arr = []
    before = 0
    after = 0
    galloping_elements= []

    ## edge case 
    if arrA[0] > arrB[len(arrB)-1]
        range of checking can insert becomes arrB[0]-1 U arrA[0]
        so maybe arrB append arrA
        return results
    if arrA[len(arrA)-1] 
        range of check can insert becomes arrB[len(arrB)+1] - arr[lens]
        arrA append arrB
        *issue with this is that  will have error accessing those  but maybe as we use append we can also do that before and after
        return results

    if arrA[i] == arrA[i+1]:
        increment
    else: 
        arrA[i+1] > arrB[i] > arrA[i] ? add arrB[i] into empty array - increment and repeat until not longer true
       
    
        insert galloping_elements into arrA at that index

  
    '''
    pass


def tim_sort(arr):
    MIN_RUN = 3
    runs_sort(MIN_RUN, arr)
    '''
    runs_sort will return a lot of small array
    will need to check first 3 arrays in a stack - if 1 or 2 or 2 and 3 are similar in size then merge
    else break
    recurse until runs length is less than 2 
    return results
    '''


print(tim_sort(random.sample(range(200), 70)))
