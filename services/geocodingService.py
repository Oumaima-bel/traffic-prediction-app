import streamlit as st
import osmnx as ox
from geopy.geocoders import Nominatim


@st.cache_data
def fetch_places(query):
    try:
        return ox.geocode_to_gdf(query+", Rabat, Morocco", which_result=None)
        
    except:
        return None




def search_places(query):
    if len(query)<3:
        return []

    try:
        gdf = fetch_places(query)
        return gdf["display_name"].head().tolist()

    except:
        return []


@st.cache_data
def get_coordinates(place_name):
    try:
        gdf = ox.geocode_to_gdf(place_name, which_result=None)
        point = gdf.geometry.iloc[0].centroid    
        return (point.x, point.y)
    except:
        return None



@st.cache_data
def get_adresse(lat,lng):
    geolocator = Nominatim(user_agent = "my_app")
    place_details = geolocator.reverse((lng, lat))
    return place_details.address if place_details else None