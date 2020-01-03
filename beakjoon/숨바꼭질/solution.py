n,m=map(int,input().split())

if n==m:print(0)
else :
    answer = 0
    queue=[n]
    
    maxLen = 2*max(n,m)
    visited = [0 for i in range(maxLen+1)]
    visited[n]=1
    
    while True:
        answer += 1
        nextQ = []
        end = False
        while len(queue) != 0:
            q=queue.pop(0)
            if abs(q-m)==1:
                print(answer)
                end = True
                break
            elif 2*q == m :
                print(answer)
                end = True
                break
            else :
                if q-1>=0 and visited[q-1] == 0:
                    nextQ.append(q-1)
                    visited[q-1]=1
                if q+1 <= maxLen and visited[q+1] == 0:
                    nextQ.append(q+1)
                    visited[q+1]=1
                if 2*q <= maxLen and visited[2*q] == 0 :
                    nextQ.append(2*q)
                    visited[2*q]=1
        if end :
            break
        queue=nextQ
