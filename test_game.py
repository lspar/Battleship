
from game import get_ship, shoot, all_ships, make_grid, ship_tracker
from app import play_game, reset_game
import pytest
from unittest.mock import patch
import streamlit as st

def test_make_grid():
    grid=make_grid()
    assert len(grid)==8 #check that the grid has 8 rows
    for row in grid:
        assert len(row)==8
        for cell in row:
            assert cell== "🌊"
    grid[0][0] = "🚢"
    assert grid[1][0]== "🌊"

def test_shoot():
    coords= {(3,4), (5,6)}
    grid = make_grid()
    hits = set()
    assert shoot(coords, grid, hits, 3,4) == "Hit!"
    assert shoot(coords, grid, hits, 5,6) == "Hit!"
    assert shoot(coords, grid, hits, 2, 4) == "Miss!"
    assert shoot(coords, grid, hits, 3, 4) =="Repeat!"


def is_valid_ship(ship: set):
    assert len(ship) == 2

    coords = list(ship)
    (r1, c1), (r2, c2) = coords #unpacks each value

    for r, c in coords:
        assert 0 <= r <= 7
        assert 0 <= c <= 7

    #checks that one coordinate is one block away from the other
    manhattan_distance = abs(r1 - r2) + abs(c1 - c2)
    assert manhattan_distance == 1

def test_ship():
    for i in range(20):
        ship = get_ship()
        is_valid_ship(ship)


def has_duplicates(seq):
    """
    Checks if a sequence (list, tuple, etc.) contains any duplicate elements.
    Returns True if duplicates exist, False otherwise.
    """
    return len(seq) != len(set(seq))


def valid_all_ships(ships: list, coords:set):
    # len of all is always greater equal to 6
    # Less equal ten 
    # nothing in common
    num_ships=len(ships)
    assert 3 <= num_ships <= 5
    assert has_duplicates(coords) ==False

def test_all_ships():
    for i in range(100):
        coords, ships = all_ships()
        valid_all_ships(ships, coords)


def test_reset_game():
    st.session_state.clear()
    st.session_state.grid= make_grid()
    st.session_state.ships = [{(4,3), (6,7)}]
    st.session_state.hits = {(4,3), (6,7)}
    st.session_state.message = "You Win!"
    st.session_state.button_clicked=True

    reset_game()

    assert len(st.session_state.grid)==8
    for row in st.session_state.grid:
        assert len(row)==8
        for cell in row:
            assert cell== "🌊"
    
    assert isinstance(st.session_state.hits, set)
    assert 3<= len(st.session_state.ships) <= 5
    assert st.session_state.hits==set()
    assert st.session_state.button_clicked is False
    assert st.session_state.message==""


#Streamlit Mocks

def test_play_game():
    st.session_state.clear()
    st.session_state.grid = make_grid()
    st.session_state.allcoords, st.session_state.ships = {(3,4),(3,3)}, [{(3,4),(3,3)}]
    st.session_state.hits = set()
    st.session_state.message = ""
    st.session_state.button_clicked = False

    with patch("app.st.button", return_value=True), \
        patch("app.st.info") as mock_info, \
        patch ("app.st.success") as mock_success:
        
        print("BEFORE FIRING:")
        print("hits: ", st.session_state.hits)
        print("ships:", st.session_state.ships)
        play_game(3, 4)
        print("AFTER FIRING:")
        print("hits:", st.session_state.hits)
        print("ships:", st.session_state.ships)
    
        mock_info.assert_called_once_with(st.session_state.message)
        mock_info.reset_mock() # Give it another button click to simulate firing multiple times
        play_game(3,3)
        mock_info.assert_called_once_with(st.session_state.message)
        assert st.session_state.hits == {(3, 4), (3, 3)}
        assert st.session_state.hits == st.session_state.allcoords
        mock_success.assert_called_once_with("You Win!")
        


            
        #assert st.session_state.button_clicked is True

def test_ship_tracker():
    ships=[{(3,3), (3,4)}, {(2,2), (2,1)}]
    assert ship_tracker(ships, {(3,3), (3,4), (2,2), (2,1)}) == 0
    assert ship_tracker(ships, {(3,3), (3,4)}) == 1
    assert ship_tracker(ships, set()) == 2
    

#num_ships decreases by 1 everytime that shoot() return Hit!
# if shoot ==Hit assert num_ships -1 == True
#decreases num by 1 only when it is a hit