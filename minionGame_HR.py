# string[start : stop - 1 : step]       string slicing

#Total Number of substring = (length of given string * (length of given string + 1)) // 2


#MY CODE.......NOT SUITBLE FOR LARGE STRING

# def minion_game(string):
#     list1 = []
#     vowel = ('A','E','I','O','U')

#     cons_count = 0
#     vow_count = 0

#     for i in range (len(string)):
#         for j in range(i + 1, len(string) + 1):
#             list1.append(string[i : j])

#     for val in range(0, len(list1)):
#         if list1[val][0] in vowel:
#             vow_count += 1
#         else:
#             cons_count += 1

#     if cons_count > vow_count:
#         print(cons_count)
#     elif cons_count < vow_count:
#         print(vow_count)
#     else:
#         print('Draw')





#OTHER'S CODE.....PERFACT

def minion_game(string):
    vowels = ['A', 'E', 'I' ,'O', 'U']
    strLen = len(string)
    max_score = strLen*(strLen+1)//2
    
    vowel_index = [strLen-i for i,c in enumerate(string) if c in vowels]
    kev_score = sum(vowel_index)        
    stu_score = max_score - kev_score

    if kev_score > stu_score:
        print(f"Kevin {kev_score}")
    elif kev_score < stu_score:
        print(f"Stuart {stu_score}")
    else:
        print(f"Draw")



# string = 'BANANA'

string = input()
minion_game(string)

