#problem 1
def hello():
    print("Hello")

result = hello()
print(result)

#problem 2
def pack(a, b, c):
    return [a,b,c]

result = pack(1,2,3)
print(result)

#problem 3
def eat_lunch(foods):
    if len(foods)== 0:
        print("My lunchbox is empty!")
    else: 
        for i in range(len(foods)):
            if i == 0:
                print(f"First I eat {foods[0]}")
            else:
                print(f"Next I eat {foods[1]}")

result = eat_lunch(["apple","banana","sandwich","cookie"])
print(result)