
from game import get_ship, shoot, all_ships, make_grid
from app import play_game
import pytest
from unittest.mock import patch
import streamlit as st

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
    grid = make_grid()
    hits = set()
    assert shoot(ships, grid, hits, 3,4) == "Hit!"
    assert shoot(ships, grid, hits, 5,6) == "Hit!"
    assert shoot(ships, grid, hits, 2, 4) == "Miss!"
    assert shoot(ships, grid, hits, 3, 4) =="Repeat!"


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


def valid_all_ships(ships: set):
    # len of all is always greater equal to 6
    # Less equal ten 
    # nothing in common
    r=len(ships)
    assert 6 <= r <= 10
    assert has_duplicates(ships) ==False

def test_all_ships():
    for i in range(100):
        ships = all_ships()
        valid_all_ships(ships)

def test_play_game():
    st.session_state.clear()
    st.session_state.grid = make_grid()
    st.session_state.ships = {(3,4)}
    st.session_state.hits = set()
    st.session_state.message = ""
    st.session_state.button_clicked = False

    with patch("streamlit.button", return_value=True), \
        patch("streamlit.info") as mock_info:
        
        print("BEFORE FIRING:")
        print("hits: ", st.session_state.hits)
        print("ships:", st.session_state.ships)
        play_game(3, 4)
        print("AFTER FIRING:")
        print("hits:", st.session_state.hits)
        print("ships:", st.session_state.ships)

        mock_info.assert_called_once_with(st.session_state.message)
        assert st.session_state.hits == {(3, 4)}
        assert st.session_state.button_clicked is False
        
        
