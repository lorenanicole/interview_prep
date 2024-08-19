def miniMaxSum(arr: list) -> list:
    sortedArr = sorted(arr)
    miniSum = sum(sortedArr[:4])
    maxSum = sum(sortedArr[1:])

    print(miniSum, maxSum)


miniMaxSum([1, 3, 5, 7, 9]) == [16, 24]