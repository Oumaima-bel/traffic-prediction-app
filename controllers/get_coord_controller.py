import streamlit as st


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
