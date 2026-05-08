# https://school.programmers.co.kr/learn/courses/30/lessons/42746
from functools import cmp_to_key
def solution(numbers):
    # sort desc 
    def compare_items(a, b):
        if a + b < b + a:
            return 1
        elif a + b > b + a:
            return -1
        return 0
    
    numbers = [str(number) for number in numbers]
    
    numbers.sort(key = cmp_to_key(compare_items))
    # print(numbers)
    
    answer = ''.join(numbers)
    # edge cases if all numbers are 0
    return '0' if answer[0] == '0' else answer