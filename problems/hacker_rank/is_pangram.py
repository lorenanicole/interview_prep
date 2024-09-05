def pangrams(s):
    s = s.lower()

    for c in range(ord('a'), ord('z')):
        if chr(c) not in s:
            return 'not pangram'
    
    return 'pangram'
    

import string

def pangrams(sentence):
    sentence = list(sentence)
    sentence = [char.lower() for char in sentence if char.isalpha()]
    sentence = list(set(sentence))
    # import pdb; pdb.set_trace()

    sentence = "".join(sorted(sentence))
    lowerCaseLetters = "".join(sorted(string.ascii_lowercase))
    # import pdb; pdb.set_trace()
    if lowerCaseLetters == sentence:
        return 'panagram'
    else:
        return 'not pangram'


print(pangrams('The quick brown fox jumps over the lazy dog') == 'pangram')
print(pangrams('We promptly judged antique ivory buckles for the prize') == 'not pangram')