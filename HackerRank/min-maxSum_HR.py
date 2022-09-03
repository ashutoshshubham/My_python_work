# Given five positive integers, find the minimum and maximum values 
# that can be calculated by summing exactly four of the five integers

def minMaxSum(arr):
    array = sorted(arr)
    a = 0
    b = 0
    for i in range (0,4):
        a = a + array[i]
    for j in range (1,5):
        b =  b + array[j]
    print (f'maximum sum is {b}')
    print(f'minimum sum is {a}')

n = list(map(int,input().split()))
minMaxSum(n)

