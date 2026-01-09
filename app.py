import streamlit as st
import copy
st.title("Batttleship")

grid = []
squiggles=["~", "~", "~", "~", "~", "~", "~", "~"]
for squiggle in range(8):
        grid.append(copy.deepcopy(squiggles))
for row in grid:
        st.write(" ".join(row))