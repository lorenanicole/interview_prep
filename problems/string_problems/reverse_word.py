"""
https://www.geeksforgeeks.org/top-50-string-coding-problems-for-interviews/
"""

def reverse_words(s):
    words = s.split(" ")
    return " ".join(words[::-1])

print(reverse_words("i love programming very much") == "much very programming love i") 
print(reverse_words("geeks for all") == "all for geeks")
