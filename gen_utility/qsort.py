#Qsort
numbers_str = input("Write numbers to sort (separate them with a comma): \n") #asks the user what numbers to sort
numeri = list(map(int, numbers_str.split(',')))#Here the numbers are separated


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)#Here the numbers are put in ascending order




print(quicksort(numeri))
input("Program by Martin449 and foxeritocretito")
