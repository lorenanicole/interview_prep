from collections import defaultdict

def shortestDistance(s, word1, word2):
    locations = defaultdict(list)

    # for indx, word in enumerate(s):
    #     if word == word1:
    #         locations['word1'].append(indx)
    #     elif word == word2:
    #         locations['word2'].append(indx)
    
    distance_pairs = []
    pair_num = 0

    # for indx, word in enumerate(s):
    #     if word == word1:
    #         distance_pairs[pair_num] = [indx]
    #     elif word == word2:
    #         distance_pairs[pair_num].append(indx)
    #         pair_num += 1
    
    # for indx, pair in enumerate(distance_pairs):
    #     distance_pairs[indx] = abs(pair[1] - pair[0])
    
    # return min(distance_pairs)


    """
    1. If find one of the words start counting
    2. Only if the next word found is the other word then can stop counting
    3. Note the distance
    4. Return min distance
    """
    w1, w2 = False, False
    i, counter = 0, 0
    distances = []
    while i < len(s):
        if s[i] == word1:
            w1 = True
            print(i, counter, 'word1')
            counter += 1
        if s[i] == word2:
            w2 = True
            print(i, counter, 'word2')
            counter += 1
        if w1 and w2:
            print(counter, 'w1 and w2')
            distances.append(counter + 1)
            counter = 0
            w1, w2 = False, False
        i += 1

    return min(distances)
        
        


print(shortestDistance(['axa', 'ffn', 'ty', 'bs', 'oin', 'bs', 'axa'], 'bs', 'axa') == 1)