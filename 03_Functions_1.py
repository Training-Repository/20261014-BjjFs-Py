#region 1
# def add(a: int , b: int) -> int:
#     return a + b

# result = add(5, 3)
# print(result)

# result = add(1.1, 2.2)
# print(result)

# result = add("Test", 10)
# print(result)
#endregion

#region Polymorphism
# from random import randint

# class Animal:
#     def speak(self) -> str:
#         return f"Animal makes a sound."

#     def eat(self) -> str:
#         return f"Animal is eating."

# class Dog:
#     def speak(self) -> str:
#         return f"Dog barks."

#     def eat(self):
#         return f"Dog tears into the food."

# class Cat:
#     def speak(self) -> str:
#         return f"Cat meows."

#     def eat(self):
#         return f"Cat nibbles the food."

# class Cow:
#     # def speak(self) -> str:
#     #     return f"Cow moos."

#     def eat(self):
#         return f"Cow chews the grass."


# def AnimalSpeak(obj:Animal):
#     print(obj.speak())



# ch = randint(1, 3)
# an: Animal

# match ch:
#     case 1:
#         an = Dog()

#     case 2:
#         an = Cat()

#     case 3:
#         an = Cow()

# AnimalSpeak(an)
#endregion 

#region functions as objects

# Method overloading can be done by using the package 'multiple dispatch'
# Use PIP to install it on system

# Use the dispatch method from the module

from multipledispatch import dispatch

@dispatch(int, int)
def add(a: int , b: int) -> int:
    """Add method for Integers"""
    print(add.__doc__)
    return a + b

# print(f"{add.__name__}, {type(add)}, {id(add)}")

@dispatch(float, float)
def add(a: float , b: float) -> float:
    """Add method for Floats"""
    print(add.__doc__)
    return a + b

# print(f"{add.__name__}, {type(add)}, {id(add)}")

result = add(5, 3)
print(result)

result = add(1.1, 2.2)
print(result)

# result = add("Test", "String")
# print(result)
#endregion