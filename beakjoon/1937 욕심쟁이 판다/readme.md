# 1937 욕심쟁이 판다
출처 : https://www.acmicpc.net/problem/1937 <br><br>

1. dp, dfs <br>
2. (i,j)에서 살 수 있는 일수를 life[[j][i]라하고, (i+1,j),(i-1,j),(i,j-1)로 이동이 가능하다고 하면, life[j][i]의 점화식은 아래와 같다. <br>
> life[j][i] = max(life[j-1][i],life[j][i-1],life[j][i+1])+1
3. 이렇게 dfs를 하되, 메모리제이션을 하며 진행함으로써 시간을 단축시킬 수 있다. <br>
4. 또한, 맵의 최대 크기는 500 * 500 으로 주어지는데, 파이썬의 경우 250000번의 재귀호출이 불가능하므로, sys.setrecursionlimit() 함수를 통해 재귀 최대 횟수를 늘려주어야 한다.
