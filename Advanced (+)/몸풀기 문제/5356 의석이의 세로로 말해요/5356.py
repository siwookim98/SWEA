import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    grid = [list(input().strip()) for _ in range(5)]
    read_vertically = []
    for c in range(15):
        for r in range(5):
            if c < len(grid[r]):
                read_vertically.append(grid[r][c])

    print(f'#{tc} {"".join(read_vertically)}')
