from string import ascii_uppercase
def solution(msg):
    dic = {}
    idx=1
    for a in ascii_uppercase:
        dic[a] = idx
        idx+=1
    answer = []

    i=0
    j=i+1
    while i < len(msg)-1:
        j=i+1
        while j<= len(msg) and msg[i:j] in dic:
            j+=1
        answer.append(dic[msg[i:j-1]])
        dic[msg[i:j]]=idx
        idx += 1
        i=j-1
        #print(dic)
    if i == len(msg)-1:
        answer.append(dic[msg[-1]])
    return answer
