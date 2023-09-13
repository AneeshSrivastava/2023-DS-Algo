
def mergeArrays(leftArr, rightArr):
    resultArr=[]
    leftArrIndex=0
    rightArrIndex=0

    while leftArrIndex<len(leftArr) and rightArrIndex<len(rightArr):
        if leftArr[leftArrIndex] <= rightArr[rightArrIndex]:
            resultArr.append(leftArr[leftArrIndex])
            leftArrIndex+=1
        else:
            resultArr.append(rightArr[rightArrIndex])
            rightArrIndex+=1
        
    resultArr+= leftArr[leftArrIndex:]
    resultArr+= rightArr[rightArrIndex:]
    return resultArr



def mergeSort(arr: list):
    if len(arr)<=1:
        return arr
    mid = int(len(arr)/2)
    leftarr = mergeSort(arr[:mid])
    rightarr = mergeSort(arr[mid:])
    return mergeArrays(leftarr, rightarr)

def main():
    arr = [3, 45, 6, 2, 1, -1, 10, 12]
    sortedArr= mergeSort(arr)
    print(sortedArr)

if __name__=="__main__":
    main()