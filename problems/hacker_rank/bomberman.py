import time

def bomberMan(n, grid):
    # bomb_map = []
    # grid = [list(row) for row in grid]

    # col_size = len(grid[0])
    # row_size = len(grid)

    # while time.sleep(3) or n > 0:
    #     for r_indx in range(row_size):
    #         for c_indx in range(col_size):
    #             # import pdb; pdb.set_trace()
    #             if grid[r_indx][c_indx] == '.':
    #                 grid[r_indx][c_indx] = 'O'
    #                 bomb_map.append([r_indx, c_indx])
    #         # import pdb; pdb.set_trace()
    #     # import pdb; pdb.set_trace()
    #     for coords in bomb_map:
    #         grid[coords[0]][coords[1]] = '.'

    #     n-= 1    
    # import pprint; pprint.pprint(grid)
    # print("--------------")
    # return grid
    counter = 0
    while counter < 3:
        counter += 1
    
    while n > 0:
        for indx, elem in enumerate(grid):
            if elem == '.':
                grid[indx] = 'O'
            elif elem == 'O':
                grid[index] = 'O'
        n -= 1
    
    return grid

grid = ['.......', '...O...', '....O..','.......', 'OO.....', 'OO.....']
expected_response = ['OOO.OOO','OO...OO', 'OOO...O', '..OO.OO', '...OOOO', '...OOOO']


# print(bomberMan(3, grid))# == expected_response)
print(bomberMan(3, ['.', '.', '.', '.', '.', '.', '.']))