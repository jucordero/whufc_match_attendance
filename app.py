import streamlit as st
import pandas as pd
import numpy as np


from player_list import players

# Create a boolean array of the same length as the number of players
attendance = np.zeros(len(players), dtype=bool)
pods = np.zeros(len(players), dtype=bool)

ncols =  6

cols_head = st.columns(ncols)
with cols_head[0]:
    st.write("Player")
with cols_head[1]:
    st.write("Attended")
with cols_head[2]:
    st.write("Brought pod to training")
with cols_head[3]:
    st.write("Goals scored")
with cols_head[4]:
    st.write("Assists")
    

for i, plyr in enumerate(players):
    cols = st.columns(ncols)
    with cols[0]:
        st.write("")
        st.write("")
        st.write("")
        st.write(plyr)
    with cols[1]:
        st.write("")
        st.write("")
        attendance[i] = st.checkbox("Attended", label_visibility="hidden", key=f"attendance_{i}")
    with cols[2]:
        st.write("")
        st.write("")
        pods[i] = st.checkbox("Pod", label_visibility="hidden", key=f"pod_{i}")
    with cols[3]:
        st.text_input("Goals", key=f"goals_{i}", label_visibility="hidden")
    with cols[4]:
        st.text_input("Assits", key=f"assists_{i}", label_visibility="hidden")

