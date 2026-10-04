import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    cnt = [0] * 10
    max_num = 0
    max_cnt = 0

    for i in arr:
        cnt[i] += 1

    for j in range(1, 10):
        if cnt[max_num] <= cnt[j]:
            max_num = j

    max_cnt = cnt[max_num]

    print(f'#{tc} {max_num} {max_cnt}')





