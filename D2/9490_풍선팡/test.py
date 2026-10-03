import sys

sys.stdin = open('input1.txt')

T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_sum = 0

    for r in range(N):
        for c in range(M):

            center = matrix[r][c]
            total = center

            for i in range(4):
                for distance in range(1, center+1):

                    dx = r + dr[i] * distance
                    dy = c + dc[i] * distance

                    if 0 <= dx < N and 0 <= dy < M:
                        total += matrix[dx][dy]

            max_sum = max(max_sum, total)

    print(f'#{test_case} {max_sum}')