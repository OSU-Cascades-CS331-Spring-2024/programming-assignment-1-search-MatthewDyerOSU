import argparse
from CityMap import CityMap
from AgentActions import AgentActions
from bfs import breadthFirstSearch
from ucs import uniformCostSearch


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
    path, path_cost = uniformCostSearch(agent_actions, start_city, goal_city)
    if path:
        print("Path found:", " -> ".join(path))
        print("Path Cost", path_cost)
    else:
        print("No path found between", start_city, "and", goal_city)

if __name__ == "__main__":
    main()