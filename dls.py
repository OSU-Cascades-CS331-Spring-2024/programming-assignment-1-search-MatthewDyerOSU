


def depthLimitedSearch(agent_actions, start_city, goal_city, limit):
    num_explored = 0
    num_maintained = 1
    num_expanded = 0

    def recursiveDLS(current_city, goal_city, limit, path, cost, num_explored, num_maintained, num_expanded):
        num_explored += 1
        
        if current_city == goal_city:
            return path, cost, num_explored, num_expanded, num_maintained
        if limit <= 0:
            return None, float('inf'), num_explored, num_expanded, num_maintained
        
        possible_moves = agent_actions.get_possible_moves(current_city)
        num_expanded += len(possible_moves)
        
        for (neighbor, travel_cost) in possible_moves:
            if neighbor not in path:
                num_maintained += 1
                new_path = path + [neighbor]
                new_cost = cost + travel_cost
                result, result_cost, num_explored, num_expanded, num_maintained = recursiveDLS(
                    neighbor, goal_city, limit-1, new_path, new_cost, num_explored, num_maintained, num_expanded
                    )
                if result is not None:
                    return result, result_cost, num_explored, num_expanded, num_maintained
                
        return None, float('inf'), num_explored, num_expanded, num_maintained
    
    return recursiveDLS(start_city, goal_city, limit, [start_city], 0, num_explored, num_maintained, num_expanded)