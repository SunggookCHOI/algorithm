# 16637 괄호 추가하기
출처 : https://www.acmicpc.net/problem/16637 <br><br>

1. dfs <br>
2. operator의 인덱스(i)를 기준으로 num[i]와 num[i+1]을 op[i]로 연산하거나, num[i]와 num[i+1]과 num[i+2]를 op[i+1]로 연산한 것과 연산한다.
