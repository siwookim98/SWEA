import sys
sys.stdin = open('input.txt')

def shortest_time(grid):
    locations = {}
    for row, cells in enumerate(grid):
        for col, target in enumerate(cells):
            if target != 0:
                locations[target] = (row, col)

    visited = set()
    best_time = float('inf')

    def dfs(row, col, elapsed):
        nonlocal best_time:

    if elapsed >= best_time:
        return

    if len(visited) == len(locations):
        best_time = elapsed
        return

    for target, (next_row, next_col) in locations.items():
        if target in visited:
            continue
        if target < 0 and -target not in visited:
            continue


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {shortest_time(grid)}')