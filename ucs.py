import heapq

def uniformCostSearch(agent_actions, start_city, goal_city):
    frontier = []
    heapq.heappush(frontier, (0, start_city, [start_city]))
    explored = set()

    num_explored = 0
    num_expanded = 0
    num_maintained = 0

    while frontier:
        current_cost, current_city, path = heapq.heappop(frontier)
        num_explored += 1

        if current_city == goal_city:
            return path, current_cost, num_explored, num_expanded, num_maintained
        
        if current_city not in explored:
            explored.add(current_city)
            possible_moves = agent_actions.get_possible_moves(current_city)
            num_expanded += len(possible_moves)

            for neighbor, travel_cost in possible_moves:
                if neighbor not in explored:
                    new_cost = current_cost + travel_cost
                    new_path = path + [neighbor]
                    heapq.heappush(frontier, (new_cost, neighbor, new_path))
                    num_maintained += 1

    return None, None, num_explored, num_expanded, num_maintained
        

