import streamlit as st
import pandas as pd 
from game import shoot, all_ships, make_grid, ship_tracker, shot_limit, shot_countdown
import copy

st.title("Battleship!")

make_grid()

if "grid" not in st.session_state:
        st.session_state.grid = make_grid()

if "ships" not in st.session_state:
        st.session_state.allcoords, st.session_state.ships = all_ships()

if "hits" not in st.session_state:
        st.session_state.hits = set()

if "message" not in st.session_state:
        st.session_state.message = ""

if "ships_remaining" not in st.session_state:
        st.session_state.ships_remaining= ship_tracker(st.session_state.ships, st.session_state.hits)

if "total_shots" not in st.session_state:
        st.session_state.total_shots = 0

def reset_game():
        st.session_state.grid=make_grid()
        st.session_state.allcoords, st.session_state.ships = all_ships()
        st.session_state.hits = set()
        st.session_state.message = ""
        st.session_state.ships_remaining= ship_tracker(st.session_state.ships, st.session_state.hits)
        st.session_state.total_shots = 0

if st.button("New Game"):
        reset_game()


row = st.selectbox("Row",(0,1,2,3,4,5,6,7))
col = st.selectbox("Column", (0,1,2,3,4,5,6,7))

col1, col2 = st.columns(2, gap="small")

def play_game(selected_row, selected_col):
        with col1: 
                fire_disabled = st.session_state.hits == st.session_state.allcoords
                if st.button("Fire!", disabled=fire_disabled):
                        st.session_state.message = shoot(st.session_state.allcoords, st.session_state.grid, 
                                                        st.session_state.hits, st.session_state.total_shots, selected_row, selected_col)
                        st.session_state.ships_remaining = ship_tracker(st.session_state.ships, st.session_state.hits)
                        st.info(st.session_state.message)
                        fire_disabled = st.session_state.hits == st.session_state.allcoords
                if fire_disabled:
                        st.success("You Win!")

play_game(row,col)

with col2:
        st.write("Ships Remaining: ")
        st.info(str(st.session_state.ships_remaining))
        st.write("Shots Remaining: ")
        st.warning(str(shot_countdown(st.session_state.ships, st.session_state.total_shots)))


df = pd.DataFrame(st.session_state.grid) #creates a table with the grid we made
st.table(df)
