# STRETCH: implement Linear Search
def linear_search(arr, target):

  # TO-DO: add missing code
  count = 0
  for i in arr:
      if i == target:
          return count
      else:
          count += 1
  return -1   # not found

def find_pivot(leng):
    return int(leng/2)

# STRETCH: write an iterative implementation of Binary Search
# code needs to be sorted before hand
def binary_search(arr, target):

  if len(arr) == 0:
      return -1  # array empty

  low = 0
  high = len(arr)-1

    # TO-DO: add missing code
  while high >= low:
      pivot = find_pivot(low+high)
      if arr[pivot] == target:
          return pivot
      elif arr[pivot] > target:
          high = pivot - 1
      elif arr[pivot] < target:
          low = pivot + 1
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  pivot = find_pivot(low+high)

  if len(arr) == 0:
      return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if high >= low:
      if arr[pivot] == target:
          return pivot
      elif arr[pivot] > target:
          return binary_search_recursive(arr, target, low, pivot - 1)
      elif arr[pivot] < target:
          return binary_search_recursive(arr, target, pivot + 1, high)
  else:
      return -1
