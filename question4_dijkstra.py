# define dijkstra function - dijkstra's algorithm
def dijkstra(graph, startNode, destination):
    shortest_distance = {}
    predecessor = {}
    unvisitedNodes = graph
    infinity = 999999
    path = []

    # assigning initial value of all unvisited nodes as infinity
    for node in unvisitedNodes:
        shortest_distance[node] = infinity
    shortest_distance[startNode] = 0        #except for the root node as 0

    # parse through all the nodes from the unvisited nodes
    while unvisitedNodes:
        minNode = None
        for node in unvisitedNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:  # this comparison is to find the shortest path
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unvisitedNodes.pop(minNode) # remove visited node


    currentNode = destination
    while currentNode != startNode:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print("Path not reachable")
            break
    path.insert(0, startNode)
    if shortest_distance[destination] != infinity:
        print("Shortest distance is " + str(shortest_distance[destination]) + " and the path is " + str(path))


# graph of question 4
graph = {
        'A':{'B':3,'C':5},
        'B':{'C':2,'D':6},
        'C':{'B':1,'D':4,'F':6},
        'D':{'F':2},
        'F':{'A':3,'D':7}
    }

# this is the application
startNode = input("Start node: ")
destination = input("Destination node: ")
dijkstra(graph, startNode, destination)
