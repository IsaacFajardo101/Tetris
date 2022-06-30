import pygame
import copy
import random
from sys import exit


class Piece:
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state
        self.ismoving = False


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


def SetupNodes():
    for y in range(20):
        for x in range(10):
            AllPieces.append(Piece([x, y], "Empty"))
    AllPieces.reverse()

    for y in range(4):
        for x in range(4):
            HoldingPieces.append(Piece([x, y], "Empty"))

    for y in range(4):
        for x in range(4):
            NextPieces.append(Piece([x, y], "Empty"))


def UpdateColorNodes(NodeList, Where):
    if Where == "All":
        for node in NodeList:
            if node.state == "Blue":
                screen.blit(BlueBlock, (125 + (node.pos[0] * 25), 0 + (node.pos[1] * 25)))
            if node.state == "Green":
                screen.blit(GreenBlock, (125 + (node.pos[0] * 25), 0 + (node.pos[1] * 25)))
            if node.state == "LightBlue":
                screen.blit(LightBlueBlock, (125 + (node.pos[0] * 25), 0 + (node.pos[1] * 25)))
            if node.state == "Orange":
                screen.blit(OrangeBlock, (125 + (node.pos[0] * 25), 0 + (node.pos[1] * 25)))
            if node.state == "Purple":
                screen.blit(PurpleBlock, (125 + (node.pos[0] * 25), 0 + (node.pos[1] * 25)))
            if node.state == "Red":
                screen.blit(RedBlock, (125 + (node.pos[0] * 25), 0 + (node.pos[1] * 25)))
            if node.state == "Yellow":
                screen.blit(YellowBlock, (125 + (node.pos[0] * 25), 0 + (node.pos[1] * 25)))
            if node.state == "Empty":
                screen.blit(EmptyBlock, (125 + (node.pos[0] * 25), 0 + (node.pos[1] * 25)))
    if Where == "Hold":
        for node in NodeList:
            if node.state == "Blue":
                screen.blit(BlueBlock, (12 + (node.pos[0] * 25), 12 + (node.pos[1] * 25)))
            if node.state == "Green":
                screen.blit(GreenBlock, (12 + (node.pos[0] * 25), 12 + (node.pos[1] * 25)))
            if node.state == "LightBlue":
                screen.blit(LightBlueBlock, (12 + (node.pos[0] * 25), 12 + (node.pos[1] * 25)))
            if node.state == "Orange":
                screen.blit(OrangeBlock, (12 + (node.pos[0] * 25), 12 + (node.pos[1] * 25)))
            if node.state == "Purple":
                screen.blit(PurpleBlock, (12 + (node.pos[0] * 25), 12 + (node.pos[1] * 25)))
            if node.state == "Red":
                screen.blit(RedBlock, (12 + (node.pos[0] * 25), 12 + (node.pos[1] * 25)))
            if node.state == "Yellow":
                screen.blit(YellowBlock, (12 + (node.pos[0] * 25), 12 + (node.pos[1] * 25)))
            if node.state == "Empty":
                screen.blit(EmptyBlock, (12 + (node.pos[0] * 25), 12 + (node.pos[1] * 25)))
    if Where == "Next":
        for node in NodeList:
            if node.state == "Blue":
                screen.blit(BlueBlock, (389 + (node.pos[0] * 25), 11 + (node.pos[1] * 25)))
            if node.state == "Green":
                screen.blit(GreenBlock, (389 + (node.pos[0] * 25), 11 + (node.pos[1] * 25)))
            if node.state == "LightBlue":
                screen.blit(LightBlueBlock, (389 + (node.pos[0] * 25), 11 + (node.pos[1] * 25)))
            if node.state == "Orange":
                screen.blit(OrangeBlock, (389 + (node.pos[0] * 25), 11 + (node.pos[1] * 25)))
            if node.state == "Purple":
                screen.blit(PurpleBlock, (389 + (node.pos[0] * 25), 11 + (node.pos[1] * 25)))
            if node.state == "Red":
                screen.blit(RedBlock, (389 + (node.pos[0] * 25), 11 + (node.pos[1] * 25)))
            if node.state == "Yellow":
                screen.blit(YellowBlock, (389 + (node.pos[0] * 25), 11 + (node.pos[1] * 25)))
            if node.state == "Empty":
                screen.blit(EmptyBlock, (389 + (node.pos[0] * 25), 11 + (node.pos[1] * 25)))


