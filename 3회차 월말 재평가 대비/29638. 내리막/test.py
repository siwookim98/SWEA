import sys

sys.stdin = open('sample_in.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    # 왼쪽에서 오른쪽 이동할 때 숫자가 작아저야합니다
    # A[i] > A[i+1]
    # 차례대로 감소 1출력 한번이라도 어기면 0 출력
    # 숫자 하나일 때, 감소 조건 만족
    result = 1  # 숫자 하나일 때 감소 조건 만족하므로 초기화는 1로함
    for i in range(N - 1):
        if A[i] <= A[i + 1]:
            result = 0
            break

    print(f'#{tc} {result}')
