BFS Average Number of Cities Explored: 14.222222222222221
BFS Average Number of Cities Expanded: 43.666666666666664
BFS Average Number of Cities Maintained: 16.22222222222222
BFS Number of Times it Found Optimal Solution: 2

UCS Average Number of Cities Explored: 20.88888888888889
UCS Average Number of Cities Expanded: 45.888888888888886
UCS Average Number of Cities Maintained: 25.0
UCS Number of Times it Found Optimal Solution: 7

DLS Average Number of Cities Explored: 23.0
DLS Average Number of Cities Expanded: 40.666666666666664
DLS Average Number of Cities Maintained: 23.0
DLS Number of Times it Found Optimal Solution: 0

A* Average Number of Cities Explored: 20.88888888888889
A* Average Number of Cities Expanded: 45.888888888888886
A* Average Number of Cities Maintained: 25.0
A* Number of Times it Found Optimal Solution: 7

The first thing I noticed is that UCS and A* had the same results, which is not surprising since we know that A* is basically UCS but with the added heuristic. As I write this I just now am wondering if I was supposed to use the Euclidean distance as the weight when calculating the path cost, instead of just using it to decide where to travel to next. Either way it is clear that not only does A*/UCS find the optimal solution more often, but they do it with decently low scores for numbers of explored, expanded, and maintained.

BFS is complete, and it will always find the shortest path in terms of number of edges, however BFS is memory and space intensive. DLS uses less memory, however it might not always find a solution. UCS is guaranteed to find the lowest cost path to the goal, but it can also take a lot of memory. A* is both complete and optimal, as it will find the lowest cost within proximity to the goal, instead of just the lowest cost.