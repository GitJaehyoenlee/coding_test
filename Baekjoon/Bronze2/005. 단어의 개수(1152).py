# https://www.acmicpc.net/problem/1075

import utility.time

@utility.time.spend_time
def solution() -> int:
    word_count = len(input().split())
    return word_count


print(solution())