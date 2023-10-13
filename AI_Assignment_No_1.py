from collections import deque

def is_valid_move(maze, x, y):
    # Check if the move is within the maze boundaries and the cell is open.
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]
    
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    
    # Define possible moves: up, down, left, and right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[x][y]
            path.append(start)
            return path[::-1]
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(maze, new_x, new_y) and not visited[new_x][new_y]:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                parent[new_x][new_y] = (x, y)
    
    return None

def print_maze(maze, path):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == start:
                print("S", end=" ")  # Start
            elif (i, j) == end:
                print("E", end=" ")  # End
            elif (i, j) in path:
                print("X", end=" ")  # Path
            elif cell == 1:
                print("#", end=" ")  # Blocked
            else:
                print(".", end=" ")  # Open
        print()

# Example usage
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0]
]

start = (0, 0) #assigns the start position
end = (1, 4)   #assigns the end position

path = bfs(maze, start, end)
if path:
    print("Path found:")
    print_maze(maze, path)
else:
    print("No path found")