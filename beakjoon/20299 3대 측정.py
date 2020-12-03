# https://www.acmicpc.net/problem/20299

import sys, re
readline = sys.stdin.readline
def main():
    n,k,l = map(int,readline().split())
    ans = 0
    vip = []
    for _ in range(n):
        records = list(map(int,readline().split()))
        if min(records) >= l and sum(records) >= k :
            ans += 1
            vip += records
    print(ans)
    print(re.sub(',','',str(vip)[1:-1]))
if __name__ == '__main__':
    main()
