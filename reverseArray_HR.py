def reverseArray(a):
    list1 = []
    for i in range (len(a)-1,-1,-1):
        list1.append(a[i])
    return list1

# arr = list(map(int,input().split()))
arr = [5,4,3,2,1]
res = reverseArray(arr)

print(res)

