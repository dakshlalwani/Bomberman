from __future__ import print_function
from person import *
from timeout import *
import sys
import time


class Bombs:
    def __init__(self, a, x, y):
        self.id = 5
        self.posx = x
        self.posy = y
        self.prevtime = time.time()
        self.count = 0
        self.time = 3
        self.t = 2
        self.flag = 0

    def checkexplode(self, a, x, y):
        if time.time() - self.prevtime > 0.8:
            self.prevtime = time.time()
            if self.time == 3:
                self.posx = x
                self.posy = y
            self.time -= 1
            a[self.posx][self.posy] = 5

    def explode(self, a, enemies, x, y, score):
        if self.flag == 1:
            a[self.posx][self.posy] = 6
            if a[self.posx - 1][self.posy] != 2:
                for i in enemies:
                    if (self.posx - 1 == i.posx and self.posy == i.posy) \
                            or (self.posx == i.posx and self.posy == i.posy):
                        enemies.remove(i)
                        score += 100
                        if enemies.__len__() == 0:
                            return score
                if a[self.posx - 1][self.posy] == 1:
                    score += 20
                if a[self.posx - 1][self.posy] == 3:
                    os.system('clear')
                    print("gameover...score =", score)
                    sys.exit(0)
                a[self.posx - 1][self.posy] = 6
            if a[self.posx + 1][self.posy] != 2:
                for i in enemies:
                    if (self.posx + 1 == i.posx and self.posy == i.posy)\
                            or (self.posx == i.posx and self.posy == i.posy):
                        enemies.remove(i)
                        score += 100
                        if enemies.__len__() == 0:
                            return score
                if a[self.posx + 1][self.posy] == 1:
                    score += 20
                if a[self.posx + 1][self.posy] == 3:
                    os.system('clear')
                    print("gameover...score =", score)
                    sys.exit(0)
                a[self.posx + 1][self.posy] = 6
            if a[self.posx][self.posy - 1] != 2:
                for i in enemies:
                    if (self.posx == i.posx and self.posy - 1 == i.posy) \
                            or (self.posx == i.posx and self.posy == i.posy):
                        enemies.remove(i)
                        score += 100
                        if enemies.__len__() == 0:
                            return score
                if a[self.posx][self.posy - 1] == 1:
                    score += 20
                if a[self.posx][self.posy - 1] == 3:
                    os.system('clear')
                    print("gameover...score =", score)
                    sys.exit(0)
                a[self.posx][self.posy - 1] = 6
            if a[self.posx][self.posy + 1] != 2:
                for i in enemies:
                    if (self.posx == i.posx and self.posy + 1 == i.posy) \
                            or (self.posx == i.posx and self.posy == i.posy):
                        enemies.remove(i)
                        score += 100
                        if enemies.__len__() == 0:
                            return score
                if a[self.posx][self.posy + 1] == 1:
                    score += 20
                if a[self.posx][self.posy + 1] == 3:
                    os.system('clear')
                    print("gameover...score =", score)
                    sys.exit(0)
                a[self.posx][self.posy + 1] = 6
            self.flag = 2

        elif self.flag == 2:
            a[self.posx][self.posy] = 0
            if a[self.posx - 1][self.posy] != 2:
                for i in enemies:
                    if self.posx - 1 == i.posx and self.posy == i.posy:
                        enemies.remove(i)
                if a[self.posx - 1][self.posy] == 3:
                    os.system('clear')
                    print("gameover...score =", score)
                    sys.exit(0)
                a[self.posx - 1][self.posy] = 0
            if a[self.posx + 1][self.posy] != 2:
                for i in enemies:
                    if self.posx - 1 == i.posx and self.posy == i.posy:
                        enemies.remove(i)
                a[self.posx + 1][self.posy] = 0
            if a[self.posx][self.posy - 1] != 2:
                for i in enemies:
                    if self.posx - 1 == i.posx and self.posy == i.posy:
                        enemies.remove(i)
                a[self.posx][self.posy - 1] = 0
            if a[self.posx][self.posy + 1] != 2:
                for i in enemies:
                    if self.posx - 1 == i.posx and self.posy == i.posy:
                        enemies.remove(i)
                a[self.posx][self.posy + 1] = 0
            self.flag = 0
            self.posx = x
            self.posy = y
        return score
