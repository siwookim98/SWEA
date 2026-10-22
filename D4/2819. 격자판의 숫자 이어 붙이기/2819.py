import sys

sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    grid = [list(input().split()) for _ in range(4)]
    results = set()

    # 격자판의 모든 위치(i, j)에서 탐색을 시작합니다.
    for i in range(4):
        for j in range(4):
            # DFS를 위한 스택을 생성하고, 시작 상태를 추가합니다.
            stack = [(i, j, grid[i][j])]

            while stack:
                r, c, current_num_str = stack.pop()

                # 숫자가 7자리가 되면 결과에 추가하고 더 이상 탐색하지 않습니다.
                if len(current_num_str) == 7:
                    results.add(current_num_str)
                    continue

                # 4방향으로 다음 상태를 만들어 스택에 추가합니다.
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < 4 and 0 <= nc < 4:
                        stack.append((nr, nc, current_num_str + grid[nr][nc]))

    print(f'#{tc} {len(results)}')
