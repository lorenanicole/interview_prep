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





import string

def caesarCipher2(s, k):
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    translated_msg = ''

    for char in s:
        if not char.isalpha():
            translated_msg += char
            continue

        if char.islower():
            translated_msg += lower_letters[(lower_letters.index(char) + k) % len(lower_letters)]
        else:
            translated_msg += upper_letters[(upper_letters.index(char) + k) % len(lower_letters)]
    
    return translated_msg


def caesarCipher(word, shift):
    upperLetters = string.ascii_uppercase
    lowerLetters = string.ascii_lowercase

    translatedMessage = ""

    for char in word:
        if not char.isalpha():
            translatedMessage += char
        if char.isupper():
            translatedMessage += upperLetters[len(upperLetters.index(char)) % 26]
        elif char.islower():
            translatedMesssage += lowerLetters[len(lowerLetters.index(char) % 26)]
        



print(caesarCipher('middle-Outz', 2)) # == 'okffng-Qwvb')
print(caesarCipher("There's-a-starman-waiting-in-the-sky", 3))
print(caesarCipher2('W', 4))
print(caesarCipher("www.abc.xy", 87) == 'fff.jkl.gh')