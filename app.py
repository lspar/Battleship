import streamlit as st
import pandas as pd 
from game import shoot, all_ships, make_grid, ship_tracker, shot_limit, shot_countdown
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Call the function with your image file name
set_png_as_page_bg('Battleship Image.jpg') 



st.title("Battleship!")
st.write("Each ship has a legnth of 2 and there could be 3-5 ships. Good Luck!")

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

if "shots_remaining" not in st.session_state:
        st.session_state.shots_remaining = shot_countdown(st.session_state.ships, st.session_state.total_shots)

def reset_game():
        st.session_state.grid=make_grid()
        st.session_state.allcoords, st.session_state.ships = all_ships()
        st.session_state.hits = set()
        st.session_state.message = ""
        st.session_state.ships_remaining= ship_tracker(st.session_state.ships, st.session_state.hits)
        st.session_state.total_shots = 0
        st.session_state.shots_remaining = shot_countdown(st.session_state.ships, st.session_state.total_shots)

if st.button("New Game"):
        reset_game()


row = st.selectbox("Row",(0,1,2,3,4,5,6,7))
col = st.selectbox("Column", (0,1,2,3,4,5,6,7))

col1, col2 = st.columns(2, gap="small")

def play_game(selected_row, selected_col):
        with col1: 
                fire_disabled = st.session_state.hits == st.session_state.allcoords or st.session_state.shots_remaining == 0
                if st.button("Fire!", disabled=fire_disabled):
                        st.session_state.message = shoot(st.session_state.allcoords, st.session_state.grid, 
                                                        st.session_state.hits, selected_row, selected_col)
                        if st.session_state.message != "Repeat!":
                                st.session_state.total_shots +=1
                        st.session_state.ships_remaining = ship_tracker(st.session_state.ships, st.session_state.hits)
                        st.session_state.shots_remaining = shot_countdown(st.session_state.ships, st.session_state.total_shots)
                        st.info(st.session_state.message)
                        fire_disabled = st.session_state.hits == st.session_state.allcoords or st.session_state.shots_remaining == 0
                if fire_disabled:
                        if st.session_state.hits == st.session_state.allcoords:
                                st.success("You Win!")
                        if st.session_state.shots_remaining ==  0:
                                st.error("Sorry, You Lost!")

play_game(row,col)

with col2:
        st.write("Ships Remaining: ")
        st.info(str(st.session_state.ships_remaining))
        st.write("Shots Remaining: ")
        st.warning(str(st.session_state.shots_remaining))


df = pd.DataFrame(st.session_state.grid) #creates a table with the grid we made
st.table(df)
