from itertools import permutations

str1, num = input().split()
num = int(num)
# str1 = "HACK"
# num = 2
list(str1)
x = list(permutations(str1,num))
print(x.sort())
for i in x:
    print("".join(i))
