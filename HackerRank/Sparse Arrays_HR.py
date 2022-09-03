def matchingStrings(strings, queries):
    count_sim = []
    count = 0
    for que in queries:
        for strg in strings:
            if que == strg:
                count += 1
        count_sim.append(count)
        count = 0
    return (count_sim)

strings_count = int(input().strip())

strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

queries_count = int(input().strip())

queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

# strings = ['def','de','fgh']
# queries = ['de','lmn','fgh']

res = matchingStrings(strings, queries)

print(res)