import heapq

def aStarSearch(agent_actions, start_city, goal_city):
    start_city_obj = agent_actions.city_map.cities[start_city]
    goal_city_obj = agent_actions.city_map.cities[goal_city]

    frontier = []
    heapq.heappush(frontier, (0 + start_city_obj.euclidean_distance_to(goal_city_obj), [start_city], 0))
    explored = set()

    num_explored = 0
    num_expanded = 0
    num_maintained = 0

    while frontier:
        f_cost, path, g_cost = heapq.heappop(frontier)
        num_explored += 1
        current_city = path[-1]

        if current_city == goal_city:
            return path, g_cost, num_explored, num_expanded, num_maintained
        
        if current_city not in explored:
            explored.add(current_city)
            current_city_obj = agent_actions.city_map.cities[current_city]
            possible_moves = agent_actions.get_possible_moves(current_city)
            num_expanded += len(possible_moves)

            for neighbor, travel_cost in possible_moves:
                if neighbor not in explored:
                    new_g_cost = g_cost + travel_cost
                    neighbor_city_obj = agent_actions.city_map.cities[neighbor]
                    new_f_cost = new_g_cost + neighbor_city_obj.euclidean_distance_to(goal_city_obj)
                    new_path = path + [neighbor]
                    heapq.heappush(frontier, (new_f_cost, new_path, new_g_cost))
                    num_maintained += 1

    return None, float('inf'), num_explored, num_expanded, num_maintained
