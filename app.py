import streamlit as st
import pandas as pd 
from game import shoot, all_ships, make_grid
import copy

st.title("Battleship!")

make_grid()

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


row = st.selectbox("Row",(0,1,2,3,4,5,6,7))
col = st.selectbox("Column", (0,1,2,3,4,5,6,7))


def play_game(selected_row, selected_col):
        if not st.session_state.button_clicked:
                if st.button("Fire!"):
                        st.session_state.message = shoot(st.session_state.ships, st.session_state.grid, st.session_state.hits, selected_row, selected_col)
                        st.info(st.session_state.message)
                        win_game()



def win_game ():
        if st.session_state.hits == st.session_state.ships:
                st.success("You Win!")
                st.session_state.button_clicked=True



play_game(row,col)

df = pd.DataFrame(st.session_state.grid) #creates a table with the grid we made
st.table(df)
