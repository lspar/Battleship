## Mak3 an 8 x 8 grid filled with "~" and print it 
'''
Step 1) Define main(), make a list with 8 squiggles and print it 
'''

import copy

def shoot(ships: set, grid: list, hits:set, row: int, col:int):
    #This function takes in a grid for battelship, ships placement, and returns a hit or miss depending
    #on the placement of the ships compared to the grid.
    if grid[row][col] !="X" and grid[row][col]!="0":
        return "Repeat!"
        if (row, col) in ships:
            grid[row][col] = "X"
            hits.add((row,col))
            return "Hit!"
        else:
            grid[row][col] = "0"
            return "Miss!"


def main():
    #This is the main function of the game that keeps track of the grid and executes actions of the player. 
    grid = []
    ships = {(1,2), (1,3)}
    hits=set()
    squiggles=["~", "~", "~", "~", "~", "~", "~", "~"]
    shots=[(3,2), (1,2), (1,3), (1,2)]
    for squiggle in range(8):
        grid.append(copy.deepcopy(squiggles))
    #grid[1][2]="X"
    #shoot(ships, grid, hits, 1,3)
    #shoot(ships, grid, hits, 1,2)
    #print(grid)
    #if hits==ships:
        #print ("Game over, you win")
    
    for i, j in shots:
        shoot(ships, grid, hits, i, j)
        if hits==ships:
            print ("You win")
            break
    print(grid)
    print(hits)
    
    
    
    '''for i, inner_list in enumerate(grid):
        for j, tile in enumerate(inner_list):
            if tile=="X":
                hits.add((i,j))
    print(hits)
    '''

main()


