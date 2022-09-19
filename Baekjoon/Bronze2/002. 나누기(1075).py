# https://www.acmicpc.net/problem/1075

import utility.time

@utility.time.spend_time
def solution(N: int, F: int) -> int:
    mok = N // F
    nam = N % F
    if nam == 0:
        return 0
    else:
        return F * (mok + 1) - N

N = int(input()[:-2]+"00")
F = int(input())
print(format(solution(N, F), '02'))
