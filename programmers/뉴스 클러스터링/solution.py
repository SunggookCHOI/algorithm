import re

def solution(str1, str2):
    checker = re.compile('[a-zA-Z]{2}')
    answer = 0
    
    token1 = []
    token2 = []
    # tokenize
    for i in range(len(str1)-1):
        t1 = str1[i:i+2]
        if checker.match(t1) != None:
            token1.append(t1.lower())
    for i in range(len(str2)):
        t2 = str2[i:i+2]
        if checker.match(t2) != None:
            token2.append(t2.lower())
    
    intersection = 0
    union = 0
    
    # count intersection and union of the two tokens
    for t in token1:
        if t in token2:
            intersection+=1
            union += 1
            token2.remove(t)
        else :
            union+=1
    union += len(token2)
    return int((intersection/union) * 65536) if intersection+union != 0 else 65536
