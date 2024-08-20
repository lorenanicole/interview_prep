def flippingBits(n):
    unsigned32n = "{:032b}".format(n)
    flippedBits = ""
    for char in unsigned32n:
        if char == '0':
            flippedBits += '1'
        else:
            flippedBits += '0'
    
    return int(flippedBits, 2)

print(flippingBits(1) == 4294967294)
print(flippingBits(2147483647) == 2147483648)

