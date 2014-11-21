def fib(n):
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fibList(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    print(result)
fib(20)
