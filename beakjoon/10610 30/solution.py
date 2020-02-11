import sys,collections

def sol(n):
    dic = collections.Counter(n)
    check = sum(int(k)*v for k,v in dic.items())
    if "0" not in dic or check%3!=0:
        return -1
    else :
        ans = ""
        for i in range(9,-1,-1):
            str_i = str(i)
            if str_i in dic :
                for _ in range(dic[str_i]):
                    ans += str_i
        return ans

if __name__ == "__main__":
    n=sys.stdin.readline().split()[0]
    print(sol(n))
