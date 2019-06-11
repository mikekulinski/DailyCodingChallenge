# Finds a path through maze from start to end point
# True represents a wall

"""
Performs BFS to find the shortest path through the maze
"""
def min_steps(maze, start, end):
    queue = [start]
    seen = set()
    length = 0
    while queue:
        next_level = []
        for current in queue:
            if current == end:
                return length

            for n in neighbors(maze, current):
                if n not in seen:
                    next_level.append(n)
                    seen.add(n)

        queue = next_level
        length += 1

    return None


def neighbors(maze, position):
    row, col = position

    neighbor_list = []
    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_coord = (row + x, col + y)
            if is_valid(maze, new_coord):
                neighbor_list.append(new_coord)

    return neighbor_list

def is_valid(maze, position):
    row, col = position
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) \
                                and not maze[row][col]


if __name__ == "__main__":
    maze = [[False, False, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]]

    print(min_steps(maze, (3, 0), (0, 0))) 