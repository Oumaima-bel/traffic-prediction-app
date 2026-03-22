import folium
import webbrowser



class Map:
    def __init__(self,location=[34.0084, -6.8539],zoom_start=13):
        self.map = folium.Map(location=location,zoom_start=zoom_start)
    
    def showMap(self):
        self.map.save("map.html")
        webbrowser.open("map.html")
    
    def addMarker(self,marker_name,coord):
        marker = folium.Marker((coord[1],coord[0]),tooltip = marker_name)
        marker.add_to(self.map)

    def addRoute(self,route_coord,color='blue',weight=5):
        folium.PolyLine(route_coord,color=color,weight=weight).add_to(self.map)
    