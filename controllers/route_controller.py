import streamlit as st



def compute_route(my_map,graph):
    if st.session_state.start_coord and st.session_state.dest_coord:

        my_map.addMarker('Start',st.session_state.start_coord)
        my_map.addMarker('Destination',st.session_state.dest_coord)

        st.session_state.route = my_map.getShortestRoute(
            start=st.session_state.start_coord,
            finish=st.session_state.dest_coord,
            graph=graph
        )

        st.session_state.route_coord = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in st.session_state.route]
    
        my_map.addRoute(st.session_state.route_coord)
        st.session_state.route_drawn = True

