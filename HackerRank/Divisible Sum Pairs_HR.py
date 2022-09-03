def divisibleSumPairs(n, k, ar):

    list1 = [] 
    for i in range (0,len(ar)-1):
        for j in range (i + 1,len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                tup1 = (ar[i],ar[j])
                list1.append(tup1)
    return (len(list1))


# n = 4
# k = 5
# ar = [1,2,3,4,5,6]

n = int(input())
k = int(input())
ar = list(map(int,input().split()))

res = divisibleSumPairs(n,k,ar)
print(res)



