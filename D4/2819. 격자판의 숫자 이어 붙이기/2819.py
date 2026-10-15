import sys
sys.stdin = open('sample_input.txt')

def moving(grid):
    for r in range(4):
        for c in range(4):


T = int(input())
for tc in range(1, T+1):
    grid = [list(map(int, input().split())) for _ in range(4)]
