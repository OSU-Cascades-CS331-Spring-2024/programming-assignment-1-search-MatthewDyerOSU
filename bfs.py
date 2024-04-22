from queue import Queue

def breadthFirstSearch(agent_actions, start_city, goal_city):
    queue = Queue()
    queue.put(start_city)
    num_explored = 0
    num_maintained = 1
    num_expanded = 0

    explored = set()
    explored.add(start_city)

    path = {start_city: [start_city]}
    
    while not queue.empty():
        current_city = queue.get()
        num_explored += 1

        if current_city == goal_city:
            path_cost = agent_actions.calculate_path_cost(path[current_city])
            return path[current_city], path_cost, num_explored, num_expanded, num_maintained
        
        possible_moves = agent_actions.get_possible_moves(current_city)
        num_expanded += len(possible_moves)

        for neighbor, _ in possible_moves:
            if neighbor not in explored and neighbor not in queue.queue:
                path[neighbor] = path[current_city] + [neighbor]
                queue.put(neighbor)
                explored.add(neighbor)
                num_maintained += 1
    
    return None
        

