def roman_to_int(s):
    """
    Roman numerals are based on the symbols I, V, X, L, C, D, and M, which 
    represent 1, 5, 10, 50, 100, 500, and 1,000, respectively. 
    Different arrangements of these symbols represent different numbers. 
    The roman numbers I, II, III, IV, V, VI, VII, VIII, IX, and X represent 
    1, 2, 3, 4, 5, 6, 7, 8, 9 and 10 respectively.

    If a larger value symbol comes before, we subtract. Otherwise, we add.
    In IV, I comes before V and V has a larger value 5. So our result is 5 – 1 = 4.
    In VI, V comes before I and I has a smaller value 1. So our result is 5 + 1 = 6.
    In II, we have same values, so we add and get 1 + 1 = 2
    In case of more than 2 characters, we traverse from left to right and group only 
    when we see a greater value character after a smaller. 
    
    For example MXVII is 1000 + 10 + 5 + 1 + 1 = 1017. 
    And XLVII is (50 – 10) + 5 + 1 + 1 = 47.
    Note that L is larger and comes after X.
    """
    
    letter_to_num = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    number_int = []

    s = list(s)

    int_val = 0
    while len(s) > 1:
        if letter_to_num[s[0]] >= letter_to_num[s[1]]:
            int_val += letter_to_num[s[0]]
            s.pop(0)
        else:
            int_val += (letter_to_num[s[1]] - letter_to_num[s[0]])
            s = s[2:]
    
    if len(s) == 1:
        int_val += letter_to_num[s[0]]

    return int_val
        

    

print(roman_to_int("MXVII") == 1017)
print(roman_to_int("XLVII") == 47)
print(roman_to_int("XIX") == 19)
print(roman_to_int("XLIV") == 44)
print(roman_to_int("L") == 50)