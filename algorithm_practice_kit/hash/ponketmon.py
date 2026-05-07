# https://school.programmers.co.kr/learn/courses/30/lessons/1845
from collections import Counter
def solution(nums):
    count = Counter(nums)
    N = len(nums)
    answer = min(N // 2, len(count))
    return answer