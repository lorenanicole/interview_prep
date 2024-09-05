def is_anagram(w1, w2):
    if len(w1) != len(w2):
        return False
    
    if sorted(w1) == sorted(w2):
        return True
    
    return False


print(is_anagram('angered', 'enraged') == True)
print(is_anagram('moon', 'mom') == False)