# 16638 ��ȣ �߰��ϱ�
��ó : https://www.acmicpc.net/problem/16638 <br><br>

1. dfs <br>
2. dfs(idx,nums,ops) �� nums�� ops�� num[idx], op[idx] �Ǵ� num[idx]�� num[idx+1] �� ���Ͽ� op[idx] ������ �� ���� op[idx]�� �־��ش�. <br>
3. ������ num�� �������� ��쿡�� op�� �־����� �ʰ� �������ν�, idx�� len(op)+1�� �����Ͽ����� nums�� ������ ops�� �������� 1�� ������ �Ѵ�. <br>
4. *������ ���� �� �־���ϹǷ�, ops���� *�� index�� ���� ã��, num[index]�� num[index]*num[index+1]�� �ٲپ��ش�. <br>
5. �� ��, ���� ops�� ���Ͽ� num[idx]�� num[idx] �� ���Ͽ� ops[index] ������ ���� ����� answer�� ���Ѵ�.
