
from game import get_ship, shoot, all_ships, make_grid, ship_tracker, shot_limit, shot_countdown
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
    shots = 16
    assert shoot(coords, grid, hits, shots, 3,4) == "Hit!"
    assert shoot(coords, grid, hits, shots, 5,6) == "Hit!"
    assert shoot(coords, grid, hits, shots, 2, 4) == "Miss!"
    assert shoot(coords, grid, hits, shots, 3, 4) =="Repeat!"


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
    st.session_state.shots_limit= shot_limit(st.session_state.ships)

    reset_game()

    assert len(st.session_state.grid)==8
    for row in st.session_state.grid:
        assert len(row)==8
        for cell in row:
            assert cell== "🌊"
    
    assert isinstance(st.session_state.hits, set)
    assert 3<= len(st.session_state.ships) <= 5
    assert st.session_state.hits==set()
    assert st.session_state.message==""


#Streamlit Mocks

def test_play_game():
    st.session_state.clear()
    st.session_state.grid = make_grid()
    st.session_state.allcoords, st.session_state.ships = {(3,4),(3,3)}, [{(3,4),(3,3)}]
    st.session_state.hits = set()
    st.session_state.message = ""
    st.session_state.shot_limit= shot_limit(st.session_state.ships)

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

def test_shot_limit():
    ships3 = [{(3,3), (3,4)}, {(2,2), (2,1)}, {(1,2), (1,1)}]
    ships4 = [{(3,3), (3,4)}, {(2,2), (2,1)}, {(1,2), (1,1)}, {(0,0), (0,1)}]
    ships5 = [{(3,3), (3,4)}, {(2,2), (2,1)}, {(1,2), (1,1)}, {(0,0), (0,1)}, {(5,5), (5,4)}]
    assert shot_limit(ships3) ==16
    assert shot_limit(ships4) ==20
    assert shot_limit(ships5) ==25

def test_shot_countdown():
    ships3 = [{(3,3), (3,4)}, {(2,2), (2,1)}, {(1,2), (1,1)}]
    ships4 = [{(3,3), (3,4)}, {(2,2), (2,1)}, {(1,2), (1,1)}, {(0,0), (0,1)}]
    ships5 = [{(3,3), (3,4)}, {(2,2), (2,1)}, {(1,2), (1,1)}, {(0,0), (0,1)}, {(5,5), (5,4)}]
    assert shot_countdown(ships3, 16) == "Sorry, You Lost!"
    assert shot_countdown(ships4, 20) == "Sorry, You Lost!"
    assert shot_countdown(ships5, 25) == "Sorry, You Lost!"
    

#num_ships decreases by 1 everytime that shoot() return Hit!
# if shoot ==Hit assert num_ships -1 == True
#decreases num by 1 only when it is a hit