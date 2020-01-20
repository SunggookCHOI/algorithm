n=int(input())
k=int(input())

def check(mid):
    num = 0
    for i in range(1,n+1):
        num+=min(mid//i,n)
    return num

def binSearch(n,k):
    l,r=0,k
    mid=(l+r)//2
    while l<=r:
        mid=(l+r)//2
        num = check(mid)
        if num >= k:
            r=mid-1
        else:
            l=mid+1
    if check(mid)<k:
        mid+=1
    print(mid)            
    
binSearch(n,k)
