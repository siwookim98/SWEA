import sys

sys.stdin = open("sample_input.txt")  # 입력을 파일에서 읽어오도록 설정

T = int(input())  # 전체 테스트 케이스 개수

for test_case in range(1, T + 1):
    N = int(input())  # 배열의 원소 개수
    arr = list(map(int, input().split()))  # 정수 N개를 입력받아 리스트로 저장

    # 버블 정렬: 인접한 두 값을 비교해서 큰 값을 뒤로 보내는 과정을
    # N-1번 반복하면 리스트가 오름차순으로 정렬
    for i in range(N-1, 0, -1):  # 정렬이 끝난 뒤쪽 구간은 매번 줄어듬

        for j in range(i):  # 아직 정렬 안 된 구간을 앞에서부터 반복

            if arr[j] > arr[j+1]:  # 앞의 값이 뒤의 값보다 크다면
                arr[j], arr[j+1] = arr[j+1], arr[j]  # 두 값의 자리를 서로 바꿔줌

    # 정렬이 끝나면 arr[0]이 최솟값, arr[-1]이 최댓값이 됨
    print(f'#{test_case} {arr[-1] - arr[0]}')  # (최댓값 - 최솟값)을 출력