def maxMin(k, arr):
    arr.sort()
    minDiff = None
    # Generate sub arrays of length k
    # Starting at 0 iterate up to len(arr) + 1, bc arrs are 0 based, minus k as don't
    # want to iterate past end of arr
    for count in range(len(arr) + 1 - k):  
        subArr = arr[count:count+k] 
        # print(count, count + k, arr[count:count+k])
        tempDiff = subArr[-1] - subArr[0]
        if minDiff is None:
            minDiff = tempDiff
        if tempDiff < minDiff:
            minDiff = tempDiff 
    
    return minDiff


print(maxMin(2, [1,4,7,2]) == 1)
print(maxMin(4, [1,2,3,4,10,20,30,40,100,200]) == 3)
print(maxMin(3, [1,2,9,7,12]) == 5)