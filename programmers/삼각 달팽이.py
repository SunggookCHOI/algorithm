def solution(n):
    direction = ['down','right','diagonal']
    check = 0
    answer = []
    square = [[0 for i in range(n)] for j in range(n)]
    i,j = 0,0
    square[j][i] = 1
    tot = sum(i for i in range(1,n+1))
    for s in range(2,tot+1):
        d = direction[check%3]
        if d == 'down':
            if j+1==n or square[j+1][i] != 0:
                check += 1
                if square[j][i+1] != 0:
                    # 끝
                    break
                else :
                    square[j][i+1] = s
                    i += 1
            else:
                square[j+1][i] = s
                j += 1
        elif d == 'right':
            if i+1 == n or square[j][i+1] != 0 :
                check += 1
                if square[j-1][i-1] == 1:
                    break
                else :
                    square[j-1][i-1] = s
                    j-=1
                    i-=1
            else :
                square[j][i+1] = s
                i += 1
        else :
            if square[j-1][i-1] != 0:
                check +=1
                if square[j+1][i] == 1:
                    break
                else :
                    square[j+1][i] = s
                    j += 1
            else :
                square[j-1][i-1] = s
                j -= 1
                i -= 1
    for i,v in enumerate(square):
        answer += v[:i+1]
    return answer

