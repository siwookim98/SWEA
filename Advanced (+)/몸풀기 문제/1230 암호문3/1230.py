import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    ciphertexts = list(map(int, input().split()))
    M = int(input())
    commands = list(map(str, input().split()))


