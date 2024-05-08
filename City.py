import math

class City:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.connections = {}

    def add_connections(self, other_city, distance):
        self.connections[other_city] = distance

    def get_connections(self):
        return ", ".join(f"{city} {dist}" for city, dist in self.connections.items())
    
    def parse_coordinates(self):
        parts = self.coordinates.split()
        lat_deg, lat_min, lat_sec, lat_dir = parts[:4]
        lon_deg, lon_min, lon_sec, lon_dir = parts[4:]

        lat = self.dms_to_decimal(float(lat_deg), float(lat_min), float(lat_sec), lat_dir)
        lon = self.dms_to_decimal(float(lon_deg), float(lon_min), float(lon_sec), lon_dir)
        return lat, lon

    def dms_to_decimal(self, deg, min, sec, direction):
        decimal = deg + (min / 60) + (sec / 3600)
        if direction in ['S', 'W']:
            decimal = -decimal
        return decimal
    
    def get_distance(self, other_city):
        return self.connections.get(other_city, None)
    
    def euclidean_distance_to(self, other_city):
        lat1, lon1 = self.parse_coordinates()
        lat2, lon2 = other_city.parse_coordinates()
        return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
    
    def __str__(self):
        connections = self.get_connection_info()
        return f"City: {self.name}, Coordinates: {self.coordinates}, Connections: {connections}"