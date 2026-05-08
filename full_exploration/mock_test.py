# https://school.programmers.co.kr/learn/courses/30/parts/12230
def solution(answers):
    N = len(answers)
    first = second = third = 0
    fg = [1, 2, 3, 4, 5]
    sg = [2, 1, 2, 3, 2, 4, 2, 5]
    tg = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ifg = isg = itg = 0
    for i in range(N):
        if fg[ifg] == answers[i]:
            first += 1
        if sg[isg] == answers[i]:
            second += 1
        if tg[itg] == answers[i]:
            third += 1
        ifg = (ifg + 1) % len(fg)
        isg = (isg + 1) % len(sg)
        itg = (itg + 1) % len(tg)
    answer = [first, second, third]
    mm = max(answer)
    output = []
    for i in range(3) :
        if answer[i] == mm :
            output.append(i + 1)
    return output