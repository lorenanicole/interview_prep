import math

# n -> number pages in the book
# p -> page number to turn to
def pageCount(n, p):
    # pagePairs = []
    # leftToRight, rightToLeft = 0, 0

    # for pageNum in range(1, n + 1, 2):
    #     pagePairs.append([pageNum - 1, pageNum])
    
    # for pages in pagePairs:
    #     if p in pages:
    #         break
    #     rightToLeft += 1

    # for pages in pagePairs[::-1]:
    #     if p in pages:
    #         break
    #     leftToRight += 1

    # print(leftToRight, rightToLeft)

    # if rightToLeft == leftToRight:
    #     return rightToLeft

    # leastAmountTurns = leftToRight if rightToLeft > leftToRight else rightToLeft

    # return leastAmountTurns
    rightToLeft = p // 2
    leftToRight = (n - p) / 2   
    return min(rightToLeft, math.ceil(leftToRight) if n % 2 == 0 else math.floor(leftToRight))


print(pageCount(5, 3) == 1)
print(pageCount(5, 4) == 0)