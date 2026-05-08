# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# COPY SOLUTION AI 
import heapq
def solution(operations):
    visited = {}
    def cleanDeleted(heap): 
        while heap :
            _id = heap[0][1]
            if visited[_id] : # still not deleted
                break
            heapq.heappop(heap)
    
    minHeap = []
    maxHeap = []
    counter = 0
    
    for operation in operations : 
        arr = operation.split(" ")
        op, number = arr[0], int(arr[1])
        if op == 'I':
            heapq.heappush(minHeap, (number, counter))
            heapq.heappush(maxHeap, (-number, counter))
            visited[counter] = True
            counter += 1
        
        else : # lazy deletion
            heap = maxHeap if number == 1 else minHeap
            cleanDeleted(heap)
            if heap :
                value, _id = heapq.heappop(heap)
                visited[_id] = False
            
    cleanDeleted(maxHeap)
    cleanDeleted(minHeap)
    
    minValue = 0 if not minHeap else minHeap[0][0]
    maxValue = 0 if not maxHeap else -maxHeap[0][0]
    return [maxValue, minValue]