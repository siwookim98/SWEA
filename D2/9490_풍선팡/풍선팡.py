import sys

# input1.txt 파일을 표준입력처럼 사용하겠다는 뜻
sys.stdin = open('input1.txt')

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T+1):

    # N: 세로 칸 수(행), M: 가로 칸 수(열)
    N, M = map(int, input().split())
    # grid[i][j] : (i, j) 위치에 있는 풍선의 값(=터졌을 때 뻗어나가는 거리)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 상, 하, 좌, 우 4방향을 표현하기 위한 이동값
    # dr[k], dc[k] 를 함께 쓰면 k번째 방향으로 한 칸 이동
    dr = [-1, 1, 0, 0]   # 위, 아래, (좌우는 0)
    dc = [0, 0, -1, 1]   # (상하는 0), 좌, 우
    max_val = 0  # 지금까지 구한 합계 중 최댓값을 저장할 변수

    # 모든 칸을 한 번씩 "터뜨려 본다"고 가정하고 시뮬레이션
    for i in range(N):
        for j in range(M):
            v = grid[i][j]   # 지금 터뜨리는 풍선의 값 = 뻗어나갈 거리
            total = v         # 자기 자신의 값은 일단 합계에 포함

            # 4방향(위/아래/왼쪽/오른쪽)으로 각각 확인
            for k in range(4):
                # 해당 방향으로 1칸, 2칸, ..., v칸까지 이동하면서
                # 지나가는 칸들의 값을 전부 더한다
                for s in range(1, v + 1):
                    ni = i + dr[k] * s  # 이동한 후의 행(row) 위치
                    nj = j + dc[k] * s  # 이동한 후의 열(column) 위치

                    # 격자 범위를 벗어나면 이 방향은 더 못 가므로 멈춤
                    if ni < 0 or ni >= N or nj < 0 or nj >= M:
                        break

                    # 범위 안이면 그 칸의 값을 합계에 더하고 계속 진행
                    total += grid[ni][nj]

            # 지금까지 계산한 합계 중 가장 큰 값을 갱신
            if total > max_val:
                max_val = total

    # 테스트 케이스 번호와 함께 최댓값 출력
    print(f'#{tc} {max_val}')
