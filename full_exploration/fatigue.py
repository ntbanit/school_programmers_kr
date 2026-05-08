# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations
def solution(k, dungeons):
    N = len(dungeons)
    arr = [i for i in range(N)]
    max_count = 0
    for perm in permutations(arr, N):
        cur_count = 0
        fatigue = k
        for i in perm :
            require, cost = dungeons[i] 
            if fatigue < require : 
                break
            fatigue -= cost
            cur_count += 1
        max_count = max(cur_count, max_count)
            
    return max_count