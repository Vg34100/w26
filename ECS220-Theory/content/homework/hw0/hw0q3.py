from collections import deque

graph = {
    'a': ['e'],
    'b': ['e', 'f', 'g', 'h'],
    'c': ['d', 'h'],
    'd': ['c'],
    'e': ['a', 'b', 'h'],
    'f': ['b', 'h'],
    'g': ['b'],
    'h': ['b', 'c', 'e', 'f']
}

def bfs(graph, start):
    visited = []
    queue = deque([start])
    visited_set = {start}

    while queue:
        node = queue.popleft()
        visited.append(node)

        # Get neighbors in alphabetical order
        neighbors = sorted(graph[node])
        for neighbor in neighbors:
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)

    return visited

def dfs(graph, start):
    visited = []
    visited_set = set()

    def dfs_helper(node):
        visited.append(node)
        visited_set.add(node)

        # Visit neighbors in alphabetical order
        neighbors = sorted(graph[node])
        for neighbor in neighbors:
            if neighbor not in visited_set:
                dfs_helper(neighbor)

    dfs_helper(start)
    return visited

bfs_order = bfs(graph, 'a')
dfs_order = dfs(graph, 'a')

print(' '.join(bfs_order))
print(' '.join(dfs_order))
