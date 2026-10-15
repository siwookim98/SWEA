import sys
sys.stdin = open('sample_input.txt')

# [문제] 조망권: 양옆 2칸씩, 모두 4개 건물보다 높은 층 수의 합 구하기
# [핵심] 확보 세대 = 내 높이 - (양옆 4개 건물 중 최댓값), 양수일 때만 더함

for tc in range(1, 11):  # 테스트케이스 10개
    N = int(input())  # 건물 개수
    arr = list(map(int, input().split()))  # 각 건물의 높이
    view = 0  # 조망권이 확보된 세대 수의 합

    # 맨 왼쪽 2칸, 맨 오른쪽 2칸은 높이가 항상 0이라 검사할 필요 없음
    # -> i는 2부터 N-3까지 (i-2, i+2가 리스트 범위를 벗어나지 않음)
    for i in range(2, N-2):
        # 왼쪽 2칸(i-2, i-1) + 오른쪽 2칸(i+1, i+2) 중 가장 높은 건물
        side_max = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])

        # 내가 가장 높은 이웃보다 높을 때만, 그 차이만큼 조망권 확보
        # (0 이하 = 주변에 나보다 높거나 같은 건물이 있음 -> 건너뜀)
        if arr[i] - side_max > 0:
            view += arr[i] - side_max

    print(f'#{tc} {view}')  # 출력 형식: #번호 답

