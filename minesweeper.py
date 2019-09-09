import pygame
import random
pygame.init
pygame.font.init()

size = (500,500)
square_size = 15
white = (255,255,255)
red = (255, 0, 0)
blue = (0, 0, 255)

class cube:
    def __init__(self):
        self.searched = False
        self.isMine = False
        self.nearby = 0
    def reset(self):
        self.searched = False
        self.isMine = False
        self.nearby = 0

    def isNear(self):
        self.nearby = self.nearby +1

    def mined(self):
        self.isMine = True

class map:
    def __init__(self, row, col, mines):
        self.row = row
        self.col = col
        self.mines = mines
        self.cubes = [[cube() for i in range(0,col)] for j in range (0,row)]
        self.configField()

    def setMine(self, x, y):
        searching = True
        while searching:
            rand_x = random.randint(0, x)
            rand_y = random.randint(0, y)
            if not self.cubes[rand_x][rand_y].isMine:
                #print("x {0}, y {1}, randx {2}, randy {3}".format(x, y, rand_x, rand_y))
                self.cubes[rand_x][rand_y].mined()
                for i in range(0,3):
                    for j in range(0,3):
                        set_x = rand_x + i - 1
                        set_y = rand_y + j - 1
                        self.increaseCube(set_x,set_y)

                searching = False

    def increaseCube(self, x, y):
        #print("x {0}, y {1}".format(x, y))
        if x >= 0 and x <self.row and y >= 0 and y < self.col:
            self.cubes[x][y].isNear()

    def configField(self):
        for i in range(0,self.mines):
            self.setMine(self.row-1, self.col-1)
        return map

    def searchCube(self, x, y):
        if x < 0 or x >= self.row or y < 0 or y >= self.col:
            return False
        print("searching x {0}, y {1}".format(x, y))
        if self.cubes[x][y].searched:
            return False
        else:
            self.cubes[x][y].searched = True

        if self.cubes[x][y].isMine:
            return True
        elif self.cubes[x][y].nearby == 0:
            for i in range(-1,2):
                for j in range(-1, 2):
                    self.searchCube(x+i, y+j)
            return False
        return False


def drawGrid(window, gameMap):
    square_size = 15
    for i in range(0, gameMap.col):
        for j in range(0, gameMap.row):
            x = 30 + (j * square_size) + (j * 5)
            y = 30 + (i * square_size) + (i * 5)
            if gameMap.cubes[j][i].isMine and gameMap.cubes[j][i].searched:
                pygame.draw.rect(window, red, pygame.Rect(x, y, square_size, square_size))
            elif gameMap.cubes[j][i].searched:
                pygame.draw.rect(window, (0,255,0), pygame.Rect(x, y, square_size, square_size))
                if gameMap.cubes[j][i].nearby > 0:
                    displayNearby(gameMap, j, i, x, y)
            else:
                pygame.draw.rect(window, blue, pygame.Rect(x, y, square_size, square_size))

def displayNearby(gameMap, row, col, x, y):
    #print("near {0}".format(gameMap.cubes[row][col].nearby))
    font = pygame.font.SysFont(None, 25)
    near = font.render("{0}".format(gameMap.cubes[row][col].nearby), True, (0,0,0))
    window.blit(near, (x, y))

def reveal(x,y):
    cord_x = int((x-30)/20)
    cord_y = int((y-30)/20)
    return cord_x, cord_y



window = pygame.display.set_mode(size)
exit = False
clock = pygame.time.Clock()

gameMap = map(20, 20, 100)
gameOver = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            cord_x, cord_y = reveal(x, y)
            gameOver = gameMap.searchCube(cord_x, cord_y)
            print("game over {0}".format(gameOver))

        window.fill(white)
        drawGrid(window, gameMap)
        if gameOver:
            font = pygame.font.SysFont(None, 25)
            msg = font.render("{0}".format("MINE!! you lose"), True, (255, 0, 0))
            window.blit(msg, (0, 0))
        clock.tick(60)
        pygame.display.flip()
