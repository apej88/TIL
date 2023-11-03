from operator import attrgetter, itemgetter
from datastructure.c_stack import Stack

def partition(arr, low, high):
    pivot = arr[low]
    j = low
    for i in range(low + 1, high + 1):
        #print(arr,low,j,i)
        if arr[i] < pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    pivot = j
    arr[low], arr[pivot] = arr[pivot], arr[low]
    return pivot

def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot -1)
        quicksort(arr, pivot+1, high)
        
    return arr

def quicksort_stack(arr):
    stack = Stack()
    stack.push([0, len(arr)-1])
    
    while not stack.is_empty():
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            stack.push([low, pivot - 1])
            stack.push([pivot + 1, high])
    
    return arr    



