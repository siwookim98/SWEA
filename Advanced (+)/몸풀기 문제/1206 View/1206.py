for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    view = 0
    for i in range(2, N-2):
        side_max = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        if arr[i] - side_max > 0:
            view += arr[i] - side_max
    print(f'#{tc} {view}')