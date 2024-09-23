def get_trailing_zeroes(n):
    """
    Time complexity: O(log n)
    Auxiliary space: O(1)
    """
    zeroes = 0 
    while n > 0:
        n //= 5
        zeroes += n
    return zeroes


def findTrailingZeros(n):
    import math
    c = 0
    x = math.factorial(n)
    s = str(x)
    a = s[::-1]
    for i in a:
        if(i != "0"):
            break
        else:
            c += 1
    return c
 
num = 5;

resp = get_trailing_zeroes(24)
print(f"Number of trailing 0s for {num} factorial is {resp}")