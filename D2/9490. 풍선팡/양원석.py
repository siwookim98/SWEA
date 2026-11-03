import sys

sys.stdin = open("input1.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_sum = 0

    for r in range(N):
        for c in range(M):

            center = arr[r][c]

            # 0으로 두는게 더 나을려나? 이 문제는 center로 넣는게 나으려나?
            # total = 0
            total = center

            for d in range(4):
                for distance in range(1, center + 1):

                    row_sum = r + dr[d] * distance
                    row_col = c + dc[d] * distance

                    if 0 <= row_sum < N and 0 <= row_col < M:
                        total += arr[row_sum][row_col]

            max_sum = max(max_sum, total)

    print(f'#{test_case} {max_sum}')