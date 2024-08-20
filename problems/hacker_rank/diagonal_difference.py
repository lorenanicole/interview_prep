def diagonalDifference(arr):
    leftToRight, rightToLeft, countUp = 0, 0, 0

    sizeSquare = len(arr[0])

    for count in range(sizeSquare):
        leftToRight += arr[count][count]

    for count in range(sizeSquare - 1, -1, -1):
        rightToLeft += arr[countUp][count]
        countUp += 1

    return(abs(leftToRight - rightToLeft)) 


print(diagonalDifference([[1, 5, 3], [4, 5, 6], [9, 8, 9]]) == 2)
print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15)