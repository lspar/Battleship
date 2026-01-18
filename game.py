## Mak3 an 8 x 8 grid filled with "~" and print it 
'''
Step 1) Define main(), make a list with 8 squiggles and print it 
'''

import copy
import random
from bakery import assert_equal


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

ships= {(3,4), (5,6)}
grid=[["~", "~", "~", "~", "~", "~", "~", "~"],
      ["~", "~", "~", "~", "~", "~", "~", "~"],
      ["~", "~", "~", "~", "~", "~", "~", "~"],
      ["~", "~", "~", "~", "~", "~", "~", "~"],
      ["~", "~", "~", "~", "~", "~", "~", "~"],
      ["~", "~", "~", "~", "~", "~", "~", "~"],
      ["~", "~", "~", "~", "~", "~", "~", "~"],
      ["~", "~", "~", "~", "~", "~", "~", "~"]]

assert_equal(shoot(ships, grid, set(), 3, 4), "Hit!")
assert_equal(shoot(ships, grid, set(), 2, 4), "Miss!")
assert_equal(shoot(ships, grid, set(), 3, 4), "Repeat!")


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
    
def is_valid_ship(ship: set):
    assert_equal(len(ship), 2)

    coords = list(ship)
    (r1, c1), (r2, c2) = coords #unpacks each value

    for r, c in coords:
        assert_equal(0 <= r <= 7, True)
        assert_equal(0 <= c <= 7, True)

    manhattan_distance = abs(r1 - r2) + abs(c1 - c2)
    assert_equal(manhattan_distance, 1)

def test_ship():
    for i in range(100):
        ship = get_ship()
        is_valid_ship(ship)

test_ship()

def all_ships():
    all=set()
    num=random.randint(3,5)
    while len(all) < num*2:
        ship=get_ship()
        if all.isdisjoint(ship): #checks if two sets have nothing in common
            all.update(ship) #Like append
    return all

def has_duplicates(seq):
    """
    Checks if a sequence (list, tuple, etc.) contains any duplicate elements.
    Returns True if duplicates exist, False otherwise.
    """
    return len(seq) != len(set(seq))


def valid_all_ships(ships: set):
    # len of all is always greater equal to 6
    # Less equal ten 
    # nothing in common
    r=len(ships)
    assert_equal (6 <= r <= 10, True)
    assert_equal(has_duplicates(ships), False)

def test_all_ships():
    for i in range(100):
        ships = all_ships()
        valid_all_ships(ships)

test_all_ships()




#main()
#print(get_ships())
print(all_ships())



'''
    all = set() #should be a set of tuples {}
    num = random.randint(3,6)
    print (num)
    for ship in range(num):
        if ship not in all:
            all.update(get_ships())
    return all
'''

