ARR=[1, 2, 3]

def main():
    index=0
    
    ans = []
    output=[]
    solve(ARR, output, index, ans)
    return ans

def solve(arr, output, index, ans):
    # print('output: ', output)
    # base case:
    if index >= len(arr):
        ans.append(output[:])
        return

    # Exclude case:
    solve(arr, output, index+1, ans)

    # Include case:
    output.append(arr[index])
    solve(arr, output, index+1, ans )
    output.pop()

print('ANS: ',main())