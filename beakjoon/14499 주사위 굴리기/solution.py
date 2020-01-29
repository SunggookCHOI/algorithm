class Dice:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.front = 0
        self.back = 0
    def roll(self, direction, num):
        if direction == 1:
            temp = self.right
            self.right = self.up
            self.up = self.left
            self.left = self.down
            if num ==0 :
                self.down = temp
            else :
                self.down = num
            print(self.up)
        elif direction == 2:
            temp = self.left
            self.left = self.up
            self.up=self.right
            self.right = self.down
            self.down = num
            if num ==0 :
                self.down = temp
            else :
                self.down = num
            print(self.up)
        elif direction == 3:
            temp = self.front
            self.front = self.up
            self.up = self.back
            self.back = self.down
            if num ==0 :
                self.down = temp
            else :
                self.down = num
            print(self.up)
        elif direction == 4:
            temp = self.back
            self.back = self.up
            self.up = self.front
            self.front = self.down
            if num ==0 :
                self.down = temp
            else :
                self.down = num
            print(self.up)
    def getDown(self):
        return self.down
    def me(self) :
        print("-----------")
        print(" "+str(self.front))
        print(str(self.left)+str(self.up)+str(self.right))
        print(" "+str(self.back))
        print(" "+str(self.down))
        print("---------------")

import sys

if __name__ == '__main__':
    n,m,y,x,k = map(int,sys.stdin.readline().split())
    maps = []
    for i in range(n):
        maps.append(list(map(int,sys.stdin.readline().split())))
    order = list(map(int,sys.stdin.readline().split()))

    dice = Dice()
    for o in order:
        #print("현재위치 : ", x,y,o)
        if o==1 and x<m-1:
            dice.roll(o,maps[y][x+1])
            if maps[y][x+1] != 0:
                maps[y][x+1] = 0
            else :
                maps[y][x+1] = dice.getDown()
            x+=1
        elif o==2 and x>0:
            dice.roll(o,maps[y][x-1])
            if maps[y][x-1] != 0:
                maps[y][x-1] = 0
            else :
                maps[y][x-1] = dice.getDown()
            x-=1
        elif o==3 and y>0:
            dice.roll(o,maps[y-1][x])
            if maps[y-1][x] != 0:
                maps[y-1][x] = 0
            else :
                maps[y-1][x] = dice.getDown()
            y-=1
        elif o==4 and y<n-1:
            dice.roll(o,maps[y+1][x])
            if maps[y+1][x] != 0:
                maps[y+1][x] = 0
            else :
                maps[y+1][x] = dice.getDown()
            y+=1
        #dice.me()
        #print(maps)
