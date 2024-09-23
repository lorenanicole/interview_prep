# def longest_prefix(words):
#     """
#     https://www.geeksforgeeks.org/longest-common-prefix-using-sorting/

#     1. sort words, when sort words it is sorted in abc order e.g. ['cats', 'cattery', 'ship', 'car', 'karma'] --> ['car', 'cats', 'cattery', 'karma', 'ship']
#     2. while less than len of shortest word and char is same in each word, grab char add to the prefix
#     3. when letter not in each word return either prefix if exists else return -1
#     """
#     words.sort()
#     prefix = ""

#     counter = 0
#     char_to_match = words[0][0]
#     while counter < len(words[0]):
#         for word in words:
#             if word[counter] == char_to_match:
#                 continue
#             else:
#                 break
#         prefix += char_to_match
#         counter += 1
    
#     if len(prefix) == 0:
#         return -1
    
#     return prefix
        
def longest_prefix(words):
    """
    https://www.geeksforgeeks.org/longest-common-prefix-using-sorting/

    1. sort words, when sort words it is sorted in abc order e.g. ['cats', 'cattery', 'ship', 'car', 'karma'] --> ['car', 'cats', 'cattery', 'karma', 'ship']
    2. while less than len of shortest word and char is same in each word, grab char add to the prefix
    3. when letter not in each word return either prefix if exists else return -1

    Big O(N) as only using a while loop to iterate over len(words[0])
    """
    words.sort()
    prefix = ""

    counter = 0
    while counter < len(words[0]) and words[0][counter] == words[-1][counter]:
        prefix += words[0][counter]
        counter += 1
    
    if len(prefix) == 0:
        return -1
    
    return prefix


print(longest_prefix(["geeksforgeeks", "geeks", "geek", "geezer"]) == "gee")
print(longest_prefix(["hello", "world"]) == -1)