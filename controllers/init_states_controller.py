import streamlit as st

from model.map import Map



def set_init_state():
    if 'map_data' not in st.session_state:
        st.session_state.map_data = None

    if 'map' not in st.session_state:
        st.session_state.map = Map()

    if 'map_init' not in st.session_state:
        st.session_state.map_init = False

    if 'last_start' not in st.session_state:
        st.session_state.last_start = None

    if 'last_dest' not in st.session_state:
        st.session_state.last_dest = None

    if 'start_coord' not in st.session_state:
        st.session_state.start_coord = None

    if 'dest_coord' not in st.session_state:
        st.session_state.dest_coord = None
    
    if 'route' not in st.session_state:
        st.session_state.route = None

