def find_pivot(leng):
    return int(leng/2)


def implement_pivot(arr):
    pivot = find_pivot(len(arr))
    before = arr[pivot:]
    after = arr[:pivot]
    return before, after


def binary_search(arr, target, low, high):
    pivot = find_pivot(low+high)
    if low == high:
        if arr[low] > target:
            return low
        else:
            return low + 1
    if low > high:
        return low
    elif arr[pivot] > target:
        return binary_search(arr, target, low, pivot - 1)
    elif arr[pivot] < target:
        return binary_search(arr, target, pivot + 1, high)
    else:
        return pivot


def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        temp = list_to_sort[i]
        j = binary_search(list_to_sort, temp, 0, i-1)
        list_to_sort = list_to_sort[:j] + [temp] + list_to_sort[j:i] + [list_to_sort[i+1]]
    return list_to_sort


print(insertion_sort([1, 2, 34, 56, 7, 34, 6, 4]))


def merge(arrA, arrB):
    merged_arr = []

    before = 0
    after = 0
    while before < len(arrA) and after < len(arrB):
        if arrA[before] > arrB[after]:
            merged_arr.append(arrB[after])
            after += 1
        else:
            merged_arr.append(arrA[before])
            before += 1
    return merged_arr + arrA[before:] + arrB[after:]


def merge_sort(arr):
    before, after = implement_pivot(arr)
    if len(arr) <= 1:
        return arr
    else:
        return merge(merge_sort(before), merge_sort(after))


def timsort(arr):

    return arr
