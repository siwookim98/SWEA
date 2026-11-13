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
        nonlocal best_time

        # 이동을 계속해도 누적 시간은 줄어들지 않는다.
        if elapsed >= best_time:
            return

        if len(visited) == len(locations):
            best_time = elapsed
            return

        for target, (next_row, next_col) in locations.items():
            if target in visited:
                continue
            # 의뢰인에게 전달하려면 같은 번호의 몬스터를 먼저 잡아야 한다.
            if target < 0 and -target not in visited:
                continue

            distance = abs(row - next_row) + abs(col - next_col)
            visited.add(target)
            dfs(next_row, next_col, elapsed + distance)
            visited.remove(target)

    dfs(0, 0, 0)
    return best_time


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {shortest_time(grid)}')
