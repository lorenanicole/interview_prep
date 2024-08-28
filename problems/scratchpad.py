def getUniqueCharacter(s):
    # Write your code here
    freq_chars = {}
    
    for char in s:
        if char not in freq_chars:
            freq_chars[char] = 1
        else:
            # import pdb; pdb.set_trace()
            freq_chars[char] += 1
    
    first_indices = []
    for char, freq in freq_chars.items():
        if freq != 1:
            continue
        
        first_indices.append(s.index(char) + 1)
    
    return min(first_indices)

print(getUniqueCharacter('hackthegame'))