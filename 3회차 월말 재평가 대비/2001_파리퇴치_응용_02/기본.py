import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    energy_diff = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            even_sum = 0
            odd_sum = 0
            for i in range(r, r+M):
                for j in range(c, c+M):
                    if arr[i][j] % 2 == 0:
                        even_sum += arr[i][j]
                    if arr[i][j] % 2 == 1:
                        odd_sum += arr[i][j]
            energy_diff = max(energy_diff, abs(even_sum - odd_sum))

    print(f'#{tc} {energy_diff}')