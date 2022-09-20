# https://www.acmicpc.net/problem/1075
from collections import defaultdict

import utility.time

@utility.time.spend_time
def solution() -> int:
    pro_lst = defaultdict(int)
    for _ in range(int(input())):
        pro_name = input()
        pro_lst[pro_name[0]] += 1

    answer_lst = []
    for k, v in pro_lst.items():
        if v >= 5:
            answer_lst.append(k)

    if len(answer_lst) == 0:
        return "PREDAJA"
    else:
        answer_lst.sort()
        return ("".join(answer_lst))

print(solution())