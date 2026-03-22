import datetime 
import osmnx as ox
import networkx as nx

def getShortestRoute(start,finish,graph):

        start_node = ox.distance.nearest_nodes(graph, start[0], start[1])
        finish_node = ox.distance.nearest_nodes(graph, finish[0], finish[1])

        route = nx.shortest_path(graph, start_node, finish_node, weight="length")

        route_coord = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in route]

        return route



def route_data(graph, route):
    route_length = 0 # in m
    travel_time = 0 # in s

    for u, v in zip(route[:-1], route[1:]):
        edge_data = graph.get_edge_data(u,v)

        if edge_data:
            edge = list(edge_data.values())[0] # in case there are many route between node u and v (we choose the first one)
            route_length += edge.get("length",0)
            travel_time += graph[u][v][0]['travel_time']
            
    time = str(datetime.timedelta(seconds=int(travel_time)))

    unit = 'm'
    
    if route_length>=1000 and unit == "m":
        route_length = route_length/1000
        unit = 'km'
    
    return f"{route_length:.2f} {unit}", time