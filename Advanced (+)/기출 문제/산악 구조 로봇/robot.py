import sys
import heapq

sys.stdin = open('input.txt')

"""
[문제 해석]
- N x N 지도에서 (0,0) -> (N-1,N-1) 까지 상하좌우로 이동하며 '연료 소모량'의 최솟값을 구한다.
- 이동 비용(칸 A -> 칸 B)
    * 높이가 같다  : 1
    * 더 낮은 곳   : 0
    * 더 높은 곳   : (높이 차) * 2     (같은 높이 비용 1은 더하지 않음 -> 예제1에서 4->5 = 2)

[어떤 알고리즘?]
- '가중치가 있는 최단 경로' 문제 -> 다익스트라(Dijkstra)
- 가중치가 0 이상(음수 없음)이라 다익스트라 사용 가능. (BFS는 가중치가 모두 같을 때만 가능)
- 핵심 아이디어: "지금까지 드는 연료가 가장 적은 칸부터 꺼내서 확장" -> 우선순위 큐(heapq)

[흐름]
1. dist[y][x] = 시작점에서 (y,x)까지 현재까지 알려진 최소 연료 (처음엔 무한대)
2. 힙에 (연료, y, x) 를 넣고, 가장 연료가 작은 것부터 꺼낸다.
3. 꺼낸 값이 dist보다 크면 이미 더 좋은 경로가 있다는 뜻 -> 무시(스킵)
4. 4방향 이웃의 비용을 계산해 dist를 갱신할 수 있으면 갱신하고 힙에 넣는다.
5. 끝나면 dist[N-1][N-1] 이 정답.

[시간복잡도] O(N^2 log N^2)  -> N<=30 이라 매우 여유
"""

# 상, 하, 좌, 우 (대각선 이동 불가)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

INF = float('inf')


def cost(cur, nxt):
    """cur 높이 칸에서 nxt 높이 칸으로 이동할 때의 연료 소모량"""
    if nxt > cur:           # 더 높은 곳: 높이 차의 2배
        return (nxt - cur) * 2
    if nxt == cur:          # 같은 높이: 1
        return 1
    return 0                # 더 낮은 곳: 0


def dijkstra(n, board):
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = 0                      # 출발점 비용은 0
    pq = [(0, 0, 0)]                    # (누적 연료, y, x) - 튜플의 첫 값 기준으로 정렬됨

    while pq:
        d, y, x = heapq.heappop(pq)     # 현재 가장 연료가 적게 든 칸

        if d > dist[y][x]:              # 이미 더 좋은 값으로 갱신된 낡은 정보 -> 스킵
            continue
        if y == n - 1 and x == n - 1:   # 도착점이 처음 꺼내지는 순간 = 최솟값 확정 (조기 종료)
            return d

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if not (0 <= ny < n and 0 <= nx < n):   # 지도 밖이면 무시
                continue

            nd = d + cost(board[y][x], board[ny][nx])
            if nd < dist[ny][nx]:       # 더 적은 연료로 도달 가능하면 갱신
                dist[ny][nx] = nd
                heapq.heappush(pq, (nd, ny, nx))

    return dist[n - 1][n - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {dijkstra(N, board)}')
