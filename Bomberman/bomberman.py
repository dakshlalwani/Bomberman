from __future__ import print_function
import sys
import time
from timeout import *
import person
import bombs
import board
from getch import *


class BombermanGame:
    t = 3
    score = 0

    def levels(self, enemy_number, enemy_time, bomberman_time, level_number):
        print("You are at Level:", level_number)
        a = [[0 for y in range(19)] for x in range(17)]

        bomber = board.Board(a)
        bomb1 = person.move(a)
        bombact = bombs.Bombs(a, bomb1.posx, bomb1.posy)

        life = 1
        self.t = 3

        enemies = []
        for i in range(enemy_number):
            enemy = person.Enemy(a)
            if enemy.posx > 0 and enemy.posy > 0:
                enemies.append(enemy)
        prevgettime = time.time()

        while life:

            @timeout(0.1)
            def loop(prevtime):
                text = getch()
                gettime = time.time()
                if gettime - prevtime < bomberman_time\
                        and text in ['w', 'a', 's', 'd']:
                    return prevtime
                if text == 'q':
                    sys.exit(0)
                elif text == 'w':
                    bomb1.moveUp(a, self.score)
                elif text == 's':
                    bomb1.moveDown(a, self.score)
                elif text == 'a':
                    bomb1.moveLeft(a, self.score)
                elif text == 'd':
                    bomb1.moveRight(a, self.score)
                elif text == 'b' and bombact.flag == 0:
                    self.t = 3
                    bombact.time = 3
                    bombact.flag = 1
                    a[bomb1.posx][bomb1.posy] = 5
                for i in enemies:
                    i.moveenemy(a, self.score, enemy_time)
                if bombact.flag == 1 or bombact.flag == 2:
                    bombact.checkexplode(a, bomb1.posx, bomb1.posy)
                # if t == 2:
                #     bombact.time -= 1
                if bombact.time == 0 and bombact.flag == 1:
                    self.score = bombact.\
                        explode(a, enemies, bomb1.posx, bomb1.posy, self.score)
                    bombact.time = 1
                if bombact.time == 0 and bombact.flag == 2:
                    self.score = bombact.\
                        explode(a, enemies, bomb1.posx, bomb1.posy, self.score)
                    bombact.time = 3
                os.system('clear')
                print("You are at Level:", level_number)
                bomber.printboard(self.score, a, bombact.time)
                return gettime

            try:
                prevgettime = loop(prevgettime)
            except TimeoutError:
                for i in enemies:
                    i.moveenemy(a, self.score, enemy_time)
                if bombact.flag == 1 or bombact.flag == 2:
                    bombact.checkexplode(a, bombact.posx, bombact.posy)
                # if t == 2:
                #     bombact.time -= 1
                if bombact.time == 0 and bombact.flag == 1:
                    self.score = bombact.\
                        explode(a, enemies, bomb1.posx, bomb1.posy, self.score)
                    bombact.time = 1
                if bombact.time == 0 and bombact.flag == 2:
                    self.score = bombact.\
                        explode(a, enemies, bomb1.posx, bomb1.posy, self.score)
                    bombact.time = 3
                # print("a updated b")
                os.system('clear')
                print("You are at Level:", level_number)
                bomber.printboard(self.score, a, bombact.time)
            if enemies.__len__() == 0:
                return self.score

bombermangame = BombermanGame()
bombermangame.levels(7, 0.8, 0.45, 1)
bombermangame.levels(10, 0.6, 0.45, 2)
bombermangame.levels(12, 0.4, 0.25, 3)
bombermangame.levels(15, 0.25, 0.1, 4)
print("Gameover..YOU WON!!!")
