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
    
    # Implementing Breadth First Search:
    start_node = 'A'
    visited = [] # Not used set as it doesn't preserve the order of insertion which list does
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    print(visited)

if __name__ == '__main__':
    main()