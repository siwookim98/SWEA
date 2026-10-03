import sys

sys.stdin = open("sample_input.txt")


T = int(input()) 

# count = 0
for tc in range(1, T+1):
    empty_arr = [[0] * 10 for _ in range(10)] 
    N = int(input()) 
    count = 0
    for i in range(N):
        # arr = list(map(int, input().split()))
        # r1 = arr[0] 
        # c1 = arr[1] 
        # r2 = arr[2] 
        # c2 = arr[3] 
        # color = arr[4] 
        r1, c1, r2, c2, color = map(int, input().split())
        # count = 0
        # 문제에서 r1 ~ r2 , c1 ~ c2까지 범위를 색칠 하라고 했기 때문에
        # 행우선순회가 편해서 r을 먼저 범위를 정해서 진행한다.
        # 그런데 range는 종료 값이 -1이기 때문에 +1을 해줘야 한다 (주의사항!!)
        for r in range(r1, r2+1): # 행 고정
            for c in range(c1, c2+1): # 열 고정
                empty_arr[r][c] += color
                if empty_arr[r][c] == 3:
                    count += 1
    print(f'#{tc} {count}')

    # count 변수는 테스트케이스 하나당 보라색 칸 수 이다.
    # 그러니 테스트케이스가 시작될 때마다 초기화한다.  