heap = []
def binSearch(target):
    l=0
    r=len(heap)-1
    while l<=r:
        mid = (l+r)//2
        if heap[mid]>target:
            r = mid -1
        elif heap[mid]<target:
            l=mid+1
        else :
            return mid
    return mid if target<=heap[mid] else mid+1

n = int(input())
#첫번째 줄
heap = sorted(list(map(int,input().split())))
for _i in range(n-1):
    temp = list(map(int,input().split()))
    next_target = []
    for i in range(n):
        if temp[i]>=heap[-n]:
            heap.insert(binSearch(temp[i]),temp[i])
            next_target.append(i)
    heap=heap[-n:]       
    target=next_target
print(heap[-n])
