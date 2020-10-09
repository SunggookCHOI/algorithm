global dic
dic = {}
dic['0'] = [3,1]
dic['*'] = [3,0]
dic['#'] = [3,2]
i = 0
j = 0
for n in range(1,10):
    dic[str(n)] = [i,j]
    j+=1
    if j==3:
        i+=1
        j=0
def solution(numbers, hand):
    global dic
    answer = ''
    l = [3,0]
    r = [3,2]
    for n in numbers:
        near = get_nearest_hand(n,l,r)
        if n in [1,4,7]:
            answer += 'L'
            l = dic[str(n)]
        elif n in [3,6,9]:
            answer += 'R'
            r = dic[str(n)]
        else:
            if near == 'l':
                answer += 'L'
                l = dic[str(n)]
            elif near == 'r':
                answer += 'R'
                r = dic[str(n)]
            else:
                if hand =='right':
                    answer +='R'
                    r = dic[str(n)]
                else:
                    answer += 'L'
                    l = dic[str(n)]
                
    return answer

def get_nearest_hand(num,l,r):
    global dic
    tmp = dic[str(num)]
    l_dist = abs(l[0] - tmp[0]) + abs(l[1] - tmp[1])
    r_dist = abs(r[0] - tmp[0]) + abs(r[1] - tmp[1])
    if l_dist > r_dist:
        return 'r'
    elif l_dist < r_dist:
        return 'l'
    else :
        return 's'
