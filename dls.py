


def depthLimitedSearch(agent_actions, start_city, goal_city, limit):

    def recursiveDLS(current_city, goal_city, limit, path, cost):
        if current_city == goal_city:
            return path, cost
        if limit <= 0:
            return None, float('inf')
        
        for (neighbor, travel_cost) in agent_actions.get_possible_moves(current_city):
            if neighbor not in path:
                new_path = path + [neighbor]
                new_cost = cost + travel_cost
                result, result_cost = recursiveDLS(neighbor, goal_city, limit-1, new_path, new_cost)
                if result is not None:
                    return result, result_cost
                
        return None, float('inf')
    
    return recursiveDLS(start_city, goal_city, limit, [start_city], 0)