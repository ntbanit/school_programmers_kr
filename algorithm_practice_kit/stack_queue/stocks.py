# https://school.programmers.co.kr/learn/courses/30/lessons/42584 
def solution(prices):
    N = len(prices)
    answer = [-1] * N 
    
    stack = [0]
    for i in range(1, N): 
        while stack and prices[i] < prices[stack[-1]] :
            curr_index = stack.pop()
            answer[curr_index] = i - curr_index
            
        stack.append(i)
    
    while stack :
        curr_index = stack.pop()
        answer[curr_index] = N - 1 - curr_index

        
    return answer