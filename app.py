import streamlit as st
import numpy as np


from player_list import players

# Create a boolean array of the same length as the number of players
attendance = np.zeros(len(players), dtype=bool)
pods = np.zeros(len(players), dtype=bool)
injuries = np.zeros(len(players), dtype=bool)

ncols =  6

st.image("images/ezgif-7-96cb9745af.jpg", width=150)

game_cols = st.columns(2)
with game_cols[0]:
    date = st.date_input("Match date")
with game_cols[1]:
    time = st.time_input("Kickoff time")

opponent = st.text_input("Opponent", "Opponent team")

cols_head = st.columns(ncols)
with cols_head[0]:
    st.write("Player")
with cols_head[1]:
    st.write("Attended match?")
with cols_head[2]:
    st.write("Forgot to bring pod?")
with cols_head[3]:
    st.write("Got injured?")
with cols_head[4]:
    st.write("Goals scored")
with cols_head[5]:
    st.write("Assists")
    

for i, plyr in enumerate(players):
    cols = st.columns(ncols)
    with cols[0]:
        st.write(plyr)
    with cols[1]:
        attendance[i] = st.checkbox("Attended", label_visibility="collapsed", key=f"attendance_{i}")
    with cols[2]:
        pods[i] = st.checkbox("Forgot pod?", label_visibility="collapsed", key=f"pod_{i}")
    with cols[3]:
        injuries[i] = st.checkbox("Got injured?", label_visibility="collapsed", key=f"injury_{i}")
    with cols[4]:
        st.text_input("Goals", key=f"goals_{i}", label_visibility="collapsed")
    with cols[5]:
        st.text_input("Assits", key=f"assists_{i}", label_visibility="collapsed")

comments = st.text_area("Comments")

st.button("Submit")

