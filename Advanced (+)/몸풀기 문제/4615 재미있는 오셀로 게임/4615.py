import sys

sys.stdin = open('sample_input.txt')

T = int(input())

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)]
    h = N // 2
    board[h-1]