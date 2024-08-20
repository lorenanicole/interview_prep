def matchingStrings(strings, queries):
    output = []
    for elem in queries:
        matches = len(list(filter(lambda e: e == elem, strings)))
        output.append(matches)
    
    return output



print(matchingStrings(['def', 'de', 'fgh'], ['de', 'lmn', 'fgh']) == [1, 0, 1])
print(matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab']) == [2, 1, 0])