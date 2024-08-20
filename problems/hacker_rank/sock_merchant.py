def sockMerchant(n, ar):
    pairs, sockColors = 0, {}

    for sock in ar:
        if sock not in sockColors:
            sockColors[sock] = 1
        else:
            sockColors[sock] += 1
    
    for sock, numSocks in sockColors.items():
        if numSocks > 1:
            pairs += int(numSocks / 2)
    
    return pairs

print(sockMerchant(7, [1,2,1,2,1,3,2]) == 2)