import sys
sys.stdin = open('sample_input.txt')

T = int(input())

FROM = 16
TO = 2
GROUP = 1
WIDTH = 4

for tc in range(1, T+1):
    result = ''
    N, hex_text = input().split()

    for i in range(0, int(N), GROUP):
        h = hex_text[i:i+GROUP]

        integer = int(h, FROM)
        binary = format(integer, {2:'b', 8:'o', 10:'d', 16:'X'}[TO])
        result += binary.zfill(WIDTH)

    print(f'#{tc} {result}')