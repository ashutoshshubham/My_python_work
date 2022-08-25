import textwrap

def wrap(string,max_width):
    value = textwrap.fill(string,max_width)
    return (value)



string = 'abcdefghijkl'
max_width = 3
result = wrap(string,max_width)
print(result)


