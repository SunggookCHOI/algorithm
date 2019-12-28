import math

def solution(triangle):
    for i in range(1,len(triangle)):
        previous = triangle[i-1]
        present = triangle[i]
        
        for j in range(len(present)):
            if j == 0:
                present[j]+=previous[0]
            elif j == len(present)-1 :
                present[-1] += previous[-1]
            else :
                present[j] += max(previous[j-1],previous[j])
    return max(triangle[-1])
