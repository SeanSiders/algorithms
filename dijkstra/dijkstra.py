import sys
import heapq

'''

Dijkstra's algorithm is a modification of breadth-first search for a
connected graph with positively weighted edges. It will determine the
shortest path to each vertex, from the source vertex provided.

Time Complexity: O(V + E log V)

Every vertex is visted once, giving V iterations. Updating the priority
in the min heap takes log V, which occurs for every edge in E.

'''

def dijkstra(graph, source):

    # Tracks the current minimum path of distances between vertices
    weights = {vertex: sys.maxsize for vertex in graph}
    weights[source] = 0

    # Tracks which vertices have been visited
    visited = set()

    # Initialize heap with the starting vertex
    # The vertex with the smallest edge will pop in priority
    minHeap = [(0, source)]

    while minHeap:
        # Visit the next vertex with the smallest edge
        weight, vertex = heapq.heappop(minHeap)

        # Only visit vertices once
        if vertex not in visited:
            visited.add(vertex)

            # Look at all neighbors that have not been visited
            for neighborVertex, neighborWeight in graph[vertex]:
                if neighborVertex not in visited:

                    # Calculate the minimum weight for the neighbor so far
                    weights[neighborVertex] = min(weights[neighborVertex], weight + neighborWeight)

                    # Queue in the neighbor to be visited
                    heapq.heappush(minHeap, (weights[neighborVertex], neighborVertex))

    return weights 
