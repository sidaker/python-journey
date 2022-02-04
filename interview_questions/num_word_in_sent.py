def wc(s):
    '''
    count occurance of each word and return a dictionary
    '''
    worddict={}
    for w in s.split():
        if(worddict.get(w) is None):
            worddict[w] = 1
        else:
            worddict[w] = worddict[w] + 1

    return worddict


if(__name__=='__main__'):
    s = "Hello I am saying Hello again. How are things with you Thank you for coming"
    print(wc(s))
