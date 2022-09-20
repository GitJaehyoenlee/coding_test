# https://www.acmicpc.net/problem/1075

import utility.time

@utility.time.spend_time
def solution() -> int:
    answer = 0
    for i in range(8):
        chess_lst = input()
        if i % 2 == 0:
            for i in range(8):
                if i % 2 == 0 and chess_lst[i] == 'F':
                    answer += 1
        else:
            for i in range(8):
                if i % 2 == 1 and chess_lst[i] == 'F':
                    answer += 1

    return answer

print(solution())





