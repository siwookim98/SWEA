T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 일단 입력을 보니, 2번과 3번의 test case가 정렬이 안되있어서, 정렬부터
    # 정렬은 bubble_sort 사용
    n = len(arr)

    for i in range(n-1, 0, -1):

        for j in range(i):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

    # return arr
    # 정렬이 되었으니, 이제 최소인 M개의 값과 최대인 M개의 값을 더하는 작업
    sum_min = 0 

    for k in range(0, M-1):
         
         sum_min += arr[k]

    sum_max = 0 
    
    for l in range(N, N-(M-1),-1):
         
         sum_max += arr[l]

    print(sum_max - sum_min)