import sys

sys.stdin = open('input.txt')

T = int(input())

for x in range(1, T+1):

    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    distance = 0
    sorted_arr = sorted(arr)

    min_point = sorted_arr[0]
    max_point = sorted_arr[-1]

    if N == 1:
        distance = abs(S - min_point)
    elif S < min_point:
        distance = max_point - S
    elif min_point < S < max_point:
        distance = min(S - min_point, max_point - S) + (max_point - min_point)
    elif S > max_point:
        distance = S - min_point

    print(f'#{x} {distance}')



