import sys

def bin_search(arr, t):
    l=0
    r=len(arr)
    if t > arr[-1]:return len(arr)
    elif t<arr[0]:return 0
    mid = (l+r)//2
    while l<=r:
        if arr[mid] > t:
            r=mid-1
        elif arr[mid] < t:
            l = mid+1
        else:
            return mid
        mid = (l+r)//2
    return mid+1

n=map(int,sys.stdin.readline())
a_i = list(map(int,sys.stdin.readline().split()))

dp=[0]
p_i=[0]

for a in a_i:
    idx = bin_search(p_i,a)
    if idx == len(p_i):
        p_i.append(a)
    else:
        p_i[idx] = a
    dp.append(idx)
print(max(dp))
