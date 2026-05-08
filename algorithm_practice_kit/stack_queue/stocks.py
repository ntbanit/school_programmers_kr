def solution(prices):
    N = len(prices)
    answer = [-1] * N 
    
    stack = [0]
    for i in range(1, N): 
        while prices[i] < prices[stack[-1]] :
            answer[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    
    while stack :
        answer[stack[-1]] = N - 1 - stack[-1]
        stack.pop()
        
    return answer