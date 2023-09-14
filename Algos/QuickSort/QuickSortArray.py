arr=[10, 28, 45, 4, 6, 3, 1, 7, 9]

def quickSort(arr, start, end):
    if start>=end:
        return
    
    # Find pivot index
    partitionIndex=partition(arr,start, end)
    
    # Sort left part:
    quickSort(arr, start, partitionIndex-1)

    # Sort right part
    quickSort(arr, partitionIndex+1, end)


def partition(arr, start, end):
    pivotValue=arr[end]
    i=start-1

    # Logic here is to swap the elements in the array so that elements 
    # that are smaller than arr[end]/pivotValue move to left side of array
    for j in range(start, end):
        if arr[j]<=pivotValue:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    
    # As i+1 place would have the correct index of the pivot element 
    # therefore with a swap, pivot element is at the right place.
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1


print('Un-Sorted array: ', arr)
quickSort(arr, 0, len(arr)-1)
print('Sorted array: ', arr)