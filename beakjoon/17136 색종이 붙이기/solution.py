import sys

paper = []
for i in range(10):
    paper.append(list(map(int,sys.stdin.readline().split())))

empty = []
for row in range(len(paper)):
    for col in range(len(paper[row])):
        if paper[row][col] == 1:
            empty.append([row,col])

ans = [0,0,0,0,0]
def getSize(x,y,size, empty):
    temp_empty = empty.copy()
    ans = False
    if x+size-1 < len(paper) and y+size-1 < len(paper):
        ans = True
        for row in range(y,y+size):
            if [row,x+size-1] not in empty:
                ans = False
                break
            else :
                temp_empty.remove([row,x+size-1])
        if ans:
            for col in range(x,x+size-1):
                if [y+size-1,col] not in empty:
                    ans = False
                    break
                else:
                    temp_empty.remove([y+size-1,col])
    return ans, temp_empty

global answer
answer = 26

def solve(empty, ans):
    #print(empty,ans)
    global answer
    if max(ans) >5 or sum(ans) > answer:
        return ;
    if len(empty) == 0 :
        if answer > sum(ans):
            answer = sum(ans)
        return ;
    x,y=empty[0][1],empty[0][0]
    for size in range(1,6):
        temp = getSize(x,y,size,empty)
        if temp[0]:
            temp_ans = ans.copy()
            temp_ans[size-1] += 1
            empty = temp[1]
            solve(empty,temp_ans)
        else :
            return ;
solve(empty,[0,0,0,0,0])
if answer == 26 : answer = -1
print(answer)
