# 베스트 앨범
출처 : https://programmers.co.kr/learn/courses/30/lessons/42579# <br><br>

1. 해시, 정렬 <br>
2. genre를 정렬하기위한 g_num과 genre 안의 곡들을 정렬하기 위한 g_songs, 두개의 dictionary를 활용한다.
3. g_songs의 경우, 재생횟수가 같은 경우, 곡 고유 번호로 정렬해야 하기에 comparator 함수를 따로 정의하여 활용한다. g_songs의 요소들이 [곡번호, 재생횟수] 이므로
2번째 요소를 먼저 비교한 후, 첫번째 요소를 비교한다. 첫번째 요소(곡 번호)의 경우 같을 수 없다. 
> 파이썬3의 경우, comparator를 커스터마이즈하여 활용하고 싶은 경우, cmp_to_key 를 import 하여 활용하여야 한다.
