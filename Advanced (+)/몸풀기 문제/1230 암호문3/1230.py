import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    ciphertexts = list(map(int, input().split()))
    M = int(input())
    commands = list(map(str, input().split()))

    idx = 0
    while idx < len(commands):

        if commands[idx] == 'I':
            x = int(commands[idx+1])
            y = int(commands[idx+2])
            s = list(map(int, commands[idx+3:idx+3+y]))
            ciphertexts[x:x] = s
            idx += 3 + y

        elif commands[idx] == 'D':
            x = int(commands[idx + 1])
            y = int(commands[idx + 2])
            del ciphertexts[x:x+y]
            idx += 3

        elif commands[idx] == 'A':
            y = int(commands[idx + 1])
            s = list(map(int, commands[idx+2:idx+2+y]))
            ciphertexts += s
            idx += 2 + y

    print(f'#{tc}', *ciphertexts[:10])


