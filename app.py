import streamlit as st
import pandas as pd 
from game import shoot
import copy

st.title("Battleship")

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

df = pd.DataFrame(st.session_state.grid) #creates a table with the grid we made
st.table(df)

st.selectbox("Row",(0,1,2,3,4,5,6,7))
st.selectbox("Column", (0,1,2,3,4,5,6,7))