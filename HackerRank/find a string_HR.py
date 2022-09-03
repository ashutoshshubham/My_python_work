# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.


def count_substring(string,sub_string):
    list1 = []
    count = 0
    for i in range (len(string) - len(sub_string) + 1):
        list1.append(string[i : len(sub_string) + i])
    for j in list1: 
        if j == sub_string:
            count += 1
    return (count)

string = input()
sub_string = input()
res = count_substring(string,sub_string)
print(res)



    
