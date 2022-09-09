n = int(input())
list1 = []
arr = []

for i in range(0,n):
    cmd = list(map(str,input().split()))
    list1.extend(cmd)
for j in list1:
    if j == 'append':
        x = list1.index(j)
        arr.append(int(list1[x + 1]))
        list1.remove(list1[x])
    elif j == 'insert':
        x = list1.index(j)
        arr.insert(int(list1[x + 1]), int(list1[x + 2]))
        list1.remove(list1[x])
    elif j == 'remove':
        x = list1.index(j)
        arr.remove(int(list1[x + 1]))
        list1.remove(j)
    elif j == 'sort':
        arr.sort()
    elif j == 'pop':
        arr.pop()
    elif j == 'reverse':
        arr.reverse()
    elif j == 'print':
        print(arr)


#sample input

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print



