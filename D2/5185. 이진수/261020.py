import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    result = ''
    N, hex_text = input().split()

    for h in hex_text:
        integer = int(h, 16)
        binary = bin(integer)[2:]
        result += binary.zfill(4)

    print(f'#{tc} {result}')