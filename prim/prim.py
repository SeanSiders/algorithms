from collections import defaultdict
import heapq

''' -----------------------------------------------------------------------------------
Prim's algorithm will determine the minimum spanning tree of a connected graph.
This implementation will create a dictionary, where each vertex is recorded with
it's minimum edge.

Time Complexity: O(E^2 log E)

For a complete graph, time complexity of traversals will result in E^2, with a
log E complexity for using the min heap.
----------------------------------------------------------------------------------  '''


def prim(graph:defaultdict(list), source) -> defaultdict(int):
    visited = set()
    minSpanningTree = defaultdict(int)

    minHeap = [(0, source)]
    while len(visited) < len(graph):
        # Pop the vertex with least weight
        weight, vertex = heapq.heappop(minHeap)

        # Only visit vertices once
        if vertex not in visited:
            visited.add(vertex)

            # Add the next vertex to the MST
            minSpanningTree[vertex] = weight

            # Look at all unvisited neighbors
            for neighborVertex, neighborWeight in graph[vertex]:
                if neighborVertex not in visited:
                    heapq.heappush(minHeap, (neighborWeight, neighborVertex))

    return minSpanningTree
