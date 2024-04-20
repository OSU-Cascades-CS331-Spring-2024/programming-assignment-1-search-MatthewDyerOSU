import argparse
from CityMap import CityMap
from AgentActions import AgentActions
from bfs import breadthFirstSearch
from ucs import uniformCostSearch
from dls import depthLimitedSearch
from astar import aStarSearch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--searchType', type=str, required=False, default='bfs', help='Type of search algorithm to be used')
    parser.add_argument('--initialCity', type=str, required=False, help='The initial city to start the search from')
    parser.add_argument('--goalCity', type=str, required=False, help='The goal city the search will try to navigate to')
    parser.add_argument('--mapFile', type=str, required=True, help='The name of the file the map will be retrieved from')
    args = parser.parse_args()

    city_map = CityMap(args.mapFile)
    agent_actions = AgentActions(city_map)
    start_city = 'nice'
    goal_city = 'paris'

    path, path_cost = breadthFirstSearch(agent_actions, start_city, goal_city)
    if path:
        print("BFS Path found:", " -> ".join(path))
        print("BFS Path Cost", path_cost)
    else:
        print("No path found between", start_city, "and", goal_city)

    path, path_cost = uniformCostSearch(agent_actions, start_city, goal_city)
    if path:
        print("UCS Path found:", " -> ".join(path))
        print("UCS Path Cost", path_cost)
    else:
        print("No path found between", start_city, "and", goal_city)

    path, cost = depthLimitedSearch(agent_actions, start_city, goal_city, 5)
    if path:
        print("DLS Path found:", " -> ".join(path))
        print("DLS Path cost:", cost)
    else:
        print("No path found within depth limit from", start_city, "to", goal_city)

    path, cost = aStarSearch(agent_actions, start_city, goal_city)
    if path:
        print("A* Path found:", " -> ".join(path))
        print("A* Path cost:", cost)
    else:
        print("No path found from", start_city, "to", goal_city)

if __name__ == "__main__":
    main()