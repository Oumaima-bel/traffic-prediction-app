import streamlit as st

from model.map import Map
from services.route_service import getShortestRoute



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



def compute_route(my_map,graph):
    if st.session_state.start_coord and st.session_state.dest_coord:

        my_map.addMarker('Start',st.session_state.start_coord)
        my_map.addMarker('Destination',st.session_state.dest_coord)

        st.session_state.route = getShortestRoute(
            start=st.session_state.start_coord,
            finish=st.session_state.dest_coord,
            graph=graph
        )

        st.session_state.route_coord = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in st.session_state.route]
    
        my_map.addRoute(st.session_state.route_coord)
        st.session_state.route_drawn = True



def update_start_coord(start,get_coordinates):
    if start and start != st.session_state.get("last_start"):
        st.session_state.start_coord = get_coordinates(start)
        st.session_state.last_start = start



def update_dest_coord(dest,get_coordinates):
    if dest and dest != st.session_state.get("last_dest"):
        st.session_state.dest_coord = get_coordinates(dest)
        st.session_state.last_dest = dest




def select_from_map():
    data = st.session_state.map_data
    if data and 'last_clicked' in data and data["last_clicked"] is not None:
        lat = data['last_clicked']['lat']
        lng = data['last_clicked']['lng']

        return lng, lat
    return None




def on_click(goal,get_adresse):
    coord = select_from_map()
    

    if coord:
        adresse = get_adresse(*coord)

        if goal == 'start':
            st.session_state.start_coord = coord
            st.session_state.last_start = adresse

        elif goal == 'destination':
            st.session_state.dest_coord = coord
            st.session_state.last_dest = adresse