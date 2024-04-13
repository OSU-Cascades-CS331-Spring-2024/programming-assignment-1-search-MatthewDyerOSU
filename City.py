

class City:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.connections = {}

    def add_connections(self, other_city, distance):
        self.connections[other_city] = distance

    def get_connections(self):
        return ", ".join(f"{city} {dist}" for city, dist in self.connections.items())
    
    def get_distance(self, other_city):
        return self.connections.get(other_city, None)
    
    def __str__(self):
        connections = self.get_connection_info()
        return f"City: {self.name}, Coordinates: {self.coordinates}, Connections: {connections}"