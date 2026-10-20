import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            sum_flies = 0
            for i in range(r, r+M):
                for j in range(c, c+M):
                    sum_flies += fly[i][j]

            if max_flies < sum_flies:
                max_flies = sum_flies

    print(f'#{tc} {max_flies}')
