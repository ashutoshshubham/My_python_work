def plusMinus(arr):
    length = len(arr)
    zero = 0
    pos = 0
    neg = 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i > 0:
            pos += 1
        elif i < 0:
            neg += 1
    print(round(zero/length,6))
    print(round(pos/length,6))
    print(round(neg/length,6))
 
if __name__ == '__main__': 
    n = int(input())
    arr = list(map(int,input().split()))
    plusMinus(arr)



