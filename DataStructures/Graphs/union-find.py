'''
Problem statement: 
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
'''

import random

def generate_union_find_input(n):
    # Ensure that n is greater than 1 for meaningful edges
    if n < 2:
        raise ValueError("n must be at least 2 to create valid edges.")

    # Generate unique edges
    edges = set()
    
    # Randomly create edges until we have enough
    while len(edges) < n - 1:  # We need at least n-1 edges for a connected component
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:  # Ensure no self-loops
            edges.add((min(u, v), max(u, v)))  # Add edges in a sorted manner to avoid duplicates

    edges = list(edges)
    
    # Randomly add some additional edges to make it more complex
    extra_edges_count = random.randint(0, n)  # Generate up to n extra edges
    for _ in range(extra_edges_count):
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            edges.append((min(u, v), max(u, v)))  # Ensure unique edges

    # Generate a random source and destination
    source = random.randint(0, n - 1)
    destination = random.randint(0, n - 1)
    while destination == source:  # Ensure source and destination are different
        destination = random.randint(0, n - 1)

    return n, edges, source, destination

def main():
    # Inputs:
    n, edges, source, destination = generate_union_find_input(600000)
    print("Number of nodes:", n)
    # print("edges:", edges)
    print("Node 1:", source)
    print("Node 2:", destination)

    def find(x):
        # Path Compression: Whenever we find the parent of the given node 'x' we directly assign that parent to 'x'
        # Why do this ? this optimizes the code for large graphs and traversal becomes shorter.
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(u , v):
        parent_u = find(u)
        parent_v = find(v)
        # Union by Rank: As union find's time complexity is highly dependent on tree hight, minimizing it becomes very important for large graphs.
        # We union such that the element with the high rank always stays on top.
        if rank[parent_v] > rank[parent_u]:
            parent[parent_u] = parent_v
        elif rank[parent_u]>rank[parent_v]:
            parent[parent_v] = parent_u
        else:
            rank[parent_u] +=1 
            parent[parent_v] = parent_u


    rank = [0]*n
    parent = [i for i in range(0, n)]
    for edge in edges:
        u, v = edge
        union(u, v)
    if find(source) == find(destination):
        print(f'Input nodes exists in the same graph')
    else:
        print(f"Input node DO NOT exist in same graph")

if __name__ == "__main__":
    main()