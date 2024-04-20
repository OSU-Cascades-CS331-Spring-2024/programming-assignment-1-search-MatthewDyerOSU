import heapq

def uniformCostSearch(agent_actions, start_city, goal_city):
    frontier = []
    heapq.heappush(frontier, (0, start_city, [start_city]))

    explored = set()

    while frontier:
        current_cost, current_city, path = heapq.heappop(frontier)

        if current_city == goal_city:
            return path, current_cost
        
        if current_city not in explored:
            explored.add(current_city)
            for neighbor, travel_cost in agent_actions.get_possible_moves(current_city):
                if neighbor not in explored:
                    new_cost = current_cost + travel_cost
                    new_path = path + [neighbor]
                    heapq.heappush(frontier, (new_cost, neighbor, new_path))

    return None
        

