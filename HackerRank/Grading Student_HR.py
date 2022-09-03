# Every student receives a grade in the inclusive range from 0 to 100 .
# Any grade less than 40 is a failing grade.
# If the difference between the grade and the next multiple of 5 is less than 3, 
#  round grade up to the next multiple of .
# If the value of grade is less than 38, 
#  no rounding occurs as the result will still be a failing grade.


def gradingStudents(grade):
    ans = []
    for num in grade:
        g1 = num
        if num >= 38:
            remainder = num % 10
            if remainder < 5 and remainder != 0:
                remainder = 5 - remainder
                if remainder < 3:
                    g1 = g1 + remainder
                else:
                    g1
            elif remainder > 5:
                remainder = 10 - remainder
                if remainder < 3:
                    g1 = g1 + remainder
                else:
                    g1
            else:
                g1
        else:
            g1
        ans.append(g1)
    return(ans)
    
grade = [73,67,38,33]
result = gradingStudents(grade)
print('\n'.join(map(str, result)))
