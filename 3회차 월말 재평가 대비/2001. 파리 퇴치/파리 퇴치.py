 import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0

    for r in range(N-M+1):
        for c in range(N-M+1):
            flies = 0
            for i in range(r, r+M):
                for j in range(c, c+M):
                    flies += grid[i][j]
            if max_flies < flies:
                max_flies = flies

    print(f'#{tc} {max_flies}')