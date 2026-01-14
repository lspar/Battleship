import streamlit as st
import pandas as pd 
from game import shoot
from game import all_ships

import copy

st.title("Battleship!")

def make_grid():
        grid= []
        squiggles=["~", "~", "~", "~", "~", "~", "~", "~"]
        for squiggle in range(8):
                grid.append(copy.deepcopy(squiggles))
#for row in grid:
        #st.write(" ".join(row))
        return grid
if "grid" not in st.session_state:
        st.session_state.grid = make_grid()

if "ships" not in st.session_state:
        st.session_state.ships = all_ships()

if "hits" not in st.session_state:
        st.session_state.hits = set()

if "message" not in st.session_state:
        st.session_state.message = ""

if "button_clicked" not in st.session_state:
        st.session_state.button_clicked=False

def reset_game():
        st.session_state.grid=make_grid()
        st.session_state.ships = all_ships()
        st.session_state.hits = set()
        st.session_state.message = ""
        st.session_state.button_clicked=False
if st.button("New Game"):
        reset_game()

def hide_button():
        st.session_state.button_clicked=True




row = st.selectbox("Row",(0,1,2,3,4,5,6,7))
col = st.selectbox("Column", (0,1,2,3,4,5,6,7))

if not st.session_state.button_clicked:
        if st.button("Fire!"):
                st.session_state.message = shoot(st.session_state.ships, st.session_state.grid, st.session_state.hits, row, col)
                st.info(st.session_state.message)
                if st.session_state.hits == st.session_state.ships:
                        st.success("You Win!")
                        hide_button()


df = pd.DataFrame(st.session_state.grid) #creates a table with the grid we made
st.table(df)
