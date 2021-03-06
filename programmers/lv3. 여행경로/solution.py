import collections


def cmp(answer, arr):
    for i in range(len(answer)):
        if arr[i]<answer[i]:
            return True
        elif arr[i]>answer[i]:
            return False
        else:
            pass
def dfs(q,path,tickets):
    global answer
    if len(q)==0:
        return ;
    nxt = q.popleft()
    path.append(nxt)
    if len(tickets)==0:
        if cmp(answer, path):
            answer = path
        return ;
    for t in tickets:
        if t[0] == nxt:
            temp_tickets = tickets.copy()
            temp_tickets.remove(t)
            q.appendleft(t[1])
            dfs(q,path.copy(),temp_tickets)
def solution(tickets):
    global answer
    answer = ['ZZZ']
    for t in tickets:
        if t[0] == 'ICN':
            temp_tickets = tickets.copy()
            temp_tickets.remove(t)
            q=collections.deque()
            q.appendleft(t[1])
            dfs(q,['ICN'],temp_tickets)
    return answer
