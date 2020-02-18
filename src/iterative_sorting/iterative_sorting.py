# TO-DO: Complete the selection_sort() function below

# REASONS NOT TO DO RECURSION:
# NOT READABLE
# also could hit stack overflow so not so efficient

# selection sort
# imagine the array in two parts
# sorted and unsorted
# with each iteration
# find the smallest value
# and add it to the sorted array
# this is done by swapping the small value
# and the index of the end of the sorted values
# together


def swap(arr, n, nx):
    arr[nx], arr[n] = arr[n], arr[nx]


def selection_sort(arr, i=0):
    smallest_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[smallest_index]:
            smallest_index = j
    if i < len(arr):
        swap(arr, smallest_index, i)
        selection_sort(arr, (i+1))
    return arr


# without recursion

#   for i in range(0, len(arr) - 1):
#     current = i
#     smallest_index = current
#     for j in range(current, len(arr)):
#       if arr[j] < arr[ smallest_index]:
#          smallest_index = j
#     if current !=  smallest_index:
#      swap(arr, smallest_index, current)
#   return arr


# bubble sort basically go for the length of the array
# it compares an index and the next index together
# depending which one is smaller it will switch the
# values - if swap was made then will perform another another
# functon call
# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i+1]:
            swap(arr, i+1, i)
            bubble_sort(arr)
    return arr

# without recursion

# for i in range(len(arr)):
#     for j in range(0, len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             swap(arr, j, j+1)


# STRETCH: implement the Count Sort function below
# need to verify if any number in array is negative
# create an array with an highest index of the highest numeric
# value of the given array
# loop through original array assign +1 to appropriate index
# in created array
# in the index array add values between i and i+1
# then loop over array referencing the index array
# so value of input array will equal index
# that value of the index array will be the index
# of the new sorted array, when that is computed
# -1 from the value of that index index array
def count_sort(arr):
    if len(arr) == 0:
        return arr
    elif min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    else:
        maximum = int(max(arr))
        count_array = [0]*(maximum+1)
        print(maximum)

        for i in range(len(arr)):
            count_array[arr[i]] += 1

        sorted_array = []

        for j, num in enumerate(count_array):
            while num > 0:
                sorted_array.append(j)
                num -= 1

        return sorted_array
