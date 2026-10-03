import sys

sys.stdin = open("sample_input.txt")  # 입력을 파일에서 읽어오도록 설정

T = int(input())  # 전체 테스트 케이스 개수

for test_case in range(1, T + 1):
    N = int(input())  # 배열의 원소 개수
    arr = list(map(int, input().split()))  # 정수 N개를 입력받아 리스트로 저장

    max_num = arr[0]  # 초기값은 반복문 시작 전에 딱 한 번만 설정
    for i in arr:
        if max_num < i:
            max_num = i

    min_num = arr[0]  # 초기값은 반복문 시작 전에 딱 한 번만 설정
    for j in arr:
        if min_num > j:
            min_num = j

    print(f'#{test_case} {max_num - min_num}')