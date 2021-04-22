import pygame
from random import random

class Board:
    ''' the 4 * 4 board on which we play 2048'''

    def __init__(self):
        self.board = [[None for i in range(4)] for j in range(4) ]
        # the main file will "interpreter" this board as visual blocks in a for loop
        self.rows = 4
        self.columns = 4

        self.board[0][0] = 2
        self.board[0][1] = 2
        self.board[1][0] = 2
        self.board[1][1] = 2

        print(self.board)

    def TwoOrFour(self):
        ''' call it when a 'merge' happened '''
        if random() < 0.5:
            return 2
        return 4

    def move(self, dirc):

        moved = []

        if dirc == pygame.K_w: # up
            for i in range(self.rows):
                for j in range(self.columns):

                    if i == 0:
                        break

                    current = self.board[i][j]
                    target = self.board[i - 1][j]

                    if  self.board[i][j] is None:  # if empty
                        pass

                    elif target is None:  # if target is empty
                        self.board[i - 1][j] = current
                        self.board[i][j] = None
                        moved.append([i, j])
                    elif target is not None and target == current: # a merge
                        self.board[i - 1][j] = 2 * self.board[i-1][j]
                        self.board[i][j] = None
                        moved.append([i, j])

        elif dirc == pygame.K_s: # down
            for m in range(self.rows):
                for j in range(self.columns):

                    i = self.rows - 1 - m  # move the button first

                    if i == 3:
                        break

                    current = self.board[i][j]
                    target = self.board[i + 1][j]

                    if self.board[i][j] is None:  # if empty
                        pass

                    elif target is None:  # if target is empty
                        self.board[i + 1][j] = current
                        self.board[i][j] = None
                        moved.append([i, j])
                    elif target is not None and target == current:  # a merge
                        self.board[i + 1][j] = 2 * self.board[i + 1][j]
                        self.board[i][j] = None
                        moved.append([i, j])


        elif dirc == pygame.K_a: # left
            for i in range(self.rows):
                for j in range(self.columns):

                    if j == 0:
                        pass
                    else:
                        current = self.board[i][j]
                        target = self.board[i][j - 1]

                        if self.board[i][j] is None:  # if empty
                            pass

                        elif target is None:  # if target is empty
                            self.board[i][j - 1] = current
                            self.board[i][j] = None
                            moved.append([i, j])
                        elif target is not None and target == current:  # a merge
                            self.board[i][j - 1] = 2 * self.board[i][j - 1]
                            self.board[i][j] = None
                            moved.append([i, j])

        elif dirc == pygame.K_d: # right
            for i in range(self.rows):
                for n in range(self.columns):

                    j = self.columns - 1 - n  # move the right column first

                    if j == 3:
                        pass
                    else:
                        current = self.board[i][j]
                        target = self.board[i][j + 1]

                        if self.board[i][j] is None:  # if empty
                            pass

                        elif target is None:  # if target is empty
                            self.board[i][j + 1] = current
                            self.board[i][j] = None
                            moved.append([i, j])
                        elif target is not None and target == current:  # a merge
                            self.board[i][j + 1] = 2 * self.board[i][j + 1]
                            self.board[i][j] = None
                            moved.append([i, j])

        print(self.board)

        for pair in moved:
            i = pair[0]
            j = pair[1]
            if self.board[i][j] is None:
                self.board[i][j] = self.TwoOrFour()

        print(self.board)



    def check(self):
        if 2048 in self.board:
            return True
        return False

