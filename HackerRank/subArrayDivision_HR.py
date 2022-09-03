#Algorithm_HR

def birthday(s, d, m):
    val = 0
    for i in range(0,len(s) - m + 1):
        sum1 = 0
        for j in range(i,i+m):
            sum1 = sum1 + s[j]
        if sum1 == d:
            val += 1 
    return val

s = list(map(int,input().split()))
d = int(input())
m = int(input())

# s = [1,2,1,3,2]
# d = 3
# m = 2

result = birthday(s,d,m)
print(result)