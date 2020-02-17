# TO-DO: Complete the selection_sort() function below

# selection sort
# imagine the array in two parts
# sorted and unsorted
# with each iteration
# find the smallest value
# and add it to the sorted array
# this is done by swapping the small value
# and the index of the end of the sorted values
# together


def selection_sort(arr, i=0):
    smallest_index = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[smallest_index]:
            smallest_index = j
    if i < len(arr):
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
        selection_sort(arr, (i+1))     
    return arr


# bubble sort basically go for the length of the array
# it compares an index and the next index together
# depending which one is smaller it will switch the
# values - if swap was made then will perform another another
# functon call
# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            bubble_sort(arr)
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
