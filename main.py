import argparse
from CityMap import CityMap
from AgentActions import AgentActions
from bfs import breadthFirstSearch
from ucs import uniformCostSearch
from dls import depthLimitedSearch
from astar import aStarSearch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-S', type=str, required=False, default='bfs', help='Type of search algorithm to be used')
    parser.add_argument('-A', type=str, required=False, help='The initial city to start the search from')
    parser.add_argument('-B', type=str, required=False, help='The goal city the search will try to navigate to')
    parser.add_argument('-M', type=str, required=True, help='The name of the file the map will be retrieved from')
    args = parser.parse_args()

    city_map = CityMap(args.M)
    agent_actions = AgentActions(city_map)

    if args.A and args.B:
        if args.S == "bfs":
            path, path_cost, num_explored, num_expanded, num_maintained = breadthFirstSearch(agent_actions, args.A, args.B)
            if path:
                print("BFS Path found:", " -> ".join(path))
                print("BFS Path Cost:", path_cost)
                print("BFS Explored:", num_explored)
                print("BFS Expanded", num_expanded)
                print("BFS Maintained:", num_maintained)
            else:
                print("No path found between", args.A, "and", args.B)
        elif args.S == "dls":
            path, path_cost, num_explored, num_expanded, num_maintained = depthLimitedSearch(agent_actions, args.A, args.B, 7)
            if path:
                print("DLS Path found:", " -> ".join(path))
                print("DLS Path cost:", path_cost)
                print("DLS Explored:", num_explored)
                print("DLS Expanded", num_expanded)
                print("DLS Maintained:", num_maintained)
            else:
                print("No path found between", args.A, "and", args.B, "within depth limit")
        elif args.S == "ucs":
            path, path_cost, num_explored, num_expanded, num_maintained = uniformCostSearch(agent_actions, args.A, args.B)
            if path:
                print("UCS Path found:", " -> ".join(path))
                print("UCS Path Cost", path_cost)
                print("UCS Explored:", num_explored)
                print("UCS Expanded", num_expanded)
                print("UCS Maintained :", num_maintained)
            else:
                print("No path found between", args.A, "and", args.B)
        elif args.S == "astar":
            path, cost, num_explored, num_expanded, num_maintained = aStarSearch(agent_actions, args.A, args.B)
            if path:
                print("A* Path found:", " -> ".join(path))
                print("A* Path cost:", cost)
                print("A* Explored:", num_explored)
                print("A* Expanded", num_expanded)
                print("A* Maintained:", num_maintained)
            else:
                print("No path found from", initial_cities[i], "to", goal_cities[i])



    if args.A is None or args.B is None:
        initial_cities = ["brest", "montpellier", "strasbourg", "paris", "grenoble", "brest", "grenoble", "nice", "caen"]
        goal_cities = ["nice", "calais", "bordeaux", "grenoble", "paris", "grenoble", "brest", "nantes", "strasbourg"]

        bfs_explored_total = 0
        bfs_expanded_total = 0
        bfs_maintained_total = 0

        ucs_explored_total = 0
        ucs_expanded_total = 0
        ucs_maintained_total = 0

        dls_explored_total = 0
        dls_expanded_total = 0
        dls_maintained_total = 0

        astar_explored_total = 0
        astar_expanded_total = 0
        astar_maintained_total = 0

        wins = {
            "BFS": 0,
            "UCS": 0,
            "DLS": 0,
            "A*": 0
        }

        with open('solutions.txt', 'w') as file:
            for i in range(9):
                path, bfs_path_cost, num_explored, num_expanded, num_maintained = breadthFirstSearch(agent_actions, initial_cities[i], goal_cities[i])
                if path:
                    bfs_explored_total += num_explored
                    bfs_expanded_total += num_expanded
                    bfs_maintained_total += num_maintained
                    print("BFS Path found:", " -> ".join(path), file=file)
                    print("BFS Path Cost:", bfs_path_cost, file=file)
                    print("BFS Explored:", num_explored, file=file)
                    print("BFS Expanded", num_expanded, file=file)
                    print("BFS Maintained:", num_maintained, file=file)
                else:
                    print("No path found between", initial_cities[i], "and", goal_cities[i], file=file)

                path, ucs_path_cost, num_explored, num_expanded, num_maintained = uniformCostSearch(agent_actions, initial_cities[i], goal_cities[i])
                if path:
                    ucs_explored_total += num_explored
                    ucs_expanded_total += num_expanded
                    ucs_maintained_total += num_maintained
                    print("UCS Path found:", " -> ".join(path), file=file)
                    print("UCS Path Cost", ucs_path_cost, file=file)
                    print("UCS Explored:", num_explored, file=file)
                    print("UCS Expanded", num_expanded, file=file)
                    print("UCS Maintained :", num_maintained, file=file)
                else:
                    print("No path found between", initial_cities[i], "and", goal_cities[i], file=file)

                path, dls_path_cost, num_explored, num_expanded, num_maintained = depthLimitedSearch(agent_actions, initial_cities[i], goal_cities[i], 5)
                if path:
                    dls_explored_total += num_explored
                    dls_expanded_total += num_expanded
                    dls_maintained_total += num_maintained
                    print("DLS Path found:", " -> ".join(path), file=file)
                    print("DLS Path cost:", dls_path_cost, file=file)
                    print("DLS Explored:", num_explored, file=file)
                    print("DLS Expanded", num_expanded, file=file)
                    print("DLS Maintained:", num_maintained, file=file)
                else:
                    print("No path found within depth limit from", initial_cities[i], "to", goal_cities[i], file=file)

                path, astar_path_cost, num_explored, num_expanded, num_maintained = aStarSearch(agent_actions, initial_cities[i], goal_cities[i])
                if path:
                    astar_explored_total += num_explored
                    astar_expanded_total += num_expanded
                    astar_maintained_total += num_maintained
                    print("A* Path found:", " -> ".join(path), file=file)
                    print("A* Path cost:", astar_path_cost, file=file)
                    print("A* Explored:", num_explored, file=file)
                    print("A* Expanded", num_expanded, file=file)
                    print("A* Maintained:", num_maintained, file=file)
                else:
                    print("No path found from", initial_cities[i], "to", goal_cities[i], file=file)
            
                costs = {
                    "BFS": bfs_path_cost,
                    "UCS": ucs_path_cost,
                    "DLS": dls_path_cost,
                    "A*": astar_path_cost
                }

                lowest_cost = min(costs, key=costs.get)
                wins[lowest_cost] += 1

        with open('README.md', 'w') as file:
            print("BFS Average Number of Cities Explored:", bfs_explored_total/9, file=file)
            print("BFS Average Number of Cities Expanded:", bfs_expanded_total/9, file=file) 
            print("BFS Average Number of Cities Maintained:", bfs_maintained_total/9, file=file) 
            print("BFS Number of Times it Found Optimal Solution:", wins["BFS"], file=file)

            print("UCS Average Number of Cities Explored:", ucs_explored_total/9, file=file)
            print("UCS Average Number of Cities Expanded:", ucs_expanded_total/9, file=file) 
            print("UCS Average Number of Cities Maintained:", ucs_maintained_total/9, file=file) 
            print("UCS Number of Times it Found Optimal Solution:", wins["UCS"], file=file) 

            print("DLS Average Number of Cities Explored:", dls_explored_total/9, file=file)
            print("DLS Average Number of Cities Expanded:", dls_expanded_total/9, file=file) 
            print("DLS Average Number of Cities Maintained:", dls_maintained_total/9, file=file) 
            print("DLS Number of Times it Found Optimal Solution:", wins["DLS"], file=file)   

            print("A* Average Number of Cities Explored:", astar_explored_total/9, file=file)
            print("A* Average Number of Cities Expanded:", astar_expanded_total/9, file=file) 
            print("A* Average Number of Cities Maintained:", astar_maintained_total/9, file=file) 
            print("A* Number of Times it Found Optimal Solution:", wins["A*"], file=file)

    

if __name__ == "__main__":
    main()