from Labyrinth1a import Map, Position
import numpy as np


# if map.occupation(pos): -> (bool-ähnlich, geht davon aus das es ein bool ist)
# if pos in visited:

def pathfinding(map: Map, start_pos: Position, end_pos: Position) -> Position:
    visited = {}
    visited[start_pos] = True

    pos = Position(x=0, y=0)
    if end_pos.x < start_pos.x:
        pos.x += 1
    elif end_pos.x > start_pos.x:
        pos.x -= 1
    elif end_pos.y < start_pos.y:
        pos.y += 1
    elif end_pos.y > start_pos.y:
        pos.y -= 1

    #if map.occupation(pos):
    #    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


    else end_pos_y == start_pos_y && end_pos_x == start_pos_x:
        print("Start und Endposition sind gleich, Selbstzerstörung in 10Sekunden!!! Bitte geben Sie eine andere Position an um die Selbstzerstörrung zu verhindern.")
        time.sleep(10)
        while True:
            fail = 0
            print("Exception error: "+fail)
            fail = fail + 1

    return Position(x=0, y=0)
    
def find_path(maze):
    # BFS algorithm to find the shortest path
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (1, 1)
    end = (maze.shape[0]-2, maze.shape[1]-2)
    visited = np.zeros_like(maze, dtype=bool)
    visited[start] = True
    queue = Queue()
    queue.put((start, []))
    while not queue.empty():
        (node, path) = queue.get()
        for dx, dy in directions:
            next_node = (node[0]+dx, node[1]+dy)
            if (next_node == end):
                return path + [next_node]
            if (next_node[0] >= 0 and next_node[1] >= 0 and
                next_node[0] < maze.shape[0] and next_node[1] < maze.shape[1] and
                maze[next_node] == 0 and not visited[next_node]):
                visited[next_node] = True
                queue.put((next_node, path + [next_node]))


# node[0] -> node.x, node[1] -> node.y
# maze[next_node] == 0 -> occupied
# .shape[0] -> map.maxsize.x