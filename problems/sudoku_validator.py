import math

def sudoku_validator(grid):
    digits = [1,2,3,4,5,6,7,8,9]

    for row in range(8):
        if grid[row] != digits:
            return False
        for col in range(8):
            if grid[row][col] != digits:
                return False

    subgrids = []
    # Alternatively can iterate over range(0,9,3)
    for row in range(3):
        subgrid = []
        for col in range(3):
            for i in range(3):
                for j in range(3):
                    # print(3*i + k, 3*j + l)
                    # 3*i + k generates value to iterate through every 3 first ranges in a given row
                    # 3*j + l generates value to iterate through every 3 elems within a row
                    subgrid.append(grid[3*row + i][3*col + j])
            # import pdb; pdb.set_trace()
            print(subgrid)
            if subgrid != digits:
                return False
    
    return True
    




def sudoku_validator(grid):
    digits = [1,2,3,4,5,6,7,8,9]

    # for r_indx, row in enumerate(grid):   # x - indx for row
    #     if row != digits:
    #         return False
    #     for c_indx, col in enumerate(grid):  # y - indx for col
    #         if grid[r_indx][c_indx] != digits:
    #             return False

    for w in range(0, 8, 2):
        for y in range(0, 8, 2):
            for x in range(0, 8, 2):
                for z in range(0, 8, 2):
                    print(w, y, x, z)

        





print(sudoku_validator([
[4, 0, 0, 0, 0, 5, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 9, 8],
[3, 0, 0, 0, 8, 2, 4, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 8, 0],
[9, 0, 3, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 3, 0, 6, 7, 0],
[0, 5, 0, 0, 0, 9, 0, 0, 0],
[0, 0, 0, 2, 0, 0, 9, 0, 7],
[6, 4, 0, 3, 0, 0, 0, 0, 0],
]))