def rotateLeft(d, arr):
    for i in range (d):
        n = len(arr)
        temp = arr[0]
        arr.pop(0)
        arr.append(temp)
    return(arr)



# d = 4
# arr = [1,2,3,4,5]

n = int(input())
d = int(input())
arr = list(map(int,input().split()))

res = rotateLeft(d, arr)
print(res)




