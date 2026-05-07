# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# USING HASH 
def solution(phone_book):
    word_set = set(phone_book)
    for word in phone_book:
        for L in range(1, len(word)) :
            if word[:L] in word_set :
                return False
    
    return True

# SORTING 
def solution2(words):
    words.sort()
    for i in range(len(words) - 1):
        if words[i + 1].startswith(words[i]) :
            return False
    return True 