WORD="23"
keypad = [
    '',
    '',
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
    'pqrs',
    'tuv',
    'wxyz'
]

def solve(word, output: str, wordIndex, ans, keypad):
    # base case:
    if wordIndex >= len(word):
        ans.append(output)
        return 
    
    # 
    number = int(word[wordIndex])
    keypadLetters=keypad[number]

    for i in range(0, len(keypadLetters)):
        output+=keypadLetters[i]
        solve(word, output, wordIndex+1, ans, keypad)
        output=output[:-1]
    

def main():
    wordIndex=0
    ans=[]
    output=""
    solve(WORD, output, wordIndex, ans, keypad)
    print("Answer is: ", ans)


if __name__=="__main__":
    main()