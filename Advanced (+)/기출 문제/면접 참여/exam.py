import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    # M개의 문제를 맞추었을때, 최소 총점 구하기
    # K값에 도달하면 2배되니까 그 전에 틀리는게 최소값 구하기 알맞음
    # 틀린 문제를 W라고 할 때, 이 틀린 문제들은 카운터를 0으로 초기화 시켜서 2배 막아줌
    # 정답 연속 구간을 앞에 배치하고 나머지는 사이에 틀린 문제를 배치함으로써 2배 막음

    W = N - M  # 틀린 문제
    safe = W * (K - 1)  # 뒤에서 2배 없이 맞힐 수 있는 문제
    front = M - safe  # 앞에서 맞힐 문제

    if front <= 0:  # safe가 M보다 크거나 같을때 카운터 상관없이 맞힌 문제가 최솟값
        print(f'#{tc} {M}')
        continue

    # 시뮬레이션
    score = 0
    counter = 0
    for _ in range(front):
        score += 1
        counter += 1
        if counter == K:
            counter = 0
            score *= 2

    score += safe

    print(f'#{tc} {score}')
