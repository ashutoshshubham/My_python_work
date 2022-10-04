
def bonAppetit(bill, k, b):
    sum = 0
    for i in bill:
        sum = sum + i
    sum = sum - bill[k]
    sum = sum // 2
    if sum == b:
        return("Bon Appetit")
    else:
        return(b - sum)
    


n = int(input())
k = int(input())
bill = list(map(int,input().split()))
b = int(input())


# n = 4
# k = 1
# bill = [3,10,2,9]
# b = 7

res = bonAppetit(bill,k,b)
print(res)
