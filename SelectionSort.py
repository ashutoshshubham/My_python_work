#Selection Sort

def selection_sort(customList):
    for i in range (len(customList)):
        min_index = i
        for j in range (i + 1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[min_index], customList[i] = customList[i], customList[min_index]
    print(customList)

cList = [8,6,4,10,7,3,2,1,9,3,2,4,5]
selection_sort(cList)