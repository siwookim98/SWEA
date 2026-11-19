import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    gain = []
    total = sum(A)

    if total >= 2 * N:
        print(f'#{tc} {cnt}')
        continue

    for i in range(N):
        gain.append(max(A[i] + i + 1, i + 1) - A[i])

    gain = sorted(gain, reverse=True)

    for g in gain:
        total += g
        cnt += 1
        if total >= 2 * N:
            break

    print(f'#{tc} {cnt}')