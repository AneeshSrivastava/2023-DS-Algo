word='abc'

def main():
    wordIndex=0
    result=[]
    getPermutations(word, wordIndex, result)
    print('The permutations of the given string is: ', result)

def getPermutations(word, wordIndex, result):
    # Base case:
    if wordIndex>=len(word):
        result.append(word[:])
        return

    # Logic:
    for i in range(wordIndex, len(word)):
        word=list(word)
        word[i], word[wordIndex] = word[wordIndex], word[i]
        word=''.join(word)
        getPermutations(word, wordIndex+1, result)
        # Back track
        word=list(word)
        word[i], word[wordIndex] = word[wordIndex], word[i]
        word=''.join(word)

if __name__=="__main__":
    main()