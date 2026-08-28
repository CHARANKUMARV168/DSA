
arr = [ 1, 1,0,-1,-1]

def plusMinus(arr):
    n = len(arr)
    pos = 0
    zero = 0 
    neg = 0
    for num in arr :
        if num < 0 :
            neg = neg + 1
        if num == 0:
            zero = zero +1
        if num > 0 :
            pos = pos + 1

    print(pos/n)
    print(neg/n)
    print(zero/n)

plusMinus(arr)