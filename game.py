## Mak3 an 8 x 8 grid filled with "~" and print it 
'''
Step 1) Define main(), make a list with 8 squiggles and print it 
'''

import copy

def shoot(ships: set, grid: list, row: int, col:int):
    if grid[row][col] !="X" and grid[row][col]!="0":
        if (row, col) in ships:
            grid[row][col] = "X"
        else:
            grid[row][col] = "0"


def main():
    grid = []
    ships = {(1,2), (1,3)}
    squiggles=["~", "~", "~", "~", "~", "~", "~", "~"]
    for squiggle in range(8):
        grid.append(copy.deepcopy(squiggles))
    #grid[1][2]="X"
    shoot(ships, grid, 1,0)
    print(grid)


main()
