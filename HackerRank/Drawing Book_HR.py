def pageCount(n, p):
    if n % 2 == 0:
        if p > (n - p):
            if (n - p) == 1:
                count = 1
            else:
                count = (n - p) // 2
        if p == (n - p):
            count = (n - p) // 2 + 1
        if p == 1:
            count = 0
        if p < (n - p):
            count = p // 2
    else:
        if p >= (n - p):
            count = (n - p) // 2
        if p < (n - p):
            count = p // 2
    return count

n = int(input())
p = int(input())

# n = 10
# p = 5
res = pageCount(n, p)
print(res)