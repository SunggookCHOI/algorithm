def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        tmp = compress(i,s)
        answer = min(answer,tmp)
    return answer


def compress(num,s):
    ans = ''
    i = 0
    j = num
    cnt = 1
    while i<len(s):
        if s[i:i+num] == s[j:j+num]:
            cnt += 1
            j += num
            if j + num > len(s):
                ans = ans + str(cnt) + s[i:i+num] if cnt != 1 else ans + s[i:i+num]
                ans += s[j:]
                break
        else:
            ans = ans + str(cnt) + s[i:i+num] if cnt != 1 else ans + s[i:i+num]
            i = j
            j += num
            cnt=1
            
    return len(ans)
