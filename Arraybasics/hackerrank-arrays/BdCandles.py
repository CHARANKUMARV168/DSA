candles = [4,4,1,3]

def birthdayCakeCandles(candles):
    x = max(candles)
    count = 0
    for num in candles :
        if num == x:
            count = count+1
    return count

x = birthdayCakeCandles(candles)
print(x)