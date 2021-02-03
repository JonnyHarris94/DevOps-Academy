def fizz_buzz(wordList):
    a = 'Fizz'
    b = 'Buzz'
    c = a + b
    
    res = []

    for n in wordList:
        if (n %5 == 0) and (n %3 ==0):
            res = res + [n,c]
        if (n %3 == 0):
            res = res + [n,a]
        if (n %5 == 0):
            res = res + [n,b]
    return res

list = range(1,100)
print(fizz_buzz(list))

