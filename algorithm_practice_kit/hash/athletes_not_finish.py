# https://school.programmers.co.kr/learn/courses/30/lessons/42576
from collections import Counter
def solution(participant, completion):
    p_cnt = Counter(participant)
    c_cnt = Counter(completion)
    
    for key in c_cnt :
        p_cnt[key] -= c_cnt[key]
        
    for key in p_cnt :
        if p_cnt[key] > 0:
            return key
    return ""