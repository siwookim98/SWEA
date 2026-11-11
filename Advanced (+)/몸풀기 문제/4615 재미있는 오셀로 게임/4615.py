import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)]  # 행마다 별개의 리스트를 만든다
    mid = N // 2

    # 가운데 4칸 초기 배치 (0-index 기준)
    board[mid - 1][mid - 1] = 2
    board[mid][mid] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1

    for _ in range(M):
        x, y, color = map(int, input().split())
        # x: 열(가로), y: 행(세로), 둘 다 1부터 시작
        # 판에 접근할 때는 board[y - 1][x - 1]

