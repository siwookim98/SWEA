import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    # 아이디어
    # 최종 점수 = 각 1점이 그 이후에 발생한 2배 횟수만큼 곱해진 값의 합
    # 2배가 일어나는 횟수를 줄이고, 일어나더라도 최대한 앞쪽에서 일어나게 해야 최소가 된다.
    #
    # 틀린 문제W개는 카운터를 0으로 초기화시켜 2배를 막아주는 방어막 역할을 한다.
    # 방어막 1개당 K-1개의 연속 정답을 2배 없이 안전하게 만들 수 있다.
    #
    # 따라서 배치는 다음과 같다.
    #   앞쪽: 정답 연속 구간 (2배 발생) + 뒷쪽: X (K-1개 정답) 를 W번 반복 (2배 없음)
    W = N - M                 # 틀린 문제 수
    safe = W * (K - 1)        # 뒷쪽에서 2배 없이 안전하게 맞힐 수 있는 정답 수
    front = M - safe          # 앞쪽에서 연속으로 맞혀야 하는 정답 수

    if front <= 0:
        # 방어막이 충분해서 한 번도 2배가 일어나지 않는 경우 -> 정답 개수 그대로가 점수
        print(f'#{tc} {M}')
        continue

    # 앞쪽 연속 정답 구간을 문제 규칙대로 시뮬레이션
    score = 0
    counter = 0
    for _ in range(front):
        score += 1            # 3. 정답이면 1점 획득
        counter += 1          #    카운터 1 증가
        if counter == K:      # 4. 카운터가 K에 도달하면
            counter = 0       #    카운터 초기화
            score *= 2        #    현재 총점 2배

    # 앞쪽 구간 끝에서 틀린 문제(X)가 나와 카운터가 리셋되므로,
    # 뒷쪽 구간의 정답들은 2배 없이 점수만 더해진다.
    score += safe

    print(f'#{tc} {score}')
