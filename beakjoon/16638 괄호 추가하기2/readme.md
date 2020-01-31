# 16638 괄호 추가하기
출처 : https://www.acmicpc.net/problem/16638 <br><br>

1. dfs <br>
2. dfs(idx,nums,ops) 는 nums와 ops에 num[idx], op[idx] 또는 num[idx]와 num[idx+1] 에 대하여 op[idx] 연산을 한 값과 op[idx]를 넣어준다. <br>
3. 각각의 num이 마지막일 경우에는 op를 넣어주지 않고 끝냄으로써, idx가 len(op)+1에 도달하였을때 nums의 개수가 ops의 개수보다 1개 많도록 한다. <br>
4. *연산을 먼저 해 주어야하므로, ops에서 *의 index를 먼저 찾고, num[index]를 num[index]*num[index+1]로 바꾸어준다. <br>
5. 그 후, 남은 ops에 대하여 num[idx]와 num[idx] 에 대하여 ops[index] 연산을 해준 결과를 answer와 비교한다.
