# https://www.acmicpc.net/problem/1075

import utility.time

@utility.time.spend_time
def solution() -> int:
    """
    N : 운동 N 분
    m : 초기(최소) 맥박
    M : Max 맥박
    T : 운동 맥박 증가량
    R : Rest 맥박 감소량
    :return:
    """
    N, m, M, T, R = map(int, input().split())

    if m + T > M:
        return -1

    now = m
    while N > 0:
        cov = M - now
        max_cov // T


solution()