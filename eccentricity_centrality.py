```python
from collections import deque

def Calculate_eccentricity(nodes, edges, node=None):

    # 1. Create an empty adjacency list for every node
    # Each node will store a set of its neighboring nodes
    adjacency_list = {node: set() for node in nodes}

    # 2. Build the adjacency list using the given edges
    # Since the graph is undirected, add both u -> v and v -> u
    for u, v in edges:
        adjacency_list[u].add(v)
        adjacency_list[v].add(u)

    # Dictionaries to store the eccentricity and eccentricity centrality
    # of each node
    eccentricity = {}
    eccentricity_centrality = {}

    # 3. Perform BFS starting from every node
    # This allows us to calculate the shortest distances from each node
    for source_node in nodes:

        # Initialize the distance of every node to infinity
        # Infinity indicates that a node has not yet been reached
        distances = {node: float("inf") for node in nodes}

        # The distance from the source node to itself is always zero
        distances[source_node] = 0

        # Mark the source node as visited and add it to the BFS queue
        visited = set([source_node])
        queue = deque([source_node])

        # 4. Explore the graph using Breadth-First Search (BFS)
        while queue:
            # Remove the first node from the queue
            current_node = queue.popleft()

            # Explore all neighbors of the current node
            for neighbor in adjacency_list[current_node]:

                # Process only nodes that have not been visited
                if neighbor not in visited:

                    # Calculate the shortest distance to this neighbor
                    # BFS guarantees shortest paths in an unweighted graph
                    distances[neighbor] = distances[current_node] + 1

                    # Mark the neighbor as visited to avoid revisiting it
                    visited.add(neighbor)

                    # Add the neighbor to the queue for further exploration
                    queue.append(neighbor)

        # 5. Calculate the eccentricity of the source node
        # Eccentricity is the maximum shortest-path distance from
        # the source node to any other node
        max_distance = max(distances.values())
        eccentricity[source_node] = max_distance

        # 6. Calculate eccentricity centrality
        # It is the reciprocal of eccentricity: 1 / eccentricity
        # Round the result to four decimal places
        eccentricity_centrality[source_node] = round(
            1.0 / max_distance, 4
        )

    # 7. Return results for a specific node if one is provided
    if node is not None:
        return eccentricity_centrality[node], eccentricity[node]

    # Otherwise, return the results for all nodes
    return eccentricity_centrality, eccentricity
```
