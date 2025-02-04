def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n-2) + fib(n-1)

print(fib(0) == 0)
print(fib(1) == 1)
print(fib(2) == 1)
print(fib(3) == 2)
print(fib(4) == 3)
print(fib(5) == 5)
print(fib(6) == 8)
print(fib(7) == 13)
print(fib(8) == 21)

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144