import sys

sys.stdin = open('input.txt')

def make_answers(N,M,K):
    """총점이 가장 작아지도록 ox 순서를 만들어 반환"""
    wrong = N-M
    # X 하나 뒤에는 O를 k-1개까지 붙여도 2배가 일어나지 않는다
    safe = wrong * (K-1)
    # X 뒤에 다 숨기지 못한 O는 맨 앞에 몰아 둔다. (총점이 작을 때 2배)
    front = max(M-safe, 0)

    answers = ['O'] * front
    left = M - front
    for _ in range(wrong):
        answers.append('X')
        # 남은 O를 K-1개까지만 붙인다
        add = min(K-1, left)
        answers.extend(['O'] * add)
        left -= add

    return answers

def simulate(answers, K):
    """문제의 규칙대로 점수를 계산"""
    total = 0
    counter = 0
    for answer in answers:
        if answer == 'X':
            # 틀리면 카운터만 0으로
            counter = 0
            continue
        # 맞히면 1점 획득 후 카운터 1 증가
        total += 1
        counter += 1
        # 카운터가 K에 도달하면 카운터 초기화 + 총점 2배
        if counter == K:
            counter = 0
            total *= 2
    return total

T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int, input().split())

    answers = make_answers(N,M,K)
    print(f'{tc} {simulate(answers, K)}')
