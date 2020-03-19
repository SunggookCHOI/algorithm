import string, sys
al = string.ascii_uppercase
k=int(sys.stdin.readline())
n=int(sys.stdin.readline())
al = list(al[:k])
answer = list(sys.stdin.readline()[:-1])
def swap(i):
    temp = al[i]
    al[i] = al[i+1]
    al[i+1] = temp

def swap2(i):
    temp = answer[i]
    answer[i] = answer[i+1]
    answer[i+1] = temp

for i in range(n):
    ladder = sys.stdin.readline().split()[0]
    if ladder[0] == "?":
        break
    else:
        for idx,l in enumerate(ladder):
            if l =="-":
                swap(idx)

rest = [sys.stdin.readline().split()[0] for _ in range(i+1,n)]
rest.reverse()
for ladder in rest:
    for idx,l in enumerate(ladder):
        if l =="-":
            swap2(idx)
ans = ""

for i in range(k-1):
    if al[i] == answer[i]:
        ans += "*"
    elif al[i] == answer[i+1] and al[i+1]==answer[i] and (i==0 or ans[-1] == "*"):
        ans += "-"
        swap(i)
    else:
        ans = "x" * (k-1)
        break
print(ans)
