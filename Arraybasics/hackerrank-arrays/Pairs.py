def pairs(k, arr):
    count = 0
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]-arr[i] == k:
                count =count+1
    return count
# we shd return the pairs which differ by k
k = 1
arr = [1,2,3,4]
pairs(k,arr)