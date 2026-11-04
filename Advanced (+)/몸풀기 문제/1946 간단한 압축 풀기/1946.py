import sys
sys.stdin = open('input.txt')

# 목표 : 압축된 문서를 원복 문서 너비가 10인 문자열로 만드는 프로그
# 상태 : 원본 문서 10인 문자열 리스
# 자료구조
# 핵심로직
# 종료조건
# 시간복잡도

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    origin_file = []

    for _ in range(N):
        C, K = input().split()
        K = int(K)

        for i in range(K):
            origin_file.append(C)

    print(f'#{tc}')
    for start in range(0,len(origin_file),10):
        print(*origin_file[start:start + 10], sep='')






