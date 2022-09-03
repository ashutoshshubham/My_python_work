def countApplesAndOranges(s, t, a, b, apples, oranges):
    app1 = []
    ora1 = []
    count = 0

    for app in apples:
        sum = a + app
        app1.append(sum)

    for ora in oranges:
        sum = b + ora
        ora1.append(sum)

    for i in app1:
        if i >= s and i <= t:
            count += 1
    print(count)

    count = 0

    for i in ora1:
        if i >= s and i <= t:
            count += 1
    print(count)

s = 7
t = 11
a = 5 
b = 15
m = 3
n = 2
apples = [-2,2,1]
oranges = [5,-6]

countApplesAndOranges(s, t, a, b, apples, oranges)
