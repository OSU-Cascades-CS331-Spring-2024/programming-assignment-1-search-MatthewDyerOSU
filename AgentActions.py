

class AgentActions:
    def __init__(self, city_map):
        self.city_map = city_map

    def get_possible_moves(self, current_city):
        city = self.city_map.cities.get(current_city)
        if city:
            return list(city.connections.items())
        else:
            return []
        
    def move_to_city(self, current_city, next_city):
        if next_city in self.city_map.cities[current_city].connections:
            return self.city_map.cities[current_city].connections[next_city]
        else:
            return float('inf')
        
    def calculate_path_cost(self, path):
        cost = 0
        for i in range(len(path)-1):
            cost += self.move_to_city(path[i], path[i+1])
        return cost