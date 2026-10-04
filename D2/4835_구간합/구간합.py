import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_max = 0
    arr_min = float('inf')

    for i in range(N-M+1):
        arr_sum = sum(arr[i:i+M])

        if arr_max < arr_sum:
            arr_max = arr_sum

        if arr_min > arr_sum:
            arr_min = arr_sum

    print(f'#{tc} {arr_max - arr_min}')