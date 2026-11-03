import sys
sys.stdin = open('input.txt')

def millionaire_project_stack(N, future):
    result = 0
    cur_max = future[N-1]

    #각 가격에 대해 마지막 날의 가격과 비교한다.
    for i in range(N-2, -1, -1):
        if cur_max < future[i]: # 현재 가격이 더 크면,
            # update cur_max
            cur_max = future[i]
        else: # 과거 금액에 사서 현재에 판다.
            # 이익을 계산한다.
            result += cur_max - future[i]

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    future = list(map(int, input().split(' ')))
    print(f'#{tc} {millionaire_project_stack(N, future)}')





