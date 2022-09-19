# https://www.acmicpc.net/problem/1009

import utility.time

sol = [
    [0],
    [1],
    [2, 4, 8, 6],
    [3, 9, 7, 1],
    [4, 6],
    [5],
    [6],
    [7, 9, 3, 1],
    [8, 4, 2, 6],
    [9, 1]
]

@utility.time.spend_time
def solution(n1, n2):
    n1 = n1 % 10
    n2 = (n2 - 1) % len(sol[n1])
    return 10 if sol[n1][n2] == 0 else sol[n1][n2]

cnt = int(input())
for _ in range(cnt):
    a, b = map(int, input().split())
    print(solution(a, b))
