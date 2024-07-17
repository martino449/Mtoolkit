import random
numbers_str = input("Write numbers to sort (separate them with a comma): \n")
numeri = list(map(int, numbers_str.split(',')))


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right) 




print(quicksort(numeri))
input("Program by Martin449")