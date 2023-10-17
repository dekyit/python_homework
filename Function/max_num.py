def max_num(a, b, c):
    max_value = max(a, b, c)
    return max_value

#without using max function

def max_num(a, b, c):
    if a>= b and a>= c:
        return a
    elif b>= a and b>=c:
        return b
    else:
        return c
    

result = (max_num(10,15, 20))
print(result)