T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    P = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)

    room = 1
    count = 0

    while room != N:
        if room == 1:
            room = 2
        elif not visited[room]:
            visited[room] = True
            room = P[room]
        else:
            room += 1

        count += 1

    print(f'#{tc} {count}')