def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if(vertex not in visited):
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
            print 'visiting node:',vertex
    return visited


graph = {'A': set(['B', 'C']),
'B': set(['A', 'D', 'E']),
'C': set(['A', 'F']),
'D': set(['B']),
'E': set(['B', 'F']),
'F': set(['C', 'E'])}

depth = bfs(graph, 'A')
print 'the set is:',depth
