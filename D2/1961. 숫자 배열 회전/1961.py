import sys
sys.stdin = open('input.txt')

def rotate(grid):
    n = len(grid)
    result = [[0] * n for _ in range(n)]  # 결과를 담을 새 N * N 배열
    # 여기서 result의 모든 칸 (i, j)를 채운다
    for i in range(n):
        for j in range(n):
            result[i][j] = grid[n-j-1][i]

    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    rotate90 = rotate(grid)
    rotate180 = rotate(rotate90)
    rotate270 = rotate(rotate180)

    print(f'#{tc}')
    for i in range(N):
        a = ''.join(map(str, rotate90[i]))  # 90도 회전의 i번째 줄 -> 문자열
        b = ''.join(map(str, rotate180[i]))  # 180도 회전의 i번째 줄 -> 문자열
        c = ''.join(map(str, rotate270[i]))  # 270도 회전의 i번째 줄 -> 문자열
        print(a, b, c)  # 사이에 공백 하나씩 넣어 출력


