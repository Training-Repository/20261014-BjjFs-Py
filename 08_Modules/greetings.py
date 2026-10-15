__all__ = ['greet', 'greetName', 'greetInteractive']

def greet():
    print("Hi there")

def greetName(name):
    greeting = "Hello"
    msg = PrepMsg(greeting, name)
    print(msg)

def PrepMsg(greeting, name):
    return f"{greeting} {name}!"

def greetInteractive():
    name = input("What is your name: ")
    greeting = "Hello"
    msg = PrepMsg(greeting, name)
    print(msg)

def Test():
    greet()
    greetName("Manish")
    # greetInteractive()

# Test()
# print(f"Greetings --> {__name__ = }")

if __name__ == '__main__':
    Test()