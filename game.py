## Mak3 an 8 x 8 grid filled with "~" and print it 


import copy
import random

def shoot(ships: set, grid: list, hits:set, row: int, col:int):
    #This function takes in a grid for battelship, ships placement, and returns a hit or miss depending
    #on the placement of the ships compared to the grid.
    if grid[row][col] !="X" and grid[row][col]!="0":
        if (row, col) in ships:
            grid[row][col] = "X"
            hits.add((row,col))
            return "Hit!"
        else:
            grid[row][col] = "0"
            return "Miss!"
    return "Repeat!"

'''
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
'''
def make_grid():
    grid= []
    squiggles=["🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"]
    for squiggle in range(8):
        grid.append(copy.deepcopy(squiggles))
    return grid 

def get_ship():
    #choose h or.v
    #pick a valid start
    horizontal="Horizontal"
    vertical="Vertical"
    two_options=[horizontal, vertical]
    chosen_option=random.choice(two_options)

    if chosen_option=="Horizontal":
        #set the range of row 0-7
        # range col 0-6
        #choosing starting coord
        horizontal_set=set()
        row_options=list(range(8))
        col_options=list(range(7))
        chosen_row=random.choice(row_options)
        chosen_col=random.choice(col_options)
        #Put it into a tuple
        horizontal_set.add((chosen_row, chosen_col))
        horizontal_set.add((chosen_row, chosen_col+1))
        return horizontal_set
    else:
        #vertical starting  coord
        vertical_set=set()
        row_options=list(range(7))
        col_options=list(range(8))
        chosen_row=random.choice(row_options)
        chosen_col=random.choice(col_options)
        #Put it into tuple 
        #vertical_set.add((chosen_row, chosen_col), (chosen_row+1, chosen_col))
        vertical_set.add((chosen_row, chosen_col))
        vertical_set.add((chosen_row+1, chosen_col))
        return vertical_set
    


def all_ships():
    all=set()
    num=random.randint(3,5)
    while len(all) < num*2:
        ship=get_ship()
        if all.isdisjoint(ship): #checks if two sets have nothing in common
            all.update(ship) #Like append
    return all

print(all_ships())