n=int(input())
answer = 0
while n != 0:
    if n%5==0:
        answer+=n//5
        print(answer)
        break
    else :
        n-=3
        answer+=1
        if n==0:
            print(answer)
            break
    if n<0 :
        print(-1)
        break
