def solution(n, number):
    global min
    min=9
    for i in range(1,9):
        sol(n,number,i,digit(i,n))
        sol(n,number,i,-digit(i,n))
    if min>8:
        return -1
    else:
        return min

def sol(n,number,count,result):
    global min
    if count>=min:
        return ;
    if result==number and count<min :
        min=count   
    
    
    rest=9-count
    sol(n,number,count+1,result+n)
    sol(n,number,count+1,result-n)
    sol(n,number,count+1,result*n)
    
    if number-result <= rest/2 and number-result>0 :
        if count+((number-result)*2) <min :
            min = count+((number-result)*2)
    elif result-number <= rest/2 and result-number>0 :
        if count+((result-number)*2) < min :
            min = count+((result-number)*2)
    
    for i in range(1,rest) :
        if result%digit(i,n)==0:
            sol(n,number,count+i,result/digit(i,n))
            sol(n,number,count+i,result/(-digit(i,n)))
        sol(n,number,count+i,result+digit(i,n))
        sol(n,number,count+i,result-digit(i,n))
        sol(n,number,count+i,result*digit(i,n))
        
def digit(digits,n):
    answer=''
    for i in range(digits):
        answer+=str(n)
    return int(answer)
