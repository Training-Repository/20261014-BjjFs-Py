# Fibonacci series
def FibGen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
    print("||DONE||")

x = FibGen(5)
# val = next(x)
# type(x), type(FibGen), next(x), next(x), next(x), next(x), next(x), next(x)

while True:
    try:
        val = next(x)
        print(val, end=", ")
    except StopIteration:
        print("\nDone with Fibonacci series")
        break

print("="*80)