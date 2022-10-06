#bubble sort

def bubble_sort(customList):
    for i in range (len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)

cList = [7,6,1,8,3,9,4,2,4]
bubble_sort(cList)