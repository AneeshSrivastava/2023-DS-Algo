'''
In a weighted graph, Dijkstra's algorithm is used to find the shortest path between two nodes. 
It is a greedy algorithm that finds the shortest path between a source node and all other nodes in the graph. 
It is used for single source shortest path on a weighted graph. 
It is not used for negative edge weights.
Real-life use cases:
    - It is used in GPS to find the shortest path between source and destination. 
    - It is used in network routing protocols. 
    - It is used in telephone networks to find the shortest path between two telephone numbers. 
    - It is used in social networking websites to find the shortest path between two people.

Time complexity: O(V^2) where V is the number of vertices in the graph but with the help of min-heap, it can be reduced to O(E + V log V) where E is the number of edges in the graph. 
    - The time complexity can be reduced to O(V log V) using Fibonacci heap. 
    - The time complexity can be reduced to O(E + V log V) using adjacency list representation of the graph.

Space complexity: O(V) where V is the number of vertices in the graph. 
    - The space complexity can be O(E + V) using adjacency list representation of the graph. 
    - The space complexity can be O(V log V) using Fibonacci heap. 
    - The space complexity can be O(V) using min-heap.
'''


from heapq import heappush, heappop

def main():
    # Graph represented as adjacency list
    graph = {
    'A': {'B': 1.8, 'C': 1.5, 'D': 1.4},
    'B': {'A': 1.8, 'E': 1.6},
    'C': {'A': 1.5, 'E': 1.8, 'F': 2.1},
    'D': {'A': 1.4, 'F': 2.7, 'G': 2.4},
    'E': {'B': 1.6, 'C': 1.8, 'F': 1.4, 'H': 1.6},
    'F': {'C': 2.1, 'D': 2.7, 'E': 1.4, 'G': 1.3, 'H': 1.2},
    'G': {'D': 2.4, 'F': 1.3, 'H': 1.5},
    'H': {'E': 1.6, 'F': 1.2, 'G': 1.5}
}
    start_node = 'A'
    end_node = 'H'
    shortest_path = dijkstra(graph, start_node, end_node)
    print('Shortest path from node', start_node, 'to node', end_node , 'is:', '->'.join(shortest_path))

def dijkstra(graph, start_node, end_node):
    distances = {node: float('infinity') for node in graph}
    visited = {node: False for node in graph}
    previous = {node: None for node in graph}

    distances[start_node] = 0
    min_heap = [(0, start_node)]

    while min_heap:
        current_distance, current_node = heappop(min_heap)
        visited[current_node] = True
        for neighbor in graph[current_node]:
            if visited[neighbor]:
                continue
            new_distance = current_distance + graph[current_node][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                min_heap.append((new_distance, neighbor))
    path = []
    current_node = end_node
    while current_node is not None:
        path.append(current_node)
        current_node = previous[current_node]
    path.reverse()
    return path


if __name__ == '__main__':
    main()