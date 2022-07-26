# You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to uppercase letters and vice versa.


str1 = 'AshUtOsh IS a "GoOd BOy"'
str1 = list(str1)
str2 = []
for i in str1:
    if i.isupper():
        str2.append(i.lower())
    elif i.islower():
        str2.append(i.upper())
    else:
        str2.append(i)
print("".join(str2))


