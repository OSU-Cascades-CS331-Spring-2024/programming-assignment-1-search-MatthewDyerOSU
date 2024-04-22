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

    if args.A is None or args.B is None:
        initial_cities = ["brest", "montpellier", "strasbourg", "paris", "grenoble", "brest", "grenoble", "nice", "caen"]
        goal_cities = ["nice", "calais", "bordeaux", "grenoble", "paris", "grenoble", "brest", "nantes", "strasbourg"]

        for i in range(9):
            path, path_cost, num_explored, num_expanded, num_maintained = breadthFirstSearch(agent_actions, initial_cities[i], goal_cities[i])
            if path:
                print("BFS Path found:", " -> ".join(path))
                print("BFS Path Cost:", path_cost)
                print("BFS Explored:", num_explored)
                print("BFS Expanded", num_expanded)
                print("BFS Maintained:", num_maintained)
            else:
                print("No path found between", initial_cities[i], "and", goal_cities[i])

            path, path_cost, num_explored, num_expanded, num_maintained = uniformCostSearch(agent_actions, initial_cities[i], goal_cities[i])
            if path:
                print("UCS Path found:", " -> ".join(path))
                print("UCS Path Cost", path_cost)
                print("UCS Explored:", num_explored)
                print("UCS Expanded", num_expanded)
                print("UCS Maintained :", num_maintained)
            else:
                print("No path found between", initial_cities[i], "and", goal_cities[i])

            path, cost, num_explored, num_expanded, num_maintained = depthLimitedSearch(agent_actions, initial_cities[i], goal_cities[i], 7)
            if path:
                print("DLS Path found:", " -> ".join(path))
                print("DLS Path cost:", cost)
                print("DLS Explored:", num_explored)
                print("DLS Expanded", num_expanded)
                print("DLS Maintained:", num_maintained)
            else:
                print("No path found within depth limit from", initial_cities[i], "to", goal_cities[i])

            path, cost, num_explored, num_expanded, num_maintained = aStarSearch(agent_actions, initial_cities[i], goal_cities[i])
            if path:
                print("A* Path found:", " -> ".join(path))
                print("A* Path cost:", cost)
                print("A* Explored:", num_explored)
                print("A* Expanded", num_expanded)
                print("A* Maintained:", num_maintained)
            else:
                print("No path found from", initial_cities[i], "to", goal_cities[i])


    

if __name__ == "__main__":
    main()