"""
Python dictionary for graph GRAH0, GRAPH1, GRAPH2
"""
GRAPH0 = {
    0: {1, 2},
    1: {},
    2: {}}
GRAPH1 = {
    0: {1, 5, 4},
    1: {2, 6},
    2: {3},
    3: {0},
    4: {1},
    5: {2},
    6: {}}
GRAPH2 = {
    0: {1, 5, 4},
    1: {2, 6},
    2: {3, 7},
    3: {7},
    4: {1},
    5: {2},
    6: {},
    7: {3},
    8: {1, 2},
    9: {0, 3, 4, 5, 6, 7}}
""" 
Function to calculate the degree
Create an empty dictionary
Looping through the nodes
initialize each node with 0 incoming edges
Loop through the nodes again
Look at all the nodes that a source node points to
"""


def compute_in_degrees(graph):
    indegree = {}
    for node in graph:
        indegree[node] = 0
    for node in graph:

        for neighbor in graph[node]:
            indegree[neighbor] += 1
    return indegree


"""
Distribution of degrees
Helps to check if a degree exists if it does get its value else use 0.
Then add one more node to that degree
"""


def in_degree_distribution(graph):
    dist = {}
    indegree = compute_in_degrees(graph)
    for node in indegree:
        degree = indegree[node]
        dist[degree] = dist.get(degree, 0) + 1
    return dist


"""
Helps create a complete graph with all possible nodes
"""


def make_complete_graph(nodes):
    if nodes <= 0:
        return {}
    graph = {}
    for node in range(nodes):
        neighbors = set()
        for neighbor in range(nodes):
            if neighbor != node:
                neighbors.add(neighbor)
            graph[node] = neighbors
    return graph


"""
Check for in degree for each node in the graph
"""
print("In degree for each node")
print("GRAPH 0 - {}".format(compute_in_degrees(GRAPH0)))
print("GRAPH 1 - {}".format(compute_in_degrees(GRAPH1)))
print("GRAPH 2 - {}".format(compute_in_degrees(GRAPH2)))

"""
Check for the degree distribution
"""
print("\nDegree distribution")
print("GRAPH - {}".format(in_degree_distribution(GRAPH0)))
print("GRAPH1 - {}".format(in_degree_distribution(GRAPH1)))
print("GRAPH2 - {}".format(in_degree_distribution(GRAPH2)))
"""
Make a complete graph with all possible edges except for itself
"""
print("\nComplete Graph")
print("GRAPH 0 - {}".format(make_complete_graph(len(GRAPH0))))
print("GRAPH 1 - {}".format(make_complete_graph(len(GRAPH1))))
print("GRAPH 2 - {}".format(make_complete_graph(len(GRAPH2))))

