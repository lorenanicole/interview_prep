def lonelyinteger(a):
    histogramOfElem = {}
    for elem in a:
        if elem not in histogramOfElem:
            histogramOfElem[elem] = 1
        else:
            histogramOfElem[elem] += 1
    
    for elem, freq in histogramOfElem.items():
        if freq == 1:
            return elem

print(lonelyinteger([1,2,3,4,3,2,1]) == 4)