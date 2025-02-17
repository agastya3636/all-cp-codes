AI Lab 3: Best First Search, Dijkstra’s , A* Algorithm

Explore the above three algorithms for the given start and goal node; Swap Start node and goal node and run see the changes. For Dijkstra how can you determine the shortest distance for all the nodes. What will happen to code if you apply the code for a non existing Goal.  Also Apply the code over your chosen name A, to G where (Goal has to be your name), Also Make out the solution by randomly modifying the Heuristic cost? What will be the impact?
APython implementation of the Best-First Search (BFS) algorithm, followed by an example to demonstrate its use.
Python Code for Best-First Search
import heapq

# Define the graph using an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 6)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

# Heuristic function (h(n)) for each node
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 4,
    'F': 1,
    'G': 0  # G is the goal
}

def best_first_search(graph, start, goal):
    # Priority queue (min-heap) for frontier
    frontier = []
    heapq.heappush(frontier, (heuristic[start], start))
    
    # Visited set to keep track of explored nodes
    visited = set()
    
    while frontier:
        # Get the node with the lowest heuristic value
        _, current_node = heapq.heappop(frontier)
        
        # If the goal is reached, return success
        if current_node == goal:
            print(f"Goal {goal} reached!")
            return True
        
        visited.add(current_node)
        print(f"Exploring: {current_node}")
        
        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor))
    
    print("Goal not found")
    return False

# Example usage
start_node = 'A'
goal_node = 'G'
best_first_search(graph, start_node, goal_node)
----------------------------------------- ------------------------
Output
Exploring: A
Exploring: C
Exploring: F
Exploring: B
Exploring: E
Goal G reached!
_---------    ------------------
    A
   / \
  B - C
   \ /
    D
Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
Directed Graph
    A
   / \
  B   C
   \
    D
Adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

Weighted Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 5)],
    'D': []
}
  'A' is connected to 'B' with a weight of 1 and to 'C' with a weight of 4.
  'B' is connected to 'D' with a weight of 2.
  'C' is connected to 'D' with a weight of 5.



Dijkstra's Algorithm
Dijkstra's Algorithm finds the shortest path from a start node to all other nodes in a graph with non-negative weights.
import heapq

def dijkstra(graph, start):
    # Priority queue (min-heap) for the frontier
    frontier = []
    heapq.heappush(frontier, (0, start))
    
    # Dictionary to store the shortest path cost to each node
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    
    # Dictionary to store the path to reconstruct the shortest path
    came_from = {node: None for node in graph}
    
    while frontier:
        current_cost, current_node = heapq.heappop(frontier)
        
        if current_cost > shortest_paths[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            cost = current_cost + weight
            if cost < shortest_paths[neighbor]:
                shortest_paths[neighbor] = cost
                came_from[neighbor] = current_node
                heapq.heappush(frontier, (cost, neighbor))
    
    return shortest_paths, came_from

def reconstruct_path(came_from, start, goal):
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = came_from.get(current_node, None)
    path.reverse()
    return path

# Example graph and usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 6)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

start_node = 'A'
shortest_paths, came_from = dijkstra(graph, start_node)
goal_node = 'G'
path = reconstruct_path(came_from, start_node, goal_node)

print(f"Shortest path from {start_node} to {goal_node}: {path}")
print(f"Shortest path cost: {shortest_paths[goal_node]}")

--------------   ---------------
Output 
Shortest path from A to G: ['A', 'B', 'E', 'G']
Shortest path cost: 7

A* Algorithm
The A* Algorithm combines the cost to reach the node (path cost) and a heuristic estimate to find the shortest path from a start node to a goal node. It uses both the actual path cost and the heuristic function.
import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue (min-heap) for the frontier
    frontier = []
    heapq.heappush(frontier, (heuristic[start], start))
    
    # Dictionary to store the cost of the shortest path to each node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    # Dictionary to store the total cost of the path (g + h) to each node
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]
    
    # Dictionary to store the path to reconstruct the shortest path
    came_from = {node: None for node in graph}
    
    while frontier:
        _, current_node = heapq.heappop(frontier)
        
        if current_node == goal:
            break
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            tentative_g_score = g_score[current_node] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                heapq.heappush(frontier, (f_score[neighbor], neighbor))
    
    return g_score, came_from

def reconstruct_path(came_from, start, goal):
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = came_from.get(current_node, None)
    path.reverse()
    return path

# Example graph and heuristic
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 6)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 4,
    'F': 1,
    'G': 0
}

start_node = 'A'
goal_node = 'G'
g_score, came_from = a_star(graph, start_node, goal_node, heuristic)
path = reconstruct_path(came_from, start_node, goal_node)

print(f"A* path from {start_node} to {goal_node}: {path}")
print(f"A* path cost: {g_score[goal_node]}")

-------------------------   -----------------------------
Output 
Shortest path from A to G: ['A', 'B', 'E', 'G']
Shortest path cost: 7
