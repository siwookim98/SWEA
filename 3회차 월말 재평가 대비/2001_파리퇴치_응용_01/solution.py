import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr2d = [list(map(int, input().split())) for _ in range(N)]
    temp_diff = 0
    # 여기에 코드를 작성하세요.
    for r in range(N-M+1):
        for c in range(N-M+1):
            max_temp = -20
            min_temp = 50
            for i in range(r, r+M):
                for j in range(c, c+M):
                    if max_temp < arr2d[i][j]:
                        max_temp = arr2d[i][j]
                    if min_temp > arr2d[i][j]:
                        min_temp = arr2d[i][j]

            temp_diff = max(temp_diff, max_temp - min_temp)

    print(temp_diff)


