import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Hex_number = input().split()
    N = int(N)
    Number = int(Hex_number, 16)
    Binery_Number = bin(Number)[2:].zfill(N*4)
    print(f'#{tc} {Binery_Number}')
