# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict

def solution(clothes):
    types_map = defaultdict(int)
    for clothe, type_name in clothes :
        types_map[type_name] += 1
    
    answer = 1
    for type_name in types_map : 
        answer *= (1 + types_map[type_name])
    return answer - 1