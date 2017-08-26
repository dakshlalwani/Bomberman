from __future__ import print_function
from bombs import *
from random import randint


class Board:
    def __init__(self, a):
        self.id = 2
        for j in range(19):
            a[0][j] = self.id
            a[16][j] = self.id
        for i in range(1, 16, 1):
            if i % 2 == 0:
                for j in range(1, 19, 1):
                    if j % 2 == 0:
                        a[i][j] = self.id
            else:
                a[i][0] = self.id
                a[i][18] = self.id

        for i in range(75):
            x = randint(1, 15)
            y = randint(1, 17)
            if x * y > 2 and a[x][y] == 0:
                a[x][y] = 1
        self.count = 0

    def printboard(self, score, a, p):
        print("Your Score is", score)
        print("Press 'q' to quit the game")
        for i in range(34):
            if i // 2 >= 1 and i // 2 < 16:
                print('\x1b[0;37;47m' + "XXXX" + '\x1b[0m', end='')
                if i % 4 == 0 or i % 4 == 1:
                    for j in range(1, 19, 1):
                        if j % 2 == 0 and a[i // 2][j] == 2:
                            print('\x1b[0;37;47m' + "XXXX" + '\x1b[0m', end='')
                        else:
                            if a[i // 2][j] == 0:
                                print("    ", end='')
                            elif a[i // 2][j] == 1:
                                print('\x1b[1;32;42m'+"////"+'\x1b[0m', end='')
                            elif a[i // 2][j] == 3:
                                print('\x1b[1;32;46m'+"BBBB"+'\x1b[0m', end='')
                            elif a[i // 2][j] == 4:
                                print('\x1b[1;33;41m'+"EEEE"+'\x1b[0m', end='')
                            elif a[i // 2][j] == 5:
                                m = str(p) + str(p) + str(p) + str(p)
                                print('\x1b[1;37;41m' + m + '\x1b[0m', end='')
                            elif a[i // 2][j] == 6:
                                print('\x1b[1;32;44m'+"eeee"+'\x1b[0m', end='')
                    print(end='\n')
                else:
                    for j in range(1, 19, 1):
                        if a[i // 2][j] == 0:
                            print("    ", end='')
                        elif a[i // 2][j] == 1:
                            print('\x1b[1;32;42m' + "////" + '\x1b[0m', end='')
                        elif a[i // 2][j] == 2 and j > 0:
                            print('\x1b[0;37;47m' + "XXXX" + '\x1b[0m', end='')
                        elif a[i // 2][j] == 3:
                            print('\x1b[1;32;46m' + "BBBB" + '\x1b[0m', end='')
                        elif a[i // 2][j] == 4:
                            print('\x1b[1;33;41m' + "EEEE" + '\x1b[0m', end='')
                        elif a[i // 2][j] == 5:
                            m = str(p) + str(p) + str(p) + str(p)
                            print('\x1b[1;37;41m' + m + '\x1b[0m', end='')
                        elif a[i // 2][j] == 6:
                            print('\x1b[1;32;44m' + "eeee" + '\x1b[0m', end='')
                    print(end='\n')

            elif i / 2 < 1:
                for j in range(19):
                    print('\x1b[0;37;47m' + "XXXX" + '\x1b[0m', end='')
                print(end='\n')
            else:
                for j in range(19):
                    print('\x1b[0;37;47m' + "XXXX" + '\x1b[0m', end='')
                print(end='\n')
