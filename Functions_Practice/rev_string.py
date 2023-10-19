# Write a Python function called rev_string() to reverse a string
def rev_string(input_string):
#first, initialize an empty string to store the reversed characters
    reversed_string = ""
#then, iterate through each character of the input string with a for loop in REVERSE
#slicing a string example
# string = "Hello, World"
# result = string[0:5]  # Slices from index 0 to 5 (exclusive)
# print(result)  # Output: "Hello"
    for char in input_string[:: -1]:
        reversed_string += char
    
    return reversed_string

og_string = "Hello World"
reversed = rev_string(og_string)
print("This is the original:", og_string)
print("This is the reversed:", reversed )