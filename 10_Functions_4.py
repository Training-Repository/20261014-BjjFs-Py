# Lambda Functions -  Function without a name

# def square(num):
#     return num **2

# def cube(num):
#     return num **3

# def quad(num):
#     return num **4

# tools = [square, cube, quad]

tools = [lambda x: x**2, lambda x: x**3, lambda x: x**4]
print(tools[0](3))

IsEven = lambda x: x%2 == 0 
print(IsEven(9))

HasR = lambda s : 'r' in s.lower()
print(HasR("STRING"))