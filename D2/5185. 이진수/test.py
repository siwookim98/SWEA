import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, hex_num = input().split()
    # print(hex_num)
    result = ''
    for num in hex_num:
        int_num = int(num, 16)
        bin_num = bin(int_num)[2:].zfill(4)
        # print(bin_num)
        result += bin_num
    print(f'#{tc} {result}')
