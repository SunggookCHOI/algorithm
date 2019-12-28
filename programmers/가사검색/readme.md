# 가사검색
출처 : https://programmers.co.kr/learn/courses/30/lessons/60060
<br>
## 문제 설명
각 query를 만족하는 가사들의 개수를 반환
<br>
## 문제 풀이
정규 표현식을 이용하여 query for문 안에 word for문을 돌리면 효율성을 통과할 수 없다.<br>
즉, 효과적인 검색을 위한 저장을 고려해야 한다. -> trie 자료 구조<br>

1. retrieval tree 의 약자로 문자열 검색에 특화된 알고리즘
2. word의 길이로 root node 구분
3. query를 거꾸로 수행하기 위해 원래의 단어 tree와 뒤집힌 단어의 tree 두가지를 구축해야 한다
