import datetime 

def route_data(graph, route):
    route_length = 0 # in m
    travel_time = 0 # in s

    for u, v in zip(route[:-1], route[1:]):
        edge_data = graph.get_edge_data(u,v)

        # print(graph[u][v][0]['speed_kph'])

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