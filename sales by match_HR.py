def sockMerchant(n, ar):
    list1 = list(set(ar))
    list2 = []
    count = 0
    for i in list1:
        x = ar.count(i)
        list2.append(x)
    for i in list2:
        if i >= 2:
            count = count + i // 2
    return(count)

n = int(input())
ar = list(map(int,input().split()))

# n = 7
# ar = [10,20,20,10,10,30,50,10,20]
res = sockMerchant(n, ar)
print(res)

