def strings_xor(s, t):
    """
    With two inputs, XOR is true if and only if the inputs differ (one is true, one is false). 
    With multiple inputs, XOR is true if and only if the number of true inputs is odd.
    """
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

# 1 --> True
# 0 --> False
strings_xor('10101', '00101' == '10000')