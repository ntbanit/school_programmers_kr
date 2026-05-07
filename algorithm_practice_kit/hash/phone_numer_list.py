# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# AI SOLUTION : USING HASH 
def solution(phone_book):
    word_set = set(phone_book)
    for word in phone_book:
        for L in range(1, len(word)) :
            if word[:L] in word_set :
                return False
    
    return True

# AI SOLUTION : SORTING 
def solution2(words):
    words.sort()
    for i in range(len(words) - 1):
        if words[i + 1].startswith(words[i]) :
            return False
    return True 

string = "ABCDEFGH"
print(string[:])
print(string[2:5])
print(string[2:])
print(string[:5])