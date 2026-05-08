# https://school.programmers.co.kr/learn/courses/30/lessons/86491#
def solution(sizes):
    answer = sizes[0]
    if answer[0] < answer[1]:
        answer[0], answer[1] = answer[1], answer[0] 
    
    for w, h in sizes[1:] :
        if h > w :
            w, h = h, w # assume that w >= h 
            
        answer[0] = max(answer[0], w)
        answer[1] = max(answer[1], h)
    
    return answer[0] * answer[1]