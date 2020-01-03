n = int(input())
target = sorted(map(int,input().split()))
m = int(input())
numbers = map(int,input().split())
def binSearch(x):
    l = 0
    r = n-1
    while l<=r:
        mid = (l+r)//2
        if target[mid] > x :
            r = mid -1
        elif target[mid] < x :
            l = mid + 1
        else :
            return 1
    return 0

for number in numbers :
    print(binSearch(number))
