from collections import deque

def solve_maze_bfs(m, s, e):
    r, c = len(m), len(m[0])
    q = deque([(s[0], s[1], [s])])
    v = set()
    v.add(s)
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    steps = 0
    
    while q:
        x, y, p = q.popleft()
        steps += 1
        
        if (x, y) == e:
            return p, steps-1
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < r and 0 <= ny < c and 
                (nx, ny) not in v and 
                m[nx][ny] != '#'):
                
                v.add((nx, ny))
                np = p + [(nx, ny)]
                q.append((nx, ny, np))
    
    return None, -1

def find_position(m, t):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == t:
                return (i, j)
    return None

def print_maze_with_path(m, p):
    dm = [row[:] for row in m]
    
    for i, (x, y) in enumerate(p):
        if i != 0 and i != len(p) - 1:
            dm[x][y] = '*'
    
    print("\nMaze with solution path (marked with *):")
    for row in dm:
        print(' '.join(f"{cell:2}" for cell in row))

m = [['F', 'E', '#', '#', 'M', 'N'],
    ['#', 'D', '#', 'K', 'L', '#'],
    ['B', 'C', 'G', 'H', '#', '#'],
    ['A', '#', '#', 'I', 'J', '#']]

print("Maze layout:")
for row in m:
    print(' '.join(f"{cell:2}" for cell in row))

start_char = input("Enter start position (letter): ").upper()
end_char = input("Enter end position (letter): ").upper()

s = find_position(m, start_char)
e = find_position(m, end_char)

if s and e:
    p, steps = solve_maze_bfs(m, s, e)
    
    if p:
        print(f"\nNumber of steps BFS algorithm used to reach {end_char} from {start_char}: {steps}")
    else:
        print(f"No path found from {start_char} to {end_char}!")
else:
    print(f"Could not find {start_char} or {end_char} in the maze!")