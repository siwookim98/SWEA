import sys

sys.stdin = open('input.txt')

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

INF = float('inf')

def cost(cur, nxt):
    # cur 높이의 칸에서 nxt 높이 칸으로 이돌할 때의 연료 소모량
    if nxt > cur:
        return (nxt - cur) * 2
    if nxt == cur:
        return 1
    return 0

for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]


    print(f'#{tc} {result}')
