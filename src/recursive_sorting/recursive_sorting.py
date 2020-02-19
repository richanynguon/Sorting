# TO-DO: complete the helper function below to merge 2 sorted arrays
# take two arrays
# take first item of each array - compare
# lowest value will be appended
# attach to new array


def merge(arrA, arrB):
    merged_arr = []
    # TO-DO
    before = 0
    after = 0
    while before < len(arrA) and after < len(arrB):
        if arrA[before] > arrB[after]:
            merged_arr.append(arrB[after])
            after += 1
        else:
            merged_arr.append(arrA[before])
            before += 1
    # issue:  wasnt fully returning the whole array - it did not return the last number of the array
    # adding what is before over after comparision will be the highest number
    # print(arrA, arrB, merged_arr + arrA[before:] + arrB[after:])
    return merged_arr + arrA[before:] + arrB[after:]


# TO-DO: implement the Merge Sort function below USING RECURSION
# take length of array and divide by two
# round value
# return [:middle] [middle:]
# this is done until there is one value
# calls merge on both part of splitted array together after merge sort
def find_pivot(leng):
    return int(leng/2)


def implement_pivot(arr):
    pivot = find_pivot(len(arr))
    before = arr[pivot:]
    after = arr[:pivot]
    return before, after


def merge_sort(arr):
    before, after = implement_pivot(arr)
    if len(arr) <= 1:
        return arr
    else:
        return merge(merge_sort(before), merge_sort(after))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    pointer = mid + 1
    while start <= mid and pointer <= end:
        if arr[start] < arr[pointer]:
            start += 1
        else:
            switch_placement = arr[pointer]
            # range(start, stop, step)
            for i in range(pointer, start, -1):
                arr[i] = arr[i - 1]
            arr[start] = switch_placement
            start += 1
            pointer += 1
            mid += 1
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    # lil confusing about how the function stacks
    if l < r:
        pivot = find_pivot(l+r)
        merge_sort_in_place(arr, l, pivot)
        #will stack first and complete its side
        merge_sort_in_place(arr, pivot+1, r)
        # will stack next until complete
        merge_in_place(arr, l, pivot, r)
        # will stack next until complete
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
