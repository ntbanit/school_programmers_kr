# https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math 
def solution(progresses, speeds):
    answer = []
    stack = 0 # only need the last element of stack 
    cur = 0 
    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i]) / speeds[i])
        if days > stack:
            if stack > 0 :
                answer.append(cur)

            stack = days
            cur = 1
        
        else :
            cur += 1
    
    if stack > 0 :
        answer.append(cur)
    return answer