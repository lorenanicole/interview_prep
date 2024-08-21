# def balancedSums(arr):
#     # Write your code here
#     n = len(arr)

#     leftSum, rightSum = 0, 0
#     for i in range(n):
#         leftSum = sum(arr[:i])
#         rightSum = sum(arr[i+1:])
#         if leftSum == rightSum:
#             return 'YES'
        
#     return 'NO'

def balancedSums(arr):
    # Write your code here
    n = len(arr)

    leftSum, rightSum = 0, sum(arr)
    for i in range(n):
        # Do not process current elem in right side sum
        rightSum -= arr[i]

        if leftSum == rightSum:
            return 'YES'

        # Add current elem to left side sum
        leftSum += arr[i]
        
    return 'NO'




print(balancedSums([1,2,3]) == 'NO')
print(balancedSums([1,2,3,3]) == 'YES')
print(balancedSums([1,1,4,1,1]) == 'YES')
print(balancedSums([2,0,0,0]) == 'YES')
print(balancedSums([0,0,2,0]) == 'YES')