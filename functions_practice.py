def hello():
    print("Hello")

def pack(a, b, c):
    return pack[a,b,c]

def eat_lunch(foods):
    if len(foods)== 0:
        print("My lunchbox is empty!")
    else: 
        for i in range(len(foods)):
            if i == 0:
                print(f"First I eat {foods[0]}")
            else:
                print(f"Next I eat {foods[1]}")
    
hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])