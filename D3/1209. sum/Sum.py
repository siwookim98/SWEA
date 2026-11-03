import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())  # 테스트 케이스 번호 (값 자체는 사용하지 않음)

    # 100 * 100 2차원 배열
    matrix = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0

    # 각 행의 합
    for r in range(100):
        row_sum = 0
        for c in range(100):
            row_sum += matrix[r][c]
        max_sum = max(max_sum, row_sum)

    # 각 열의 합
    for c in range(100):
        col_sum = 0
        for r in range(100):
            col_sum += matrix[r][c]
        max_sum = max(max_sum, col_sum)

    # 각 대각선의 합
    diag1 = diag2 = 0
    for i in range(100):
        diag1 += matrix[i][i]        # 좌상 -> 우하
        diag2 += matrix[i][99 - i]   # 우상 -> 좌하
    max_sum = max(max_sum, diag1, diag2)

    print(f'#{tc} {max_sum}')
