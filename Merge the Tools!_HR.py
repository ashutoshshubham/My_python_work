#MY WRONG CODE

# def merge_the_tools(string, k):
#     string2 = []
#     len_sub_str = len(string) // k
#     for i in range (0, len(string), 3):
#         string2.append(string[i : len_sub_str + i] )
#     print(string2)



#OTHER'S CODE

def merge_the_tools(string, k):
    substring=[]
    for i,l in enumerate(string):
        if l not in substring:
            substring.append(l)
        if i%k==k-1:
            print(''.join(substring))
            substring=[]

    


s = 'AABCAAADA'
k = 3
merge_the_tools(s, k)



