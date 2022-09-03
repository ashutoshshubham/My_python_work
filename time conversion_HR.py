#Convert 12 hrs time formate into 24 hrs time formate

def timeConversion(s):
    Time = []
    s = list(s)
    if s[-2] == 'A':
        if s[0] == '0':
            for i in range (len(s)-2):
                Time.append(s[i])
        if s[0] == '1':
            if s[1] == '2':
               s[0] = str(int(s[0]) - 1)
               s[1] = str(int(s[1]) - 2)
               for i in range (len(s)-2):
                  Time.append(s[i])
            else:
                for i in range (len(s)-2):
                   Time.append(s[i])
    else:
        if s[0] == '1' and s[1] == '2':
            for i in range (len(s)-2):
                  Time.append(s[i])
        else:
            s[0] = str(int(s[0]) + 1)
            s[1] = str(int(s[1]) + 2)
            for i in range (len(s)-2):
                  Time.append(s[i])

    print(''.join(Time))

if __name__ == '__main__':
    time = input("Enter Time in hh:mm:ssAM/PM formate ")
    timeConversion(time)




