# def superDigit(n, k):
#     if k == 1:
#         return int(n)
    
#     return int(n[0]) + superDigit(n[1:], k-1)

# print(superDigit('8888', 4) == 32)
# print(superDigit('116', 3) == 8)
# print(superDigit('8', 1) == 8)

def superDigit(n, k):
    if k == 1:
        import pdb; pdb.set_trace()
        return sum(map(lambda digit: int(digit), n.split()))
    else:
        return f'{n}{superDigit(n, k-1)}'

# print(superDigit('8888', 4) == 32)
print(type(superDigit('116', 3))) # == 8)
print(superDigit('8', 1) == 8)


# def fibRecursive(nthTerm):
#     if nthTerm == 1:
#         return 0
#     elif nthTerm == 2:
#         return 1
#     else:
#         return fibRecursive(n-1) + fibRecursive(n-2)
    