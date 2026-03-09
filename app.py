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

# ---------------- Custom CSS for styling messages & labels ----------------
st.markdown("""


<style>
/* Title styling */
.stTitle {
    background-color: rgba(25, 118, 210, 0.85);  /* dark blue with transparency */
    color: white;
    padding: 15px;
    border-radius: 8px;
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
}

/* Instructions styling */
.stInstructions {
    background-color: rgba(255, 255, 255, 0.85); /* semi-transparent white */
    color: #0D47A1;  /* dark blue text */
    padding: 12px;
    border-radius: 8px;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    box-shadow: 1px 1px 6px rgba(0,0,0,0.2);
}
.label-highlight {
    font-weight: bold;
    color: #1565C0;         /* dark blue text */
    background-color: rgba(255, 255, 255, 0.85);  /* semi-transparent white */
    padding: 4px 8px;
    border-radius: 5px;
    display: inline-block;
    margin-bottom: 4px;
}
/* Ships Remaining / Shots Remaining labels */
.bold-label {
    background-color: #1565C0;  /* blue label background */
    color: white;                /* white text */
    padding: 5px 10px;
    border-radius: 5px;
    font-weight: bold;
    display: inline-block;
}

/* Fire! and New Game buttons */
div.stButton > button:first-child {
    background-color: #1565C0;
    color: white !important;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
}
div.stButton > button:first-child:disabled {
    background-color: #90A4AE;
    color: #333 !important;
}

/* Hit! / Miss! / Repeat! / Win / Loss messages: white bg + dark text */
.stAlert, .hit-miss-msg {
    background-color: rgba(255, 255, 255, 0.85) !important; /* semi-transparent white */
    color: #0D47A1 !important;  /* dark blue text */
    font-weight: bold;
    border-radius: 8px;
    padding: 10px;
    text-align: center;
    font-size: 16px;
}

/* Grid cells */
.stDataFrame div[data-testid="stDataFrameContainer"] table td {
    background-color: #1E88E5;  /* blue grid background */
    color: white !important;     /* white numbers */
    text-align: center;
    font-weight: bold;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="stTitle">Battleship!</div>', unsafe_allow_html=True)
st.markdown('<div class="stInstructions">Each ship has a length of 2 and there could be 3-5 ships. Good Luck!</div>', unsafe_allow_html=True)

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

# Row label
st.markdown('<div class="label-highlight">Row</div>', unsafe_allow_html=True)
row = st.selectbox("", (0,1,2,3,4,5,6,7), key="row_select")

# Column label
st.markdown('<div class="label-highlight">Column</div>', unsafe_allow_html=True)
col = st.selectbox("", (0,1,2,3,4,5,6,7), key="col_select")

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
    # Ships Remaining label (keep blue background + white text)
    st.markdown('<div class="bold-label">Ships Remaining:</div>', unsafe_allow_html=True)
    # Ships Remaining value (white semi-transparent bg + dark text)
    st.markdown(f'<div class="hit-miss-msg">{st.session_state.ships_remaining}</div>', unsafe_allow_html=True)
    # Shots Remaining label
    st.markdown('<div class="bold-label">Shots Remaining:</div>', unsafe_allow_html=True)
    # Shots Remaining value
    st.markdown(f'<div class="hit-miss-msg">{st.session_state.shots_remaining}</div>', unsafe_allow_html=True)


df = pd.DataFrame(st.session_state.grid)
df_style = df.style.set_properties(**{
    "background-color": "#1976D2",  # matches button/grid theme
    "color": "white",
    "text-align": "center",
    "font-weight": "bold",
    "border-radius": "5px"
})
st.dataframe(df_style)
