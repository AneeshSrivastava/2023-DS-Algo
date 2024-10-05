from collections import deque
def main():
    # Graph represented as adjacency list
    graph = {
        'A': ['B', 'D', 'C'],
        'B': ['F', 'E'],
        'C': ['G', 'H'],
        'D': ['I', 'H'],
        'E': ['B', 'F'],
        'F': ['B', 'E', 'I'],
        'G': [],
        'H': ['C', 'D'],
        'I': ['D', 'F']
    }
    traversal_order = dfs(graph, 'A')
    print('DFS traversal order is: ', traversal_order)

def dfs(graph, node, visited= None):
    # Implementing Depth First Search:
    if visited is None:
        visited = []
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                # For every neighbor we again go for DFS
                dfs(graph, neighbor, visited)
    return visited

if __name__ == '__main__':
    main()