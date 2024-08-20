import string

def caesarCipher(s, k):
    charLower = list(string.ascii_lowercase[:26])
    charUpper = list(string.ascii_uppercase[:26])
    translatedMsg = ""
    for char in s:
        if not char.isalpha():
            translatedMsg += char
            continue 

        if char.islower():
            translatedMsg += charLower[(charLower.index(char) + k) % len(charLower)] 
        else:
            translatedMsg += charUpper[(charUpper.index(char) + k) % len(charUpper)] 
    
    return(translatedMsg)

print(caesarCipher('middle-Outz', 2) == 'okffng-Qwvb')
