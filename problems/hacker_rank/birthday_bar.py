def birthday(s, d, m):
    numSegments, total = 0, 0

    # We decrement m by 1 as lists are 0 based 
    for indx, _ in enumerate(s[:len(s) - (m - 1)]):
        print(indx)
        total = sum(s[indx:indx+m])
        if total == d:
            numSegments += 1
        total = 0
    

    return numSegments
        

print(birthday([2,2,6,3,1], 4, 2) == 2)