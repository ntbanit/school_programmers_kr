# https://school.programmers.co.kr/learn/courses/30/lessons/42839
def seive_prime(max_number):
    prime = [True] * (max_number + 1)
    sqrt = int(max_number ** 0.5) + 2
    for i in range(2, sqrt): 
        if not prime[i] :
            continue
        j = i * i
        while j <= max_number :
            prime[j] = False
            j += i
    prime_set = set([i for i in range(2, max_number + 1) if prime[i]])
    return prime_set

from collections import * 
def solution(numbers):
    counter = defaultdict(int)
    for char in numbers : 
        num = ord(char) - ord('0')
        counter[num] += 1
        
    max_number_arr = []
    for i in range(9, -1, -1):
        if counter[i] == 0:
            continue
        for j in range(counter[i]):
            max_number_arr.append(f"{i}")
    max_number_str = ''.join(max_number_arr)
    
    def valid(number):
        cnt = defaultdict(int)
        while number > 0 :
            mod = number % 10
            cnt[mod] += 1
            if cnt[mod] > counter[mod]:
                return False
            number //= 10 
        
        return True
        
    prime_set = seive_prime(int(max_number_str))
    output = 0
    for num in prime_set :
        if valid(num):
            output += 1
    return output

# AI CODE COPY -> MUCH MORE FASTER
from itertools import permutations

def solution2(numbers):
    # Generate every possible number from any subset of digits
    candidates = set()
    for r in range(1, len(numbers) + 1):
        for perm in permutations(numbers, r):
            candidates.add(int(''.join(perm)))  # int() handles leading zeros naturally

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(is_prime(n) for n in candidates)

"""
from itertools import permutations

for r in range(1, len("17") + 1):
    for perm in permutations("17", r):
        print(r, perm, '->', ''.join(perm), '->', int(''.join(perm)))

r=1  ('1',)     ->  "1"  ->  1
r=1  ('7',)     ->  "7"  ->  7   ✅
r=2  ('1', '7') ->  "17" ->  17  ✅
r=2  ('7', '1') ->  "71" ->  71  ✅
"""