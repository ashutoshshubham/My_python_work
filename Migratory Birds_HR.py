def migratoryBirds(arr):
    list1 = list(set(arr))
    list2 = []
    for i in list1:
        x = arr.count(i)
        list2.append(x)
    for i in range (len(list2)):
        if list2[i] == max(list2):
            break
    return list1[i]
            




n = int(input())
arr = list(map(int,input().split()))

# n = 11
# arr = [1,2,3,4,5,4,3,2,1,3,4]
# migratoryBirds(arr)


res = migratoryBirds(arr)
print(res)