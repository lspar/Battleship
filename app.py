import streamlit as st
import pandas as pd 
from game import shoot
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
        st.session_state.ships = {(1,2), (1,3)}

if "hits" not in st.session_state:
        st.session_state.hits = set()

if "message" not in st.session_state:
        st.session_state.message = ""


row = st.selectbox("Row",(0,1,2,3,4,5,6,7))
col = st.selectbox("Column", (0,1,2,3,4,5,6,7))
if st.button("Fire!"):
        st.session_state.message = shoot(st.session_state.ships, st.session_state.grid, st.session_state.hits, row, col)
        if st.session_state.message == "Hit!":
                st.info("Hit!")
        elif st.session_state.message == "Miss!":
                st.info("Miss!")
        else:
                st.info("Repeat!")

df = pd.DataFrame(st.session_state.grid) #creates a table with the grid we made
st.table(df)
