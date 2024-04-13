from queue import Queue

def breadthFirstSearch(agent_actions, start_city, goal_city):
    queue = Queue()
    queue.put(start_city)

    explored = set()
    explored.add(start_city)

    path = {start_city: [start_city]}
    

    while not queue.empty():
        current_city = queue.get()

        if current_city == goal_city:
            path_cost = agent_actions.calculate_path_cost(path[current_city])
            return path[current_city], path_cost
        
        explored.add(current_city)
        possible_moves = agent_actions.get_possible_moves(current_city)

        for neighbor, _ in possible_moves:
            if neighbor not in explored:
                path[neighbor] = path[current_city] + [neighbor]
                queue.put(neighbor)
    return None
        

