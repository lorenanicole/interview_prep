def twoArrays(k, A, B):
    # Add smallest elem from B to largest elem in A as these pairings would have the smallest guld
    # to overcome when adding each elem from each arr
    A = sorted(A, reverse=True)
    B.sort()

    for indx, _ in enumerate(A):
        if (A[indx] + B[indx]) < k:
            return 'NO'
    
    return 'YES'


print(twoArrays(10, [2,1,3], [7,8,9]) == 'YES')
print(twoArrays(5, [1,2,2,1], [3,3,3,4]) == 'NO')