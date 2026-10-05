import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    result = 1

    for i in range(N-1):
        if A[i] <= A[i+1]:
            result = 0

    print(f'#{tc} {result}')