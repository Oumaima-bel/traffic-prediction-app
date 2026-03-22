import streamlit as st
import osmnx as ox


@st.cache_data
def load_graph():
    graph = ox.io.load_graphml("./data/graph.graphml")
    ox.add_edge_speeds(graph)
    ox.add_edge_travel_times(graph)

    return graph





def save_graph(file_path,place):
    G = ox.graph_from_place(place, network_type="drive")
    ox.io.save_graphml(G,file_path)