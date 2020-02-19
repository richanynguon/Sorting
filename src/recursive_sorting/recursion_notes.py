# recurse(3)
#     print 3
#     recurse(2)
#         print 2
#         recurse(1)
#             print 1
#         recurse(1)
#             print 1
#     recurse(2)
#         print 2
#         recurse(1)
#             print 1
#         recurse(1)
#             print 1

# 1. A recursive algorithm must have a base case.
# 2. A recursive algorithm must change its state and move toward the base case.
# 3. A recursive algorithm must call itself, recursively.
# Print every number, starting at `number`, until you reach 0
# def recurse(number):
#     if number <= 0:
#         return
#     print(number)
#     number -= 1
#     recurse(number)
#     recurse(number)
# recurse(2)
# Fibonacci Sequence [1, 1, 2, 3, 5, 8, 13, 21, 34]
# Return the Nth Fibonacci Number
def fibonacci(n):
    if n < 0:
        print("Negative numbers are not valid")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Return (n - 1) + (n - 2)
        return fibonacci(n - 1) + fibonacci(n - 2)

# [5 9 3 7 2 8 1 6]
# [3 2 1][5][9 7 8 6]
# [2 1][3][][5][7 8 6][9][]
# [1][2][3][5] [6][7][8] [9] 
# Decide on base case
# base case is []
# Find the pivot point
# partition our data to the left and right of the pivot
# left -> smaller than pivot, right -> larger than pivot
# What if they're the same size as the pivot? Just pick one?  >=
# repeat, recurse
# my_list = [5, 9, 3, 7, 2, 8, 1, 6]
def partition(data):
    left = []
    pivot = data[0]
    right = []
    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else: # Handling > or =
            right.append(item)
    return left, pivot, right
def quicksort(data):
    if data == []:
        return data
    left, pivot, right = partition(data)
    return quicksort(left) + [pivot] + quicksort(right)
