def arrayManipulation(n, queries):
    query = [0] * n
    # print(query)
    for i in range (len(queries)):
        for j in range (queries[i][0], queries[i][1] + 1):
            query[j - 1] = query[j - 1] + queries[i][2]
    return max(query)
            

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

# n = 10
# queries = [[1,5,3],[4,8,7],[6,9,1]]

# n = 5
# queries = [[1,2,100],[2,5,100],[3,4,100]]

result = arrayManipulation(n, queries)

print(result)

