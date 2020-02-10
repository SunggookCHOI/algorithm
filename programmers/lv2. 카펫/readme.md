# lv2. 카펫
출처 : https://programmers.co.kr/learn/courses/30/lessons/42842 <br><br>

1. 완전탐색 <br>
2. red를 r행으로 만들면 red의 폭 red_width = red//r 이 된다. <br>
3. red를 위와 같이 하면, brown은 위의 red를 한칸씩 감싸는 형태가 되므로, 맨 위와 맨 아래 행의 brown_width는 red_width+2 가 되고, 그 사이의 brown의 개수는
 r*2가 된다. (행마다 맨 앞과 맨 뒤 한칸씩) <br>
4. 따라서 (brown_width+2)*2 + r*2 가 brown이 되는 r 값을 찾아서 [brown_width, r+2] 를 반환해주면된다.<br>
5. 따로 예외처리에 관한 조건이 없으므로, 불가능한 경우는 고려하지 않았다.
