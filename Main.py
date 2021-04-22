import pygame
import Board

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
PINK = (255,153,153)
YELLOW = (255,255,0)
ORANGE = (255,128,0)
PURPLE = (153,0,153)
DARKRED = (204,0,0)
LIGHTYELLOW = (255,255,204)
LIGHTGREEN = (204,255,153)
LIGHTPURPLE = (204,153,255)

GREY = (166,166,166)
BLACK = (0,0,0)
WHITE = (255,255,255)

default_size = (640,640)
default_topleft = [[(120, 120), (220, 120), (320, 120), (420, 120)],
             [(120, 220), (220, 220), (320, 220), (420, 220)],
             [(120, 320), (220, 320), (320, 320), (420, 320)],
             [(120, 420), (220, 420), (320, 420), (420, 420)]]

displayColor = {None: GREY, 2: LIGHTYELLOW, 4: LIGHTGREEN, 8: LIGHTPURPLE, 16: PINK, 32: YELLOW,
                64: ORANGE, 128: RED, 256: PURPLE, 512: DARKRED, 1024: BLUE, 2048: GREEN}

dircStr = {pygame.K_w: 'UP', pygame.K_s: 'DOWN', pygame.K_a: 'LEFT', pygame.K_d: 'RIGHT'}

class Game:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("2048")

        self.board = Board.Board()
        self.rows = len(self.board.board)
        self.columns = len(self.board.board[0])

        self.screen = pygame.display.set_mode(default_size)

        self.running = True

        self.win = False

        self.font = pygame.font.Font(None, 24)
        self.text = "2048. USE W,A,S,D to move all tiles."
        self.render(self.text)


    def render(self, text):
        self.text = text
        self.img = self.font.render(text, True, WHITE)


    def draw(self, value, i, j):
        font = pygame.font.SysFont(None, 24)

        if value is not None:
            img = font.render(str(value), True, BLACK)
        else:
            img = font.render(' ', True, BLACK)

        rect = pygame.Rect(default_topleft[i][j], (100, 100))

        pygame.draw.rect(self.screen, displayColor[value], rect)

        self.screen.blit(img, rect.center)


    def run(self):
        while self.running:
            if not self.win:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        dirc = event.key
                        if dirc in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                            self.board.move(dirc)
                            self.render('Move ' + dircStr[dirc])
                            print('Move ' + dircStr[dirc])
                        else:
                            self.render('Please CHOOSE from W,A,S,D.')

                self.screen.fill(BLACK)

                for i in range(self.rows):
                    for j in range(self.columns):
                        self.draw(self.board.board[i][j], i, j)

                if self.board.check():
                    self.win = True

                self.screen.blit(self.img, (30,30))

                pygame.display.flip()

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                self.screen.fill(BLACK)

                pygame.display.flip()


    pygame.quit()


if __name__ == '__main__':
    Game().run()