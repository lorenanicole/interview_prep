def gridChallenge(grid):
    n = len(grid)

    # Sort the row
    for i in range(n):
        grid[i] = sorted(grid[i])
    
    # Sort the columns
    for column in range(n):
        # Given we have the column number, iterate through
        # the rows to build the column 
        col = [grid[x][column] for x in range(n)]
        sorted_col = sorted(col)
        # Are the columns in alphabetical order?
        if col != sorted_col:
            return 'NO'

    return 'YES'


print(gridChallenge([
    'abc',
    'hjk',
    'mpq',
]) == 'YES')

print(gridChallenge([
    'mpxz',
    'abcd',
    'wlmf',
]) == 'NO')

print(gridChallenge([
    'abc',
    'lmp',
    'qrt',
]) == 'YES')

# print(gridChallenge([
#     'ebacd',
#     'fghij',
#     'olmkn',
#     'trpqs',
#     'xywuv'
# ]) == 'YES')

# print(gridChallenge([
#     'ebacd',
#     'fgyij',
#     'zlmkn',
#     'trpqs',
#     'aywuv'
# ]) == 'NO')

# print(gridChallenge([
#     'abc',
#     'ade',
#     'efg'
# ]) == 'YES')

grid = [
    'ebacd',
    'fghij',
    'olmkn',
    'trpqs',
    'xywuv'
]