import sys
from itertools import combinations

sys.stdin = open('sample_input.txt')

def get_taste(group):
    taste = 0
    for i, j in combinations(group, 2):  # 두 개씩 짝 꺼내기
        taste += grid[i][j] + grid[j][i]  # 시너지 더하기
    return taste

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    # 나누기 - 재료 n개를 n/2개씩 a,b 두 그룹으로 나누는 모든 경우 만든다
    # 맛 계산 - 각 그룹 안에서 재료 쌍마다 시너지를 더해 맛을 구한다
    # 비교 - 두 맛의 차이를 구하고 모든 경우 중 최솟값을 남긴다
    result = float('inf')
    # 1단계 - a그룹을 고르면 b그룹은 나머지로 자동 결정
    for a in combinations(range(N), N // 2):
        b = set(range(N)) - set(a)

        # 2단계 - 맛 계산
        result = min(result, abs(get_taste(a) - get_taste(b)))

    print(f'#{tc} {result}')
