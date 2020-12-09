import sys
readline = sys.stdin.readline
 
def main(n):
    for _ in range(n):
        #l = sorted([tuple(map(int,readline().split())) for _ in range(int(readline()))],key = lambda x : x[0])
        l = []
        for x in range(int(readline())):
            l.append(tuple(map(int,readline().split())))
        l = sorted(l,key = lambda x : x[0])
        tmp = l[0][1]
        ans = 1
        for n,m in l:
            if m < tmp :
                tmp = m
                ans += 1
        print(ans)
if __name__ == '__main__':
    n =int(readline())
    main(n)
