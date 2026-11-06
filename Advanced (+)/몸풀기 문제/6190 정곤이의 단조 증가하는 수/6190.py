import sys
sys.stdin = open('s_input.txt')

def is_increase_num(n):
    # 각 자리숫자의 대소비교를 어떻게하면 좋을까?
    n = str(n)
    for i in range(1, len(n)):
        if n[i-1] > n[i]:
            return False

    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    max_num = -1
    for i in range(N):
        for j in range(i+1, N):
            product = A[i] * A[j]
            if is_increase_num(product):
                max_num = max(max_num, product)

    print(f'#{tc} {max_num}')
