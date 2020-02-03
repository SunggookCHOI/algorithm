# 11048 이동하기
출처 : https://www.acmicpc.net/problem/11048 <br><br>

1. dp <br>
2. row,col에 있는 사탕의 개수를 maze[row][col]이라 할때, row,col에서의 사탕의 최대개수 dp[row][col]의 점화식은 다음과 같다.<br>
> dp[row][col] = max(dp[row-1][col],dp[row][col-1])+maze[row][col]

처음엔 아래와 같이 maze를 모두 받은 후 시작하였고, 79336KB의 메모리와 1632ms의 시간이 사용되었다. <br>
```
import collections
import sys

def summation(maze):
    ans = 0
    for m in maze:
        ans += sum(m)
    return ans 

n,m = map(int,sys.stdin.readline().split())
maze = []
for i in range(n):
    maze.append(list(map(int,sys.stdin.readline().split())))


if n < 2 or m < 2:
    print(summation(maze))
else:
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0]=maze[0][0]
    q = collections.deque()
    q.append([1,0])
    q.append([0,1])
    while q:
        row,col = q.popleft()
        if col == 0 : dp[row][col]=dp[row-1][col]+maze[row][col]
        elif row == 0 : dp[row][col]=dp[row][col-1]+maze[row][col]
        else : dp[row][col] = max(dp[row-1][col]+maze[row][col], dp[row][col-1]+maze[row][col])

        if row == n and col == m : break
        if col == 0 and row < n-1 :
            q.append([row+1,col])
        if col < m-1 :
            q.append([row,col+1])
    print(dp[-1][-1])
```
이후 다른 사람의 풀이를 참고하여, maze를 다 저장해 둘 필요가 없을을 깨닫고 row별로 입력을 받으면서 그때그때 처리하였다
> dp[i] = max(dp[i-1]+maze[i],dp[i]+maze[i]) ; (왼쪽에서 오거나, 아래에서 오거나) <br>
> 반드시 왼쪽에서부터 수행해주어야 dp[i-1]이 최대화 되어있다. <br>
