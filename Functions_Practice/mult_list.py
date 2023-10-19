# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(input_list):
    result = 1
    for eachNumber in input_list:
        # the code below reads as--> result = result * eachNumber
         result = result * eachNumber
        # result *= eachNumber
    return result 

input_list= [2,4,6,8]
product = mult_list(input_list)
print(f"The product of the numbers in the list is: {product}")