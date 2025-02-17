 Laboratory 2: AI: DFS and BFS

Laboratory is focus towards exploring the DFS and BFS algorithm. Initially the algorithms has a start node and no goal note. Understand how dose it grow. Next include a goal node and explore how dose it grow and complete.  As pert of class assignment you need to execute the variation with your ‘Roll No’ as start and no goal, then “roll no” as start and Goal=’your rollno’ and do it for both DFS and BFS. Then swap start and goal noads. 
Weeklong assignment will have variations of above graph to explore DFS and BFS  


A
   / \
  B   C
 / \   \
D   E   F

A is the starting node.
F is the goal node.
2. Recursive DFS: Visualization
In recursive DFS, the traversal happens as follows:
Call Stack Visualization:
A → B → D → Backtrack to B → E → Backtrack to A → C → F (goal found).
At each step, the current state (node, path, etc.) is stored on the call stack:
Initial Call: dfs(A)
First Recursive Call: dfs(B) (A's neighbor)
Second Recursive Call: dfs(D) (B's neighbor)
Backtrack to B: After D has no more neighbors
Third Recursive Call: dfs(E) (B's other neighbor)
Backtrack to A: After B's neighbors are fully explored
Fourth Recursive Call: dfs(C) (A's other neighbor)
Fifth Recursive Call: dfs(F) (C's neighbor and goal)

dfs(A) -> dfs(B) -> dfs(D) (D explored, backtrack)
dfs(A) -> dfs(B) -> dfs(E) (E explored, backtrack)
dfs(A) -> dfs(C) -> dfs(F) (Goal found)

  At any point, the stack represents the current path being explored.
  Backtracking is automatic when a branch ends (i.e., when a node has no more neighbors or the goal is found).
3. Iterative DFS: Visualization
In iterative DFS, the traversal happens using an explicit stack, simulating the recursive call stack:
Stack Content Visualization:
Start with Stack: [A]
Pop A, Push its neighbors: Stack = [B, C]
Pop C, Push its neighbor: Stack = [B, F]
Pop F (Goal found): Stack = [B]
At each step, nodes are popped from the stack and explored:
Initial Stack: [A]
After First Pop (A): [B, C]
After Second Pop (C): [B, F]
After Third Pop (F): Goal found.

    A
   / \
  B   C
 / \   \
D   E   F

Iterative DFS Process:
Start with Stack: [A]
Pop A, Push its neighbors B and C:
Stack = [B, C]
Since DFS is LIFO (Last In, First Out), the neighbor pushed last (C) will be explored first.
Pop C, Push its neighbor F:
Stack = [B, F]
Pop F (Goal found):
Stack = [B]
Pop B, Push its neighbors D and E:
Stack = [D, E]
Again, E is pushed last, so it will be explored before D.
Pop E (no neighbors):
Stack = [D]
Pop D (no neighbors):
Stack is now empty, and DFS ends.
Graph Representation
We'll represent a graph using a dictionary in Python, where each key is a node, and its corresponding value is a list of neighboring nodes.


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

Breadth-First Search (BFS)
BFS explores all nodes at the present "depth" level before moving on to nodes at the next depth level. It uses a queue to keep track of the next node to visit.
from collections import deque
def bfs(graph, start):
    visited = []  # List to keep track of visited nodes.
    queue = deque([start])  # Initialize a queue with the start node.

    while queue:
        node = queue.popleft()  # Dequeue a node from the front of the queue.
        if node not in visited:
            visited.append(node)  # Mark the node as visited.
            # Enqueue all unvisited neighbors.
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return visited

# Example usage:
bfs_result = bfs(graph, 'A')
print("BFS:", bfs_result)


OUTPUT
BFS: ['A', 'B', 'C', 'D', 'E', 'F']

Depth-First Search (DFS)
DFS explores as far as possible along each branch before backtracking. It can be implemented using a stack or recursion.
Using a Stack:
def dfs(graph, start):
    visited = []  # List to keep track of visited nodes.
    stack = [start]  # Initialize a stack with the start node.

    while stack:
        node = stack.pop()  # Pop a node from the top of the stack.
        if node not in visited:
            visited.append(node)  # Mark the node as visited.
            # Push all unvisited neighbors onto the stack.
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return visited

# Example usage:
dfs_result = dfs(graph, 'A')
print("DFS:", dfs_result)
OUTPUT
DFS: ['A', 'C', 'F', 'B', 'E', 'D']
Using Recursion
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []
    
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    
    return visited

# Example usage:
dfs_recursive_result = dfs_recursive(graph, 'A')
print("DFS Recursive:", dfs_recursive_result)
Output
DFS Recursive: ['A', 'B', 'D', 'E', 'F', 'C']

With goal node
BFS and DFS can be modified to include a goal node. The modification involves adding a check to see if the current node is the goal node. If it is, the search stops, and the path to the goal is returned.

Modified BFS with Goal Node

from collections import deque

def bfs_with_goal(graph, start, goal):
    visited = []  # List to keep track of visited nodes.
    queue = deque([(start, [start])])  # Queue holds tuples of (current node, path to this node).

    while queue:
        node, path = queue.popleft()  # Dequeue a node along with the path to reach it.
        if node not in visited:
            visited.append(node)  # Mark the node as visited.
            if node == goal:  # Check if the current node is the goal.
                return path  # Return the path to the goal.

            # Enqueue all unvisited neighbors with the updated path.
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # Return None if the goal is not found.

# Example usage:
bfs_goal_result = bfs_with_goal(graph, 'A', 'F')
print("BFS Path to Goal:", bfs_goal_result)
Output
BFS Path to Goal: ['A', 'C', 'F']

Modified DFS with Goal Node (using stack)
def dfs_with_goal(graph, start, goal):
    visited = []  # List to keep track of visited nodes.
    stack = [(start, [start])]  # Stack holds tuples of (current node, path to this node).

    while stack:
        node, path = stack.pop()  # Pop a node along with the path to reach it.
        if node not in visited:
            visited.append(node)  # Mark the node as visited.
            if node == goal:  # Check if the current node is the goal.
                return path  # Return the path to the goal.

            # Push all unvisited neighbors with the updated path.
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None  # Return None if the goal is not found.

# Example usage:
dfs_goal_result = dfs_with_goal(graph, 'A', 'F')
print("DFS Path to Goal:", dfs_goal_result)

OUTPUT
DFS Path to Goal: ['A', 'C', 'F']

Using Recursion
def dfs_recursive_with_goal(graph, node, goal, path=None, visited=None):
    if visited is None:
        visited = []
    if path is None:
        path = [node]

    visited.append(node)
    if node == goal:  # Check if the current node is the goal.
        return path  # Return the path to the goal.

    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dfs_recursive_with_goal(graph, neighbor, goal, path + [neighbor], visited)
            if result:  # If the goal is found in the recursion, return the result.
                return result

    return None  # Return None if the goal is not found.

# Example usage:
dfs_recursive_goal_result = dfs_recursive_with_goal(graph, 'A', 'F')
print("DFS Recursive Path to Goal:", dfs_recursive_goal_result)

Output
DFS Recursive Path to Goal: ['A', 'B', 'E', 'F']
