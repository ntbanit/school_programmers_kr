# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# O(N^2)
from collections import deque
def solution(priorities, location):
    # tuple of (priority, process_id)
    prio_queue = deque([(priorities[i], i) for i in range(len(priorities))])
    # print(prio_queue)
    # print(max(prio_queue))
    count = 0
    while prio_queue : 
        cur_max = max(prio_queue)
        process = prio_queue.popleft()
        if cur_max[0] != process[0] :
            prio_queue.append(process)
        else :
            count += 1
            if process[1] == location :
                return count 
        
    return count

# COPY AI CODE - O(NlogN)
from collections import deque
def solution2(priorities, location):
    # 1. Create a queue of (priority, original_index)
    # O(N)
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    
    # 2. Sort the priorities in descending order.
    # This acts as our "target" list for what priority should be executed next.
    # O(N log N)
    sorted_priorities = sorted(priorities, reverse=True)
    
    count = 0
    prio_idx = 0  # Points to the next priority we are looking to execute
    
    # 3. Process the queue
    # Each element is moved to the back at most a few times, 
    # and popped exactly once. O(N)
    while queue:
        current_prio, original_idx = queue.popleft()
        
        # Check if the current item matches the highest priority available
        if current_prio == sorted_priorities[prio_idx]:
            # It matches! Execute it.
            count += 1
            prio_idx += 1  # Now we look for the next highest priority
            
            # If this is our target process, we are done
            if original_idx == location:
                return count
        else:
            # Not the highest priority yet, put it at the back
            queue.append((current_prio, original_idx))
            
    return count