# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq
def solution(scoville, K):
    heap = []
    for sco in scoville :
        heapq.heappush(heap, sco)
    answer = 0
    while True:
        min_sco = heapq.heappop(heap)
        if min_sco >= K :
            break
        if not heap :
            return -1
        sec_min_sco = heapq.heappop(heap)
        
        new_sco = min_sco + 2 * sec_min_sco
        heapq.heappush(heap, new_sco)
        answer += 1
    
    return answer