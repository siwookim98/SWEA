"""
산악 구조 로봇 — 다익스트라

각 칸을 정점으로 보고 상하좌우로 이동하는 데 드는 연료를 간선 비용으로 둔다.
내리막은 0, 평지는 1, 오르막은 높이 차의 두 배다.
이동 횟수가 같아도 연료가 다를 수 있으므로 누적 연료가 가장 적은 칸부터 꺼낸다.

dist[r][c]에는 (r, c)까지 지금까지 찾은 최소 연료를 기록한다.
더 적은 연료로 도착했을 때만 dist를 갱신하고 힙에 넣는다.
이동 비용이 모두 0 이상이므로 현재 최솟값으로 목적지를 꺼내는 순간 정답이 확정된다.

테스트 케이스당 시간 O(N² log N), 공간 O(N²).
"""

import sys
from heapq import heappop, heappush


DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def minimum_fuel(grid):
    n = len(grid)
    dist = [[float("inf")] * n for _ in range(n)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]  # (누적 연료, 행, 열)

    while heap:
        fuel, row, col = heappop(heap)
        if fuel != dist[row][col]:
            continue  # 같은 칸에 더 적은 연료로 도착한 기록이 있다.
        if row == n - 1 and col == n - 1:
            return fuel

        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if not (0 <= nr < n and 0 <= nc < n):
                continue

            rise = grid[nr][nc] - grid[row][col]
            if rise < 0:
                step_cost = 0
            elif rise == 0:
                step_cost = 1
            else:
                step_cost = 2 * rise

            next_fuel = fuel + step_cost
            if next_fuel < dist[nr][nc]:
                dist[nr][nc] = next_fuel
                heappush(heap, (next_fuel, nr, nc))


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{tc} {minimum_fuel(grid)}")



