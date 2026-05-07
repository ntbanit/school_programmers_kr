# https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    stack = []
    for c in s : 
        if c == '(':
            stack.append(c)
        else :
            if not stack :
                return False
            stack.pop()

    return not stack