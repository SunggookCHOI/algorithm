#https://programmers.co.kr/learn/courses/30/lessons/81301
import re
def solution(s):
    answer = 0
    num = ['zero','one','two','three','four','five'
           ,'six','seven','eight','nine']
    # word_checker[0] = re.compile('zero')
    word_checker = [re.compile(x) for x in num]
    
    #num : 숫자, checker : re.compile('문자')
    # zero 부터 순서대로 숫자로 바꿔준다.
    for num,checker in enumerate(word_checker):
        tmp=checker.search(s)
        #s에서 '문자'를 모두 '숫자'로 바꾼다.
        while tmp:
            #문자가 s[i:j]이다.
            i,j=tmp.span()
            s = s[:i]+str(num)+s[j:]
            tmp=checker.search(s)
        
    #print(s)
    return int(s)
