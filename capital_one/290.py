class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")

        import string
        lowercase_letters = string.ascii_lowercase

        numeric_pattern = ""

        for indx, char in enumerate(pattern):
            numeric_pattern += f'{lowercase_letters.index(char.lower())}'
            # abba -> 0, 1, 1, 0
        
        words_mapping = {}
        counter = 0
        for word in words:
            if word not in words_mapping:
                words_mapping[word] = counter
                counter += 1
        
        output = ""
        for word in words:
            output += f'{words_mapping[word]}'
        
        return output == numeric_pattern
            



            
        

solution = Solution()
print(solution.wordPattern("abba", "dog cat cat dog") == True)
print(solution.wordPattern("abba", "dog cat cat fish") == False)
print(solution.wordPattern("aaaa", "cat cat cat fish") == False)
print(solution.wordPattern("e", "eureka") == True)
