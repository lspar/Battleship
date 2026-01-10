import streamlit as st
import pandas as pd 
import copy
st.title("Batttleship")

grid = []
squiggles=["~", "~", "~", "~", "~", "~", "~", "~"]
for squiggle in range(8):
        grid.append(copy.deepcopy(squiggles))
#for row in grid:
        #st.write(" ".join(row))

df = pd.DataFrame(grid) #creates a table with the grid we made
st.table(df)

if "grid" not in st.session_state:
        st.session_state.grid = []

if "ships" not in st.session_state:
        st.session_state.ships = []

if "hits" not in st.session_state:
        st.session_state.hits = set()