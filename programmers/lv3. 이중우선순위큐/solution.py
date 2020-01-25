def solution(operations):
    q=[]
    for o in operations :
        temp = o.split()
        oper = temp[0]
        num = int(temp[1])
        if oper=="I":
            q.insert(binSearch(q,num),num)
        else:
            if len(q)==0:
                pass
            else:
                if num==-1:
                    q.pop(0)
                else:
                    q.pop()
    if len(q)==0:
        return [0,0]
    return [q[-1],q[0]]


def binSearch(q, target):
    if len(q)==0:
        return 0
    l=0
    r=len(q)-1
    while l<=r:
        mid=(l+r)//2
        if q[mid]<target:
            l=mid+1
        elif q[mid]>target:
            r=mid-1
        else :
            return mid
    while mid<len(q) and target>q[mid]:
        mid+=1
    return mid

