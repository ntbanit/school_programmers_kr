# https://school.programmers.co.kr/learn/courses/30/lessons/42747#
def solution(citations):
    citations.sort()
    
    N = len(citations)
    for i in range(N) :
        if citations[i] >= N - i:
            return N - i
    
    return 0