import sys
n=int(sys.stdin.readline())
dic = {}
for i in range(n):
    f_list = sys.stdin.readline()
    f_idx = [j for j in range(n) if f_list[j]=='Y']
    for f in f_idx:
        #직접친구
        if i in dic:
            temp = dic[i]
            temp.add(f)
        else :
            temp = set()
            temp.add(f)
        dic[i]=temp
        if f in dic:
            temp = dic[f]
            temp.add(i)
        else :
            temp = set()
            temp.add(i)
        dic[f]=temp
        # 친구의 친구
        f_set = dic[f]
        for f2 in f_idx:
            if f==f2: continue
            f_set.add(f2)
            if f2 in dic:
                temp = dic[f2]
                temp.add(f)
            else :
                temp = set()
                temp.add(f)
            dic[f2] = temp
        dic[f]=f_set
ans = 0
for v in dic.values():
    if len(v)>ans:
        ans = len(v)
print(ans)
