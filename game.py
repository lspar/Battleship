## Mak3 an 8 x 8 grid filled with "~" and print it 


import copy
import random

def shoot(coords: set, grid: list, hits:set, row: int, col:int):
    #This function takes in a grid for battelship, ships placement, and returns a hit or miss depending
    #on the placement of the ships compared to the grid.
    if grid[row][col] !="🚢" and grid[row][col]!="⬛":
        if (row, col) in coords:
            grid[row][col] = "🚢"
            hits.add((row,col))
            return "Hit!"
        else:
            grid[row][col] = "⬛"
            return "Miss!"
    return "Repeat!"


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
        return 20
    if len(ships) == 4:
        return 30
    if len(ships) == 5:
        return 40
    return 0
    
def shot_countdown(ships: list, total_shots: int):
    max_shots = shot_limit(ships)
    if total_shots >= max_shots:
        return 0
    return max_shots - total_shots