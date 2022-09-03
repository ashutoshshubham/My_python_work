#string validator
#It can check if a string is composed of alphabetical 
#characters, alphanumeric characters, digits, etc.

s = input("Enter string\n")
isalnum = any(i.isalnum() for i in s)
isalpha = any(i.isalpha() for i in s)
isdigit = any(i.isdigit() for i in s)
islower = any(i.islower() for i in s)
isupper = any(i.isupper() for i in s)

print(isalnum)
print(isalpha)
print(isdigit)
print(islower)
print(isupper)