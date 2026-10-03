import sys

sys.stdin = open("sample_input.txt")  # 입력을 파일에서 읽어오도록 설정

T = int(input())  # 전체 테스트 케이스 개수

for test_case in range(1, T + 1):
    N = int(input())  # 배열의 원소 개수
    arr = list(map(int, input().split()))  # 정수 N개를 입력받아 리스트로 저장

    print(f'#{test_case} {max(arr) - min(arr)}')