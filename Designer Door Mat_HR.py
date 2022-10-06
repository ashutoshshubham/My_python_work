# Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

def door_mat(n,m):

    first_half(n,m)
    mid(m)
    second_half(n,m)
      
def first_half(n,m):
    for i in range (1, n // 2 + 1):
        x = m - 3*(2*i - 1)
        for j in range (1, (x // 2) + 1):
            print("-",end = "")
        for k in range (0, 2*i-1):
            print(".|.", end = "")
        for j in range (1, (x // 2) + 1):
            print("-",end = "")
        print(sep = '\n')

def mid(m):
    for i in range (0,(m-6) // 2):
        print("-",end = "")
    print("WELCOME", end = '')
    for i in range (0,(m-6) // 2):
        print("-",end = "")
    print(sep = '\n')

def second_half(n,m):
    for i in range (n // 2 ,0 ,-1):
        x = m - 3*(2*i - 1)
        for j in range (x // 2 ,0,-1):
            print("-",end = "")
        for k in range (2*i-1,0,-1):
            print(".|.", end = "")
        for j in range (x // 2 ,0,-1):
            print("-",end = "")
        print(end = '\n')




n = 7
m = 21
# n,m = list(map(int,input().split()))
door_mat(n,m)