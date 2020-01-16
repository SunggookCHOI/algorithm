import sys
n,m = map(int,input().split())
r, c, direction = map(int,input().split())
present = [r,c]

maps = []
for _i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    maps.append(temp)
checker=True
done = 0
maps[present[0]][present[1]] = 2
done += 1

def check_east(present):
    if present[1]+1<m and maps[present[0]][present[1]+1] == 0:
        return True
    return False
    
def check_west(present):
    if present[1]-1>=0 and maps[present[0]][present[1]-1] == 0:
        return True
    return False

def check_south(present):
    if present[0]+1<n and maps[present[0]+1][present[1]] == 0:
        return True
    return False
def check_north(present):
    if present[0]-1>=0 and maps[present[0]-1][present[1]] == 0:
        return True
    return False

while checker:
    #북쪽
    if direction == 0:
        #서쪽 청소
        if check_west(present):
            maps[present[0]][present[1]-1] = 2
            present = [present[0],present[1]-1]
            direction = 3
            done+=1
            continue
        #남쪽 청소
        elif check_south(present):
            maps[present[0]+1][present[1]] = 2
            present = [present[0]+1,present[1]]
            direction = 2
            done+=1
            continue
        #동
        elif check_east(present):
            maps[present[0]][present[1]+1] = 2
            present = [present[0],present[1]+1]
            direction = 1
            done+=1
            continue
        #북
        elif check_north(present):
            maps[present[0]-1][present[1]] = 2
            present = [present[0]-1,present[1]]
            direction = 0
            done+=1
            continue
        else :
            if present[0]+1==n or maps[present[0]+1][present[1]] ==1:
                checker = False
            else :
                present = [present[0]+1,present[1]]
            
    #서쪽
    if direction == 3:
        #남쪽 청소
        if check_south(present):
            maps[present[0]+1][present[1]] = 2
            present = [present[0]+1,present[1]]
            direction = 2
            done+=1
            continue
        #동
        elif check_east(present):
            maps[present[0]][present[1]+1] = 2
            present = [present[0],present[1]+1]
            direction = 1
            done+=1
            continue
        #북
        elif check_north(present):
            maps[present[0]-1][present[1]] = 2
            present = [present[0]-1,present[1]]
            direction = 0
            done+=1
            continue
        #서쪽 청소
        elif check_west(present):
            maps[present[0]][present[1]-1] = 2
            present = [present[0],present[1]-1]
            direction = 3
            done+=1
            continue
        else :
            if present[1]+1==m or maps[present[0]][present[1]+1] ==1:
                checker = False
            else :
                present = [present[0],present[1]+1]
    #남쪽
    if direction == 2:
        #동
        if check_east(present):
            maps[present[0]][present[1]+1] = 2
            present = [present[0],present[1]+1]
            direction = 1
            done+=1
            continue
        #북
        elif check_north(present):
            maps[present[0]-1][present[1]] = 2
            present = [present[0]-1,present[1]]
            direction = 0
            done+=1
            continue
        #서쪽 청소
        elif check_west(present):
            maps[present[0]][present[1]-1] = 2
            present = [present[0],present[1]-1]
            direction = 3
            done+=1
            continue
        #남쪽 청소
        elif check_south(present):
            maps[present[0]+1][present[1]] = 2
            present = [present[0]+1,present[1]]
            direction = 2
            done+=1
            continue
        else :
            if present[0]-1==-1 or maps[present[0]-1][present[1]] ==1:
                checker = False
            else :
                present = [present[0]-1,present[1]]
         
    #동쪽
    if direction == 1:
        #북
        if check_north(present):
            maps[present[0]-1][present[1]] = 2
            present = [present[0]-1,present[1]]
            direction = 0
            done+=1
            continue
        #서쪽 청소
        elif check_west(present):
            maps[present[0]][present[1]-1] = 2
            present = [present[0],present[1]-1]
            direction = 3
            done+=1
            continue
        #남쪽 청소
        elif check_south(present):
            maps[present[0]+1][present[1]] = 2
            present = [present[0]+1,present[1]]
            direction = 2
            done+=1
            continue
        #동
        elif check_east(present):
            maps[present[0]][present[1]+1] = 2
            present = [present[0],present[1]+1]
            direction = 1
            done+=1
            continue
        else :
            if present[1]-1==-1 or maps[present[0]][present[1]-1] ==1:
                checker = False
            else :
                present = [present[0],present[1]-1]
print(done)
