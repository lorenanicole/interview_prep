# class Solution(object):
#     def wordPattern(self, pattern, s):
#         """
#         :type pattern: str
#         :type s: str
#         :rtype: bool
#         """
#         words = s.split(" ")

#         import string
#         lowercase_letters = string.ascii_lowercase

#         numeric_pattern = ""

#         for indx, char in enumerate(pattern):
#             numeric_pattern += f'{lowercase_letters.index(char.lower())}'
#             # abba -> 0, 1, 1, 0
        
#         words_mapping = {}
#         counter = 0
#         for word in words:
#             if word not in words_mapping:
#                 words_mapping[word] = counter
#                 counter += 1
        
#         output = ""
#         for word in words:
#             output += f'{words_mapping[word]}'
        
#         return output == numeric_pattern
            



class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        pattern_to_position = {}
        counter = 0
        encoded_pattern = ""
        for char in pattern:
            if char not in pattern_to_position:
                pattern_to_position[char] = counter
                counter += 1
            encoded_pattern += str(pattern_to_position[char])
        
        word_to_position = {}
        words_encoded_pattern = ""
        counter = 0
        for word in words:
            if word not in word_to_position:
                word_to_position[word] = counter
                counter += 1
            words_encoded_pattern += str(word_to_position[word])
        
        return words_encoded_pattern == encoded_pattern
            

        

solution = Solution()
print(solution.wordPattern("abba", "dog cat cat dog") == True)
print(solution.wordPattern("abba", "dog cat cat fish") == False)
print(solution.wordPattern("aaaa", "cat cat cat fish") == False)
print(solution.wordPattern("e", "eureka") == True)
print(solution.wordPattern("deadbeef", "d e a d b e e f") == True)
