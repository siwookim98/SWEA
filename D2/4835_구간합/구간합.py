import sys

# 'sample_input.txt' 파일을 표준 입력(input())으로 읽도록 설정
sys.stdin = open('sample_input.txt')

# 전체 테스트 케이스 개수
T = int(input())

for test_case in range(1, T+1):
    # N: 배열의 크기, M: 연속으로 몇 개씩 묶어서 합을 구할지
    N, M = map(int, input().split())
    # 배열 원소들 입력받기
    arr = list(map(int, input().split()))

    # 1. 맨 처음 구간(배열의 0번 인덱스부터 M-1번 인덱스까지)의 합을 직접 더해서 구한다.
    window_sum = 0
    for i in range(M):
        window_sum += arr[i]

    # 지금까지 본 구간합 중 최댓값/최솟값을 저장할 변수.
    # 아직 구간을 하나밖에 못 봤으니 일단 첫 구간합으로 초기화한다.
    max_sum = window_sum
    min_sum = window_sum

    # 2. 구간을 한 칸씩 오른쪽으로 밀면서 나머지 구간합들을 구한다.
    #    (슬라이딩 윈도우: 매번 전체를 다시 더하지 않고,
    #     새로 들어오는 원소는 더하고 빠지는 원소는 빼는 방식으로 계산량을 줄인다)
    for i in range(M, N):
        # 새로 구간에 들어오는 원소 arr[i]를 더하고,
        # 구간에서 빠지는 원소 arr[i-M]을 뺀다.
        window_sum += arr[i] - arr[i-M]

        # 지금까지 구한 구간합 중 가장 큰 값이면 max_sum을 갱신
        if window_sum > max_sum:
            max_sum = window_sum

        # 지금까지 구한 구간합 중 가장 작은 값이면 min_sum을 갱신
        if window_sum < min_sum:
            min_sum = window_sum

    # 3. 구간합의 최댓값에서 최솟값을 뺀 값을 출력
    print(f'#{test_case} {max_sum - min_sum}')
