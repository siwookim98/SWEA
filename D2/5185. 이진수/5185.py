import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, hex_num = input().split()
    N = int(N)
    int_num = []
    bin_num = []
    for i in range(N):
        # print(hex_num[i])
        int_num.append(int(hex_num[i], 16))
    # print(int_num)
    for j in int_num:
        bin_num.append(bin(j)[2:].zfill(4))
    # print(bin_num)
    result = "".join(bin_num)
    print(f'#{tc} {result}')


