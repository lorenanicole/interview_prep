def pangrams(s):
    s = s.lower()

    for c in range(ord('a'), ord('z')):
        if chr(c) not in s:
            return 'not pangram'
    
    return 'pangram'
    

print(pangrams('The quick brown fox jumps over the lazy dog') == 'pangram')
print(pangrams('We promptly judged antique ivory buckles for the prize') == 'not pangram')