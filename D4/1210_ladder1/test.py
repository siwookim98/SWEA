import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    dr = [0 ,0, -1]
    dc = [-1, 1, 0]
    answer = 0

    for r in range(100):
        for c in range(100):

            if matrix[r][c] == 2:
                end = matrix[r][c]

                for i in range(3):
                    go_row = r + dr[i]
                    go_col = c + dc[i]

                    if 0 <= go_row < 100 and 0 <= go_col < 100 and matrix[go_row][go_col] == 1:
                        r, c = go_row, go_col
                        break

            if r == 0:
                answer = c

    print(f'#{tc} {answer}')




