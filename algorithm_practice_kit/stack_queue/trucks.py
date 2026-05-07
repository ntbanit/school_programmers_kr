# O (N * L) # N = len(truck_weights) , L = bridge_length
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # represent trucks on the bridge
    total_weight = 0
    trucks = deque(truck_weights)

    while bridge:
        time += 1
        total_weight -= bridge.popleft()  # truck leaves the bridge

        if trucks:  # still trucks waiting
            if total_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)  # no truck enters, just placeholder
    return time

# O (N) 
from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue = deque([])
    curr_weight = 0
    answer = 0
    
    for truck_weight in truck_weights : 
        answer += 1 # each truck need at least 1 second to pass the bridge 
        
        # remove all trucks alread passed the bridge
        while queue and queue[0][1] <= answer : 
            passed_truck_weight, exit_time = queue.popleft()
            curr_weight -= passed_truck_weight
        
        # wait for the next truck to leave
        while curr_weight + truck_weight > weight or len(queue) + 1 > bridge_length :
            passed_truck_weight, exit_time = queue.popleft()
            curr_weight -= passed_truck_weight
            # and "jump" the current time (answer) to its exit time 
            answer = max(answer, exit_time)

        # add current truck to bridge
        curr_weight += truck_weight
        # the truck will exit exactly `bridge_length` seconds after it enters 
        queue.append((truck_weight, answer + bridge_length))
    
    # final asnwer is the exit time of very last truck in the queue 
    final_answer = queue[-1][1]
    return final_answer
