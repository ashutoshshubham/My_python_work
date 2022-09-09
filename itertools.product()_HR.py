from itertools import product

A = list(map(int,input().split()))
B = list(map(int,input().split()))

# A = [1,2]
# B = [3,4]
C = list(product(A,B))

for x in C:
    print(x, end = " ")

