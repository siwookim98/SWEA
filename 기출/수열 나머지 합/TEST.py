import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    # 나머지를 더한 값을 result에 저장
    result = 0
    # 각 행별로 열을 순회 2차원 배열
    for i in range(N):
        for j in range(N):
            # 서로 다른 순서쌍이라서 다음 반복으로 건너뛰기
            if i == j:
                continue
            # A[i], A[j]로 나눈 나머지를 모두 더한 값
            result += A[i] % A[j]

    print(f'#{tc} {result}')
