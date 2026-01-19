
from game import get_ship, shoot, all_ships, make_grid
import pytest

def test_make_grid():
    grid=make_grid()
    assert len(grid)==8 #check that the grid has 8 rows
    for row in grid:
        assert len(row)==8
        for cell in row:
            assert cell== "~"
    grid[0][0] = "X"
    assert grid[1][0]== "~"

def test_shoot():
    ships= {(3,4), (5,6)}
    
    
assert_equal(shoot(ships, grid, set(), 3, 4), "Hit!")
assert_equal(shoot(ships, grid, set(), 2, 4), "Miss!")
assert_equal(shoot(ships, grid, set(), 3, 4), "Repeat!")

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
    for i in range(20):
        ship = get_ship()
        is_valid_ship(ship)

test_ship()

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
