def solve(s):

    for x in s[:].split():
      s = s.replace(x, x.capitalize())
    return ("".join(s))

str1 = "420ashu"
result = solve(str1)
print(result)

