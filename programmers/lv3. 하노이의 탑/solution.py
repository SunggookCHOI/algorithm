global answer
answer = []

def solution(n):
    global answer
    move(n,1,3)
    return answer

def move(n, poll1, poll2):
    global answer
    if n == 1:
        answer.append([poll1,poll2])
        return ;
    polls = [1,2,3]
    polls.remove(poll1)
    polls.remove(poll2)
    move(n-1,poll1,polls[0])
    move(1,poll1,poll2)
    move(n-1,polls[0],poll2)
