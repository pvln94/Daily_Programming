from collections import deque, defaultdict

def shortest_path(V, edges, start, end):
    if start == end:
        return 0
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        node, distance = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                if neighbor == end:
                    return distance + 1
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1


V = int(input("V = "))
edges = eval(input("Edges = "))  # Input edges as a list of lists
start = int(input("start = "))
end = int(input("end = "))

result = shortest_path(V, edges, start, end)
print("Output:", result)
