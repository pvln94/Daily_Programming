def isCyclic(V, edges):
    def dfs(v, visited, parent):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, v):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    graph = {i: [] for i in range(V)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * V
    
    for i in range(V):
        if not visited[i]:
            if dfs(i, visited, -1):
                return True
    return False

def take_input():
    V = int(input("V:"))
    E = int(input("E:"))
    print(f"Enter {E} edges in the format 'u v' where u and v are vertex indices (0-based):")
    edges = []
    for _ in range(E):
        u, v = map(int, input().split())
        edges.append([u, v])
    return V, E, edges

if __name__ == "__main__":
    V, E, edges = take_input()
    print(isCyclic(V, edges))
