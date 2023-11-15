def create_graph():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))

    for i in range(vertices):
        neighbors = list(map(int, input(f"Enter neighbors for vertex {i}: ").split()))
        graph[i] = neighbors

    return graph

def dfs(graph, vertex, visited):
    visited[vertex] = True
    print(vertex, end=' ')

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start_vertex):
    visited = [False] * len(graph)
    queue = [start_vertex]  # Use a list as a queue
    visited[start_vertex] = True

    while queue:
        vertex = queue.pop(0)  # Dequeue from the front
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)  # Enqueue to the back
                visited[neighbor] = True

# Create the graph
graph = create_graph()
start_vertex = int(input("Enter the starting vertex: "))

print("DFS:")
dfs(graph, start_vertex, [False] * len(graph))
print("\nBFS:")
bfs(graph, start_vertex)
