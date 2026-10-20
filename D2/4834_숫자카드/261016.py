import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().strip()))

    cnts = [0] * 10

    for card in cards:
        cnts[card] += 1

    max_cnt = cnts[0]
    max_card = 0
    for i in range(10):
        if max_cnt <= cnts[i]:
            max_cnt = cnts[i]
            max_card = i

    print(f'#{tc} {max_card} {max_cnt}')


