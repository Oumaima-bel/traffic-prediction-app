import streamlit as st
import folium
from streamlit_searchbox import st_searchbox
from streamlit_folium import st_folium
import osmnx as ox


from model.map import Map
from services.graphService import load_graph
from services.routeService import route_data
from services.geocodingService import fetch_places, search_places, get_coordinates, get_adresse
from controllers.init_states_controller import set_init_state
from controllers.get_coord_controller import on_click, select_from_map, update_dest_coord, update_start_coord
from controllers.route_controller import compute_route

st.set_page_config(layout = "wide")


G = load_graph()


# initial states

set_init_state()


with st.sidebar:
    start = st_searchbox(
        search_places,
        placeholder="Choose a starting place ...",
        label=st.write("Start"),
        key="start"
        )

    update_start_coord(start, get_coordinates)

    start_button = st.button(
        "Select from the map",
        key="start_button",
        on_click=on_click,
        args=('start',get_adresse,)
        )



    dest = st_searchbox(
        search_places,
        placeholder="Choose the destination ...",
        label=st.write("Destination"),
        key="destination"
        )
    
    update_dest_coord(dest, get_coordinates)

    dest_button = st.button(
        "Select from the map",
        key="dest_button",
        on_click=on_click,
        args=('destination',get_adresse,)
        )

    st.caption("Note : To select a place from the map, click on the desired location, then click the 'Select from the map' button.")

    get_route = st.button('Get Route')

    if st.session_state.route:
        length, time = route_data(G,st.session_state.route)

        st.subheader(f":green[Route length: {length}.]")
        st.subheader(f":orange[Travel time: {time}.]")

    





# show the map and the shortest path

st.write("Map")

my_map = st.session_state.map

if not st.session_state.map_init:
    my_map.map.add_child(folium.LatLngPopup())
    st.session_state.map_init = True


# draw route

if get_route:
    try:
        start = st.session_state.start_coord
        finish = st.session_state.dest_coord

        center = [(start[1] + finish[1])/2 , (start[0] + finish[0])/2]

        st.session_state.map = Map(location=center,zoom_start=14)
        my_map = st.session_state.map
        my_map.map.add_child(folium.LatLngPopup())


        compute_route(my_map,G)

    except Exception as e:
        print(f"Error: {e}")
    

    


map_data = st_folium(my_map.map,height = 600,width = None)

if map_data:
    st.session_state.map_data = map_data



