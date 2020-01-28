def compare(a,b) :
    diff=0
    idx = 0
    for i in range(len(a)):
        if a[i]!=b[i] :
            diff +=1
            idx = i
        if diff > 1 :
            return False
    if diff == 1 : 
        return True
    return False

def solution(begin, target, words):
    neighbor = [begin]
    visit = [False for i in range(len(words))]
    v_num = 0
    answer = 0

    while len(neighbor) != 0 :
        nxt = []
        answer += 1
        for n in neighbor:
            for i in range(len(words)):
                if visit[i] == False and compare(n,words[i]):
                    nxt.append(words[i])
                    visit[i] = True
                    v_num += 1
                    if words[i] == target:
                        print(answer)
                        return answer
        neighbor = nxt
    return 0
