
#region OLD
# fn1 = greet

# def wrapper():
#     print("Greeting entry")
#     fn1()
#     print("Greeting exit")

# fn2 = wrapper

# greet = wrapper
#endregion

def logger(fn):
    def wrapper():
        wrapper.__doc__ = fn.__doc__
        print(f"{fn.__name__} entry")
        fn()
        print(f"{fn.__name__} exit")
    return wrapper

# greet = logger(greet)

@logger
def greet():
    """greet method"""
    print("Hi there!")

@logger
def SayHello():
    """sayHello method"""
    print("Hello")

#------------------------------------------------


# wrapper()
# fn1()
# fn2()
greet()
print(greet.__doc__)
print("-"*40)
SayHello()
print(SayHello.__doc__)


print("="*40)
print(greet.__doc__)

#-----------------------------------


# To decorate any given function we need to handle the args and returns.
# The subject method arg-list could have any combination of args.
# That can be handled using the univerasal arg-list i.e (*vArgs, **kwArgs)
# Variable arguments & Keyworded-variable arguments 
