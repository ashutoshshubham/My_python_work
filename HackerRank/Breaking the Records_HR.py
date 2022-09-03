# Breaking the Records

def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    max_count = 0
    min_count = 0
    for score in scores:
        if score > max_score:
            max_score = score
            max_count += 1

        if score < min_score:
            min_score = score
            min_count += 1
    return (max_count,min_count)

scores = [3,4,21,36,10,28,35,5,24,42]
result = breakingRecords(scores)
print(' '.join(map(str,result)))

