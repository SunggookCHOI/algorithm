def check(string):
    string_len = len(string)-1
    for i in range(len(string)//2):
        if string[i] != string[string_len - i]:
            return False
    return True
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(len(s)-1,i-1,-1):
            if j-i+1 < answer : break
            if check(s[i:j+1]) and  j-i+1 > answer :
                answer = j-i+1

    return answer