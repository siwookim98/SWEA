import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    min_num = a[0]
    max_num = a[0]
    for num in a:
        if min_num > num:
            min_num = num
        if max_num < num:
            max_num = num
    print(f'#{tc} {max_num - min_num}')
