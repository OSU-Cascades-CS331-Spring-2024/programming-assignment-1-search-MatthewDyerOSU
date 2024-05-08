from City import City

class CityMap:
    def __init__(self, filename):
        self.cities = {}
        self.load_map(filename)

    def load_map(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if '-->' in line:
                    city_info, connections_str = line.split(' --> ')
                    city_name, *coordinates = city_info.split()
                    city = City(city_name, ' '.join(coordinates))
                    connections = connections_str.split('va-')
                    for conn in connections:
                        parts = conn.split()
                        if len(parts) == 2:
                            connected_city, distance = parts
                            city.add_connections(connected_city, int(distance))
                    self.cities[city_name] = city

    def get_city_info(self, city_name):
        return self.cities.get(city_name, None)
    
    def get_connections(self, city_name):
        city_info = self.get_city_info(city_name)
        return city_info['connections'] if city_info else None