import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):

    n = int(input())
    arr = list(map(int, input().split()))
    result = 1
    cnt = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            result = 1
        else:
            cnt += 1

            if cnt >= 2:
                result = 0
                break

    print(f'#{tc} {result}')
