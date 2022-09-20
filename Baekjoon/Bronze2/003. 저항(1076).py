# https://www.acmicpc.net/problem/1075

import utility.time

color_val = {
    "black" : 0,
    "brown" : 1,
    "red"   : 2,
    "orange" : 3,
    "yellow" : 4,
    "green" : 5,
    "blue" : 6,
    "violet": 7,
    "grey" : 8,
    "white" : 9
}

@utility.time.spend_time
def solution(color1: str, color2: str, color3: str) -> int:
    answer = 0
    answer += color_val[color1] * 10
    answer += color_val[color2]
    # color3 - 자리수
    answer = answer * pow(10, color_val[color3])
    return answer

color1 = input()
color2 = input()
color3 = input()

print(solution(color1, color2, color3))