def UpdateTick(allmoving):
    edge = False
    blocked = False

    themoving = copy.deepcopy(allmoving)

    for thing in themoving:
        if thing.pos[1] == 19:
            edge = True

    for place in themoving:
        place.pos[1] += 1

    for place in themoving:
        for square in AllPieces:
            if square.pos == place.pos:
                if not square.ismoving:
                    if square.state != "Empty":
                        blocked = True

    if edge:
        blocked = True

    if not blocked:
        return True
    if blocked:
        return False


def MoveCheck(allmoving):
    edge = False
    blocked = False

    themoving = copy.deepcopy(allmoving)

    for thing in themoving:
        if Direction == "Right":
            if thing.pos[0] == 9:
                edge = True
        if Direction == "Left":
            if thing.pos[0] == 0:
                edge = True

    if not edge:
        if Direction == "Right":
            for place in themoving:
                place.pos[0] += 1
        if Direction == "Left":
            for place in themoving:
                place.pos[0] -= 1

        for place in themoving:
            for square in AllPieces:
                if square.pos == place.pos:
                    if not square.ismoving:
                        if square.state != "Empty":
                            blocked = True
    else:
        blocked = True

    if not blocked:
        return True
    if blocked:
        return False


def PieceCords(name):
    if name == "Square":
        squarepos = [[4, 0],
                     [4, 1],
                     [5, 0],
                     [5, 1]]
        return squarepos
    if name == "L":
        lpos = [[4, 0],
                [4, 1],
                [4, 2],
                [5, 2]]
        return lpos
    if name == "LR":
        lrpos = [[5, 0],
                 [5, 1],
                 [5, 2],
                 [4, 2]]
        return lrpos
    if name == "Line":
        linepos = [[5, 0],
                   [5, 1],
                   [5, 2],
                   [5, 3]]
        return linepos
    if name == "T":
        tpos = [[5, 0],
                [5, 1],
                [4, 1],
                [6, 1]]
        return tpos
    if name == "Z":
        zpos = [[5, 0],
                [5, 1],
                [4, 1],
                [4, 2]]
        return zpos
    if name == "ZR":
        zrpos = [[4, 0],
                 [4, 1],
                 [5, 1],
                 [5, 2]]
        return zrpos


Background = pygame.image.load("Assets/Bg.png").convert()
BlueBlock = pygame.image.load("Assets/BlueBlock.png").convert()
GreenBlock = pygame.image.load("Assets/GreenBlock.png").convert()
LightBlueBlock = pygame.image.load("Assets/LightBlueBlock.png").convert()
OrangeBlock = pygame.image.load("Assets/OrangeBlock.png").convert()
PurpleBlock = pygame.image.load("Assets/PurpleBlock.png").convert()
RedBlock = pygame.image.load("Assets/RedBlock.png").convert()
YellowBlock = pygame.image.load("Assets/YellowBlock.png").convert()
EmptyBlock = pygame.Surface((25, 25))
EmptyBlock.set_alpha(0)


AllPieces = []
HoldingPieces = []
NextPieces = []

MovingPieces = []

SetupNodes()

moving = False
Direction = None

