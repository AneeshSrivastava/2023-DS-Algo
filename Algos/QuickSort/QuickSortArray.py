arr=[0, 28, 45, 4, 6, 3, 1, 7, 9]

def swap(arr, firstIndex, secondIndex):
    temp = arr[firstIndex]
    arr[firstIndex]=arr[secondIndex]
    arr[secondIndex]=temp

def quickSort(arr, start, end):
    if start>=end:
        return
    
    # Find pivot index
    partitionIndex=partition(arr,start, end)

    # place elements < pivot to left and elements>pivot to right
    sortAroundPivot(arr, start, end, partitionIndex)
    
    # Sort left part:
    quickSort(arr, start, partitionIndex)

    # Sort right part
    quickSort(arr, partitionIndex+1, end)


def partition(arr, start, end):
    pivotValue=arr[start]
    # find right place for pivotValue place it in that place
    count=0
    for element in arr[start+1:]:
        if element<= pivotValue:
            count+=1
    newIndex=start+count
    swap(arr, start, newIndex)
    return newIndex

def sortAroundPivot(arr, start, end, pivotIndex):
    # sort left and right part new place
    i=start
    j=end
    while(i<pivotIndex and j>pivotIndex):
        while arr[i]<=arr[pivotIndex]:
            i+=1
        while arr[j]>arr[pivotIndex]:
            j-=1
    
        if i<pivotIndex and j>pivotIndex:
            swap(arr,i, j)
            i+=1
            j-=1

print('Un-Sorted array: ', arr)
quickSort(arr, 0, len(arr)-1)
print('Sorted array: ', arr)