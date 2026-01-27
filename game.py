## Mak3 an 8 x 8 grid filled with "~" and print it 


import copy
import random

def shoot(coords: set, grid: list, hits:set, total_shots: int, row: int, col:int):
    #This function takes in a grid for battelship, ships placement, and returns a hit or miss depending
    #on the placement of the ships compared to the grid.
    total_shots = 0
    if grid[row][col] !="🚢" and grid[row][col]!="⬛":
        if (row, col) in coords:
            grid[row][col] = "🚢"
            hits.add((row,col))
            total_shots += 1
            return "Hit!"
        else:
            grid[row][col] = "⬛"
            total_shots += 1
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
    all_coords=set() #use this for the hits we can get individual
    ship_list =[] # knowing when its sunk
    num=random.randint(3,5)
    while len(ship_list) < num:
        ship=get_ship()
        if all_coords.isdisjoint(ship): #checks if two sets have nothing in common
            all_coords.update(ship) #Like append
            ship_list.append(ship)
    return all_coords, ship_list 


def ship_tracker(ships:list, hits:set):
    ships_remaining = len(ships)
    count=0
    for ship in ships:
        if ship <= hits: #If ship is a SUBSET
            count+=1
    ships_remaining-=count
    return ships_remaining

def shot_limit(ships: list):
    if len(ships) == 3:
        return 16
    if len(ships) == 4:
        return 20
    if len(ships) == 5:
        return 25
    
def shot_countdown(ships: list, total_shots: int):
    max_shots = shot_limit(ships)
    if total_shots >= max_shots:
        return "Sorry, You Lost!"
    return max_shots - total_shots