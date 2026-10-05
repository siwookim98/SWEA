import sys
sys.stdin = open("input.txt")

def count_flies(arr2d,M,row_i,col_i): #M*M영역 내 파리의 개수 구하기
    count = 0
    for r in range(row_i,row_i+M): #r~r+M사이
        for c in range(col_i,col_i+M):# c~c+M사이
            count += arr2d[r][c] #해당영역만 카운트
    return count


T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr2d = [list(map(int,input().split())) for _ in range(N)]
    max_count = 0 #최대 파리 개수 결과
    for r in range(N-M+1):#row 세로 전체범위
        for c in range(N-M+1):#col 가로 전체범위
            fly_count = count_flies(arr2d,M,r,c) # 파리개수구하기
            if max_count < fly_count: #max보다 크면
                max_count = fly_count #최댓값 업데이트
    print(f"#{tc} {max_count}")