# def countingSort(arr):
#     freqArr = [0] * 100
    
#     for elem in arr:
#         freqArr[elem] += 1

#     return freqArr

# print(countingSort([
#     63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 
#     12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 
#     27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 
#     41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 
#     60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33])) == [
#         2, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 3, 2, 2, 0, 4, 4, 1, 1, 0, 0, 0, 0, 3, 0, 0, 
#         1, 0, 1, 2, 0, 1, 2, 2, 3, 0, 2, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 2, 0, 0, 1, 1, 
#         1, 0, 1, 0, 1, 1, 2, 3, 0, 1, 2, 0, 1, 2, 1, 1, 4, 1, 0, 1, 1, 3, 0, 0, 2, 1, 2, 
#         3, 2, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 3, 1, 0]

def countingSort(arr):
    freqArr = [0] * 100
    print(len(freqArr))
    for elem in arr:
        print(elem)
        freqArr[elem] += 1

    sortedArr = []
    for elem, indx in enumerate(freqArr):
        sortedArr += [elem] * indx
    
    return sortedArr


def countingSort2(arr):
    freqArr, outputArr = [0] * 100, []

    for _, val in enumerate(arr):
        freqArr[val] += 1

    for indx, val in enumerate(freqArr):
        if val == 0:
            continue

        outputArr += [indx] * val

    return outputArr



print(countingSort2([1,1,3,2,1]) == [1,1,1,2,3])
print(countingSort2([3,5,1,6,7,8,3]) == [1, 3, 3, 5, 6, 7, 8])
