import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    arr = list(map(int, input().split()))
    result = 1
    for i in range(n-1):
        if 1 <= arr[i] - arr[i+1] <= 3:
            result = 1
        else:
            result = 0
            break

    print(f'#{tc} {result}')

