from collections import deque
def main():
    """
    In DFS we don't rely on Data structure like queues etc, instead we rely on recursion as it naturally 
    executes DFS traversal. Key to writing the code of the algo is below:
    - traverse the nodes.
    - for current nodes find the neighbors.
    - if neighbor is not already visited.
    - then, call DFS function with that neighbor.
    - with recursion, backtracking will happen automatically.
    """

    # Graph represented as adjacency list
    adj_list_graph = {
        'A': ['B', 'D', 'C'],
        'B': ['E', 'F'],
        'C': ['G', 'H'],
        'D': ['I', 'H'],
        'E': ['B', 'F'],
        'F': ['B', 'E', 'I'],
        'G': [],
        'H': ['C', 'D'],
        'I': ['D', 'F']
    }
    adj_matrix_graph = [
        # A  B  C  D  E  F  G  H  I
        [0, 1, 1, 1, 0, 0, 0, 0, 0],  # A
        [0, 0, 0, 0, 1, 1, 0, 0, 0],  # B
        [0, 0, 0, 0, 0, 0, 1, 1, 0],  # C
        [0, 0, 0, 0, 0, 0, 0, 1, 1],  # D
        [0, 1, 0, 0, 0, 1, 0, 0, 0],  # E
        [0, 1, 0, 0, 1, 0, 0, 0, 1],  # F
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # G
        [0, 0, 1, 1, 0, 0, 0, 0, 0],  # H
        [0, 0, 0, 1, 0, 1, 0, 0, 0]   # I
    ]

    """
    Graphs can be represented in 2 Data structures:
    - List and matrix, therefore knowing DFS traversal in both is important.
    """    
    traversal_order = dfs(adj_list_graph, 'A')
    print('DFS traversal order is with Adjacency list : ', traversal_order)
    matrix_dfs_traversal_order = dfs_with_matrix(adj_matrix_graph, 'A')
    print('DFS traversal order is with Adjacency Matrix : ', matrix_dfs_traversal_order)

def dfs(graph, start_node, visited= None):
    # Implementing Depth First Search:
    if visited is None:
        visited = []
    visited.append(start_node)
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def dfs_with_matrix(adj_matrix_graph, start_node, visited= None):
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    if visited is None:
        visited = []
    visited.append(start_node)
    node_index = nodes.index(start_node)

    for connection_index, connection in enumerate(adj_matrix_graph[node_index], start=0):
        if connection ==1 and (nodes[connection_index] not in visited):
            dfs_with_matrix(adj_matrix_graph, nodes[connection_index], visited)
    return visited
if __name__ == '__main__':
    main()