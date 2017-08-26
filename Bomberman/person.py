from __future__ import print_function
from board import *


class move:
    def __init__(self, a):
        self.posx = 1
        self.posy = 1
        self.id = 3
        self.count = 0
        self.flag = 0
        self.prevtime = time.time()
        self.ptime = time.time()
        a[self.posx][self.posy] = self.id

    def moveLeft(self, a, score):
        if self.posy > 1 and (a[self.posx][self.posy - 1] in [0, 3, 4]):
            c1 = a[self.posx][self.posy]
            c2 = a[self.posx][self.posy - 1]
            if ((c1 == 3 and c2 == 4) or (
                            c1 == 4 and c2 == 3)):
                os.system('clear')
                print("gameover...score =", score)
                sys.exit(0)
            if self.count != 0:
                a[self.posx][self.posy] = 5
            else:
                a[self.posx][self.posy] = 0
            a[self.posx][self.posy - 1] = self.id
            self.posy -= 1
            return 0
        else:
            return 1

    def moveRight(self, a, score):
        if self.posy < 18 and a[self.posx][self.posy + 1] in [0, 3, 4]:
            c1 = a[self.posx][self.posy]
            c2 = a[self.posx][self.posy + 1]
            if ((c1 == 3 and c2 == 4) or (
                            c1 == 4 and c2 == 3)):
                os.system('clear')
                print("gameover...score =", score)
                sys.exit(0)
            if self.count != 0:
                a[self.posx][self.posy] = 5
            else:
                a[self.posx][self.posy] = 0
            a[self.posx][self.posy + 1] = self.id
            self.posy += 1
            return 0
        else:
            return 1

    def moveUp(self, a, score):
        if self.posx > 1 and a[self.posx - 1][self.posy] in [0, 3, 4]:
            c1 = a[self.posx][self.posy]
            c2 = a[self.posx - 1][self.posy]
            if ((c1 == 3 and c2 == 4) or (
                            c1 == 4 and c2 == 3)):
                os.system('clear')
                print("gameover...score =", score)
                sys.exit(0)
            if self.count != 0:
                a[self.posx][self.posy] = 5
            else:
                a[self.posx][self.posy] = 0
            a[self.posx - 1][self.posy] = self.id
            self.posx -= 1
            return 0
        else:
            return 1

    def moveDown(self, a, score):
        if self.posx < 16 and a[self.posx + 1][self.posy] in [0, 3, 4]:
            c1 = a[self.posx][self.posy]
            c2 = a[self.posx + 1][self.posy]
            if ((c1 == 3 and c2 == 4) or (
                            c1 == 4 and c2 == 3)):
                os.system('clear')
                print("gameover...score =", score)
                sys.exit(0)
            if self.count != 0:
                a[self.posx][self.posy] = 5
            else:
                a[self.posx][self.posy] = 0
            a[self.posx + 1][self.posy] = self.id
            self.posx += 1
            return 0
        else:
            return 1


class Enemy(move):
    def __init__(self, a):
        p = randint(2, 15)
        q = randint(2, 17)
        self.id = 4
        if p * q > 15 and (a[p][q] == 0 or a[p][q] == 1):
            a[p][q] = self.id
            self.posx = p
            self.posy = q
        else:
            self.posx = -1
            self.posy = -1
        self.count = 0
        self.prevtime = time.time()

    def moveenemy(self, a, score, enemy_time):
        if time.time() - self.prevtime < enemy_time:
            return 0
        v = randint(0, 3)
        w = 4
        while (w):
            if v % 4 == 0:
                q = self.moveLeft(a, score)
            elif v % 4 == 1:
                q = self.moveRight(a, score)
            elif v % 4 == 2:
                q = self.moveDown(a, score)
            else:
                q = self.moveUp(a, score)
            if q == 0:
                break
            v = v + 1
            w = w - 1
        self.prevtime = time.time()
