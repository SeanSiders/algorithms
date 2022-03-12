from collections import defaultdict
from http.cookiejar import LWPCookieJar
import queue

''' -----------------------------------------------------------------------------------
Topological sort is a breadth or depth first search that is designed for
Directed Acyclic Graphs. The algorithm will explore every vertex that exists on
a path from a given source vertex.

In a breadth first approach, from the source, all neighboring vertices will be
explored via its adjacency list. Only then moving to each neighbor, and
exploring its un-visited neighbors in a recursive manner.

In a depth first approach, from the source, a complete path will be explored
until a leaf or boundary is found. From that point, the nodes in that path in
reverse order will explore all other paths to un-visited nodes until a leaf or
boundary is found. This is commonly achieved with the calling stack frame, with
a recursive function.

Usage :
    Event Scheduling
    Dependency Graphs
    Assembly Instruction Execution

Time Complexity : O(V + E)

The worst-case scenario occurs when an entire graph is traversed. This is
possible when the source vertex has no parents, and it's children contain paths
that cover the entire graph. A good example of this is a tree, or linear linked
list.
----------------------------------------------------------------------------------  '''


# An iterative breadth-first search, returning the path taken
def topologicalSort_BFS(graph:defaultdict(list), source) -> list:
    # The resulting breadth-first path
    path = list()

    # Tracks which vertices have been visited
    visited = set()

    vertexQueue = queue.Queue()
    vertexQueue.put(source)

    while not vertexQueue.empty():
        vertex = vertexQueue.get()

        # Only visit vertices once
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    # Enqueue the neighbor
                    vertexQueue.put(neighbor)

    return path 


# A recursive depth-first search, returning the path taken
def topologicalSort_DFS(graph:defaultdict(list), source) -> list:
    # The resulting depth-first path
    path = list()

    # Tracks which vertices have been visited
    visited = set()

    recursive_DFS(graph, visited, source, path)
    return path


def recursive_DFS(graph:defaultdict(list), visited:set, source, path:list):
    if source in visited: return
    visited.add(source)
    path.append(source)

    # For each neighbor, attempt dfs
    for neighbor in graph[source]:
        recursive_DFS(graph, visited, neighbor, path)
