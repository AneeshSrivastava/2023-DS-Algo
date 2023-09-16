word='abc'

def main():
    index=0
    
    ans = []
    output=[]
    solve(word, output, index, ans)
    return ans

def solve(word, output, index, ans):
    # print('output: ', output)
    # base case:
    if index >= len(word):
        ans.append(output[:])
        return

    # Exclude case:
    solve(word, output, index+1, ans)

    # Include case:
    output.append(word[index])
    solve(word, output, index+1, ans )
    output.pop()

print('Subsequences of string: ',main())