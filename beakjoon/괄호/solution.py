n = int(input())
    
def check(string):
    q=[]
    if len(string)%2 !=0:
        return 'NO'
    for s in string:
        if s=='(':
            q.append(s)
        else :
            if len(q)==0:
                return 'NO'
            else :
                q.pop()
    if len(q) != 0:
        return 'NO'
    else:
        return 'YES'
    
for i in range(n):
    print(check(input()))  
