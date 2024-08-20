def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2)

    a[mid], a[n-1] = a[n-1], a[mid]
    # print(a)
    st = mid + 1  
    ed = n - 2    
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]   
        # print(a)
        st += 1   
        ed -= 1   
        # print(st, ed)

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

# findZigZagSequence([2,3,5,1,4], 5) # == [1,4,5,3,2])
findZigZagSequence([1,2,3,4,5,6,7], 7) # == [1,2,3,7,6,5,4]