import sys
from collections import deque

# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]

def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]

def find_shortest_path(start, target_key, data, collected_keys):
    rows = len(data)
    cols = len(data[0])

    visited = set()

    q = deque([(start[0], start[1], 0, [])])

    while q:
        x, y, steps, doors_passed = q.popleft()

        if data[x][y] == target_key:
            return steps, doors_passed, (x, y)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                cell = data[nx][ny]
                if cell == '#':
                    continue

                new_doors = doors_passed.copy()

                if cell in doors_char:
                    if cell.lower() not in collected_keys:
                        continue
                    new_doors.append(cell)

                state = (nx, ny, frozenset(new_doors))

                if state not in visited:
                    visited.add(state)
                    q.append((nx, ny, steps + 1, new_doors))

    return float('inf'), [], None

def recursive_solve(robots, remaining_keys, data, collected_keys, total_steps):
    if not remaining_keys:
        return total_steps

    min_total = float('inf')
    for key in list(remaining_keys):
        for i, robot in enumerate(robots):
            steps, doors_passed, new_pos = find_shortest_path(robot, key, data, collected_keys)
            if steps == float('inf'):
                continue

            new_robots = robots.copy()
            new_robots[i] = new_pos
            new_collected = collected_keys.copy()
            new_collected.add(key)
            new_remaining = remaining_keys.copy()
            new_remaining.remove(key)

            res = recursive_solve(new_robots, new_remaining, data, new_collected, total_steps + steps)
            min_total = min(min_total, res)

    return min_total

def solve(data):
    rows = len(data)
    cols = len(data[0])

    robots = []
    all_keys = set()

    for i in range(rows):
        for j in range(cols):
            c = data[i][j]
            if c == '@':
                robots.append((i, j))
            elif c in keys_char:
                all_keys.add(c)
    result = recursive_solve(robots, all_keys, data, set(), 0)
    return result

def main():
    data = get_input()
    result = solve(data)
    print(result)

if __name__ == '__main__':
    main()