MoveTimer = 0
TickTimer = 0
speed = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving = True
                Direction = "Right"
            if event.key == pygame.K_a:
                moving = True
                Direction = "Left"
            if event.key == pygame.K_s:
                speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                if Direction == "Right":
                    moving = False
                    MoveTimer = 0
            if event.key == pygame.K_a:
                if Direction == "Left":
                    moving = False
                    MoveTimer = 0
            if event.key == pygame.K_s:
                speed = 30

    if moving:
        MoveTimer += 1

    if MoveTimer == 5:
        for movingB in AllPieces:
            if movingB.ismoving:
                MovingPieces.append(movingB)
        MovingPieces = copy.deepcopy(MovingPieces)

        if MoveCheck(MovingPieces):
            for movingB in AllPieces:
                if movingB.ismoving:
                    movingB.state = "Empty"
                    movingB.ismoving = False
            for movingB in AllPieces:
                if Direction == "Right":
                    for mover in MovingPieces:
                        if movingB.pos[1] == mover.pos[1]:
                            if movingB.pos[0] == mover.pos[0] + 1:
                                movingB.state = mover.state
                                movingB.ismoving = True
                if Direction == "Left":
                    for mover in MovingPieces:
                        if movingB.pos[1] == mover.pos[1]:
                            if movingB.pos[0] == mover.pos[0] - 1:
                                movingB.state = mover.state
                                movingB.ismoving = True
        MovingPieces = []
        MoveTimer = 0
        Blocked = False

    if TickTimer >= speed:
        for movingB in AllPieces:
            if movingB.ismoving:
                MovingPieces.append(movingB)
        MovingPieces = copy.deepcopy(MovingPieces)
        if UpdateTick(MovingPieces):
            for movingB in AllPieces:
                if movingB.ismoving:
                    movingB.state = "Empty"
                    movingB.ismoving = False
            for movingB in AllPieces:
                for mover in MovingPieces:
                    if movingB.pos[0] == mover.pos[0]:
                        if movingB.pos[1] == mover.pos[1] + 1:
                            movingB.state = mover.state
                            movingB.ismoving = True
        else:
            for movingB in AllPieces:
                if movingB.ismoving:
                    movingB.ismoving = False
        MovingPieces = []
        TickTimer = 0

    for line in range(20):
        NumSolid = 0
        for thing in AllPieces:
            if thing.pos[1] == line:
                if thing.state != "Empty":
                    if not thing.ismoving:
                        NumSolid += 1
        if NumSolid == 10:
            for thing in AllPieces:
                if thing.pos[1] == line:
                    thing.state = "Empty"
            for thing in AllPieces:
                if thing.pos[1] < line:
                    MovingPieces.append(copy.deepcopy(thing))
            for thing in AllPieces:
                if thing.pos[1] < line:
                    thing.state = "Empty"
            for thing in MovingPieces:
                thing.pos[1] += 1
                for stuff in AllPieces:
                    if thing.pos == stuff.pos:
                        stuff.state = thing.state
        MovingPieces = []

    WeSpawn = True
    for thing in AllPieces:
        if thing.ismoving:
            WeSpawn = False

    if WeSpawn:
        num = random.randint(1, 7)
        spawncords = []
        dacolor = ""
        if num == 1:
            spawncords = PieceCords("Square")
            dacolor = "Yellow"
        elif num == 2:
            spawncords = PieceCords("L")
            dacolor = "Orange"
        elif num == 3:
            spawncords = PieceCords("LR")
            dacolor = "Blue"
        elif num == 4:
            spawncords = PieceCords("Line")
            dacolor = "LightBlue"
        elif num == 5:
            spawncords = PieceCords("T")
            dacolor = "Purple"
        elif num == 6:
            spawncords = PieceCords("Z")
            dacolor = "Red"
        elif num == 7:
            spawncords = PieceCords("ZR")
            dacolor = "Green"

        for cords in spawncords:
            for thing in AllPieces:
                if cords == thing.pos:
                    thing.state = dacolor
                    thing.ismoving = True

    screen.blit(Background, (0, 0))

    UpdateColorNodes(HoldingPieces, "Hold")
    UpdateColorNodes(NextPieces, "Next")
    UpdateColorNodes(AllPieces, "All")

    pygame.display.update()
    TickTimer += 1
    clock.tick(60)
