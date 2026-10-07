import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0
    best_y = 0
    best_x = 0

    for r in range(N):
        for c in range(N):

            total = grid[r][c]

            if r > 0:
                total += grid[r-1][c]

            if r < N-1:
                total += grid[r+1][c]

            if c > 0:
                total += grid[r][c-1]

            if c < N-1:
                total += grid[r][c+1]

            if total > max_flies:
                max_flies = total
                best_y = r
                best_x = c

    print(f'#{tc} {max_flies} {best_y} {best_x}')