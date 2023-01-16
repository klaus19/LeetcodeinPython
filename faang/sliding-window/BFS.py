def BFS(graph, start):
  visited = []
  queue = [start]

  while queue:
    vertex = queue.pop(0)
    if vertex not in visited:
      visited.append(vertex)
      queue.extend(graph[vertex] - set(visited))
  return visited