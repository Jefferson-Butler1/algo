# Worst-case running time: O(n^2), where n is the number of elements in the list
def bubble_sort(arr, key= lambda x: x):
    # makes sure a user cant break it with a bad key
    if key is None:
        key = lambda x: x
    
    for i in range(len(arr) - 1, 0, -1):
        for ii in range(i):
            if key(arr[ii]) > key(arr[ii + 1]):
                arr[ii], arr[ii + 1] = arr[ii + 1], arr[ii]
