import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 돈의 최소 개수로 거슬러 주기 위해 각 종류의 돈이 몇 개씩 필요?
    money = [0] * 8
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money[0] = N // won[0]
    for i in range(1, 8):
        money[i] = (N % won[i-1]) // won[i]
    print(f'#{tc}')
    print(*money)