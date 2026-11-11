import sys
from collections import deque

sys.stdin = open('input.txt')

INF = float('inf')
# 상, 하, 좌, 우
DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]

def move_cost(now_height, next_height):
    """높이 now_height 칸에서 높이 next_height 칸으로 한 칸 이동할 때 드는 연료"""
    if next_height == now_height:
        return 1
    if next_height < now_height:
        return 0
    return (next_height - now_height) * 2

def bfs(height_map, N):
    """(0,0)에서 (N-1,N-1)까지 가는데 드는 최소 연료를 반환"""
    # visited 대신 "지금까지 찾은 최소 연료"를 기록한다
    fuel = [[INF] * N for _ in range(N)]
    fuel[0][0] = 0

    queue = deque([(0,0)])

    while queue:
        r,c = queue.popleft()

        for dr, dc in DIRECTIONS:
            nr,nc = r+dr,c+dc
            if 0 <= nr < N and 0 <= nc < N:
                new_used = fuel[r][c] + move_cost