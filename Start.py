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
    HoldingPieces.reverse()

    for y in range(4):
        for x in range(4):
            NextPieces.append(Piece([x, y], "Empty"))
    NextPieces.reverse()


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
            if node.state == "Gray":
                screen.blit(GrayBlock, (125 + (node.pos[0] * 25), 0 + (node.pos[1] * 25)))
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
            if node.state == "Gray":
                screen.blit(GrayBlock, (12 + (node.pos[0] * 25), 12 + (node.pos[1] * 25)))
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
            if node.state == "Gray":
                screen.blit(GrayBlock, (389 + (node.pos[0] * 25), 11 + (node.pos[1] * 25)))
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


def RotateCheck(allmoving):
    edge = False
    blocked = False

    themoving = copy.deepcopy(allmoving)

    if themoving[0].state == "Orange":
        if RotationState == 0:
            themoving[0].pos[0] += 1
            themoving[0].pos[1] -= 1

            themoving[3].pos[0] += 1
            themoving[3].pos[1] += 1
        if RotationState == 1:
            themoving[0].pos[0] += 1

            themoving[1].pos[0] -= 1
            themoving[1].pos[1] += 2
        if RotationState == 2:
            themoving[3].pos[1] += 1

            themoving[0].pos[0] -= 2
            themoving[0].pos[1] -= 1
        if RotationState == 3:
            themoving[2].pos[0] += 1
            themoving[2].pos[1] -= 1

            themoving[3].pos[0] -= 1
            themoving[3].pos[1] -= 1

    if themoving[0].state == "LightBlue":
        if RotationState == 0:
            themoving[0].pos[0] += 1
            themoving[0].pos[1] -= 1

            themoving[2].pos[0] -= 1
            themoving[2].pos[1] += 1

            themoving[3].pos[0] -= 2
            themoving[3].pos[1] += 2
        if RotationState == 1:
            themoving[0].pos[0] -= 2
            themoving[0].pos[1] += 1

            themoving[1].pos[0] -= 1
            themoving[1].pos[1] -= 1

            themoving[3].pos[0] += 1
            themoving[3].pos[1] -= 2
        if RotationState == 2:
            themoving[0].pos[0] -= 1
            themoving[0].pos[1] -= 2

            themoving[1].pos[0] += 1
            themoving[1].pos[1] -= 1

            themoving[3].pos[0] += 2
            themoving[3].pos[1] += 1
        if RotationState == 3:
            themoving[0].pos[0] -= 1
            themoving[0].pos[1] += 2

            themoving[2].pos[0] += 1
            themoving[2].pos[1] += 1

            themoving[3].pos[0] += 2
            themoving[3].pos[1] -= 1

    if themoving[0].state == "Blue":
        if RotationState == 0:
            themoving[2].pos[0] += 1
            themoving[2].pos[1] += 1

            themoving[3].pos[0] += 1
            themoving[3].pos[1] -= 1
        if RotationState == 1:
            themoving[0].pos[0] -= 1
            themoving[0].pos[1] -= 1

            themoving[1].pos[0] -= 1
            themoving[1].pos[1] += 1
        if RotationState == 2:
            themoving[0].pos[0] += 1
            themoving[0].pos[1] -= 1

            themoving[1].pos[0] -= 1
            themoving[1].pos[1] -= 1
        if RotationState == 3:
            themoving[2].pos[0] += 1
            themoving[2].pos[1] -= 1

            themoving[3].pos[0] += 1
            themoving[3].pos[1] += 1

    if themoving[0].state == "Purple":
        if RotationState == 0:
            themoving[3].pos[0] -= 1

            themoving[0].pos[0] -= 2
            themoving[0].pos[1] += 1
        if RotationState == 1:
            themoving[0].pos[0] -= 1
            themoving[0].pos[1] -= 2

            themoving[1].pos[1] -= 1
        if RotationState == 2:
            themoving[0].pos[0] += 1

            themoving[3].pos[0] += 2
            themoving[3].pos[1] -= 1
        if RotationState == 3:
            themoving[2].pos[1] += 1

            themoving[3].pos[0] += 1
            themoving[3].pos[1] += 2

    if themoving[0].state == "Red":
        if RotationState == 0:
            themoving[0].pos[0] += 2

            themoving[3].pos[1] += 2
        if RotationState == 1:
            themoving[3].pos[0] += 2

            themoving[2].pos[1] += 2
        if RotationState == 2:
            themoving[2].pos[0] += 2

            themoving[0].pos[1] -= 2
        if RotationState == 3:
            themoving[3].pos[0] += 2

            themoving[0].pos[1] -= 2

    if themoving[0].state == "Green":
        if RotationState == 0:
            themoving[2].pos[0] += 2

            themoving[3].pos[1] += 2
        if RotationState == 1:
            themoving[2].pos[0] -= 2

            themoving[3].pos[1] += 2
        if RotationState == 2:
            themoving[1].pos[0] -= 2

            themoving[0].pos[1] -= 2
        if RotationState == 3:
            themoving[1].pos[0] += 2

            themoving[0].pos[1] -= 2

    for stiff in themoving:
        if stiff.pos[0] < 0 or stiff.pos[0] > 9:
            edge = True
        if stiff.pos[1] < 0 or stiff.pos[1] > 19:
            edge = True

    if edge:
        blocked = True
    else:
        for place in themoving:
            for square in AllPieces:
                if square.pos == place.pos:
                    if not square.ismoving:
                        if square.state != "Empty":
                            blocked = True

    if not blocked:
        return True
    if blocked:
        return False


def PieceCords(name, placement):
    args = [0, 0]
    if placement == "Middle":
        args = [3, 1]
    if name == "Square":
        squarepos = [[1 + args[0], 1 - args[1]],
                     [1 + args[0], 2 - args[1]],
                     [2 + args[0], 1 - args[1]],
                     [2 + args[0], 2 - args[1]]]
        return squarepos
    if name == "L":
        lpos = [[1 + args[0], 1 - args[1]],
                [1 + args[0], 2 - args[1]],
                [1 + args[0], 3 - args[1]],
                [2 + args[0], 3 - args[1]]]
        return lpos
    if name == "LR":
        lrpos = [[2 + args[0], 1 - args[1]],
                 [2 + args[0], 2 - args[1]],
                 [2 + args[0], 3 - args[1]],
                 [1 + args[0], 3 - args[1]]]
        return lrpos
    if name == "Line":
        linepos = [[2 + args[0], 0],
                   [2 + args[0], 1],
                   [2 + args[0], 2],
                   [2 + args[0], 3]]
        return linepos
    if name == "T":
        tpos = [[2 + args[0], 1 - args[1]],
                [2 + args[0], 2 - args[1]],
                [1 + args[0], 2 - args[1]],
                [3 + args[0], 2 - args[1]]]
        return tpos
    if name == "Z":
        zpos = [[2 + args[0], 1 - args[1]],
                [2 + args[0], 2 - args[1]],
                [1 + args[0], 2 - args[1]],
                [1 + args[0], 3 - args[1]]]
        return zpos
    if name == "ZR":
        zrpos = [[1 + args[0], 1 - args[1]],
                 [1 + args[0], 2 - args[1]],
                 [2 + args[0], 2 - args[1]],
                 [2 + args[0], 3 - args[1]]]
        return zrpos


def RandomPieceCheck(danum, dacords, spawncolor, placement):
    if 1 <= danum <= 20:
        dacords = PieceCords("Square", placement)
        spawncolor = "Yellow"
    elif 21 <= danum <= 35:
        dacords = PieceCords("L", placement)
        spawncolor = "Orange"
    elif 36 <= danum <= 50:
        dacords = PieceCords("LR", placement)
        spawncolor = "Blue"
    elif 51 <= danum <= 70:
        dacords = PieceCords("Line", placement)
        spawncolor = "LightBlue"
    elif 71 <= danum <= 80:
        dacords = PieceCords("T", placement)
        spawncolor = "Purple"
    elif 81 <= danum <= 90:
        dacords = PieceCords("Z", placement)
        spawncolor = "Red"
    elif 91 <= danum <= 100:
        dacords = PieceCords("ZR", placement)
        spawncolor = "Green"
    return dacords, spawncolor


def HoldUpdate():
    for thinging in HoldingPieces:
        thinging.state = "Empty"

    for thinging in HoldingPieces:
        if -1 != (OriginPos[0] + thinging.pos[0]):
            if -2 != (OriginPos[0] + thinging.pos[0]):
                if 10 != (OriginPos[0] + thinging.pos[0]):
                    if 11 != (OriginPos[0] + thinging.pos[0]):
                        for some in AllPieces:
                            if some.ismoving:
                                if some.pos[0] == (OriginPos[0] + thinging.pos[0]):
                                    if some.pos[1] == (OriginPos[1] + thinging.pos[1]):
                                        thinging.state = some.state


Background = pygame.image.load("Assets/Bg.png").convert()
BlueBlock = pygame.image.load("Assets/BlueBlock.png").convert()
GreenBlock = pygame.image.load("Assets/GreenBlock.png").convert()
LightBlueBlock = pygame.image.load("Assets/LightBlueBlock.png").convert()
OrangeBlock = pygame.image.load("Assets/OrangeBlock.png").convert()
PurpleBlock = pygame.image.load("Assets/PurpleBlock.png").convert()
RedBlock = pygame.image.load("Assets/RedBlock.png").convert()
YellowBlock = pygame.image.load("Assets/YellowBlock.png").convert()
GrayBlock = pygame.image.load("Assets/GrayBlock.png").convert()
EmptyBlock = pygame.Surface((25, 25))
EmptyBlock.set_alpha(0)


AllPieces = []
HoldingPieces = []
NextPieces = []

MovingPieces = []

SetupNodes()

moving = False
Direction = None
Rotating = False

MoveTimer = 0
TickTimer = 0
speed = 30

RotationState = 0
NextSpawn = 0
HoldSpawn = 0
num = 0
spawncords = []
dacolor = ""

OriginPos = [3, 0]

HoldState = ""
isHolding = False
swapping = False
HoldLocked = False
HoldRotate = 0
VarRotate = 0

Lost = False

varHolding = []

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
                speed = 3
            if event.key == pygame.K_SPACE:
                Rotating = True
            if event.key == pygame.K_LSHIFT:
                if not HoldLocked:
                    VarRotate = HoldRotate
                    HoldRotate = RotationState
                    varHolding = copy.deepcopy(HoldingPieces)
                    HoldUpdate()
                    for thing in AllPieces:
                        if thing.ismoving:
                            HoldState = thing.state
                            thing.state = "Empty"
                            thing.ismoving = False
                    if isHolding:
                        OriginPos = [3, 0]
                        for thing in AllPieces:
                            for thinging in varHolding:
                                if (thinging.pos[0] + 3) == thing.pos[0]:
                                    if thinging.pos[1] == thing.pos[1]:
                                        thing.state = thinging.state
                                        if thinging.state != "Empty":
                                            thing.ismoving = True
                        RotationState = VarRotate
                    else:
                        HoldSpawn = num
                        isHolding = True
                    for thing in HoldingPieces:
                        if thing.state != "Empty":
                            HoldState = thing.state
                            thing.state = "Gray"
                    HoldLocked = True
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

    if Rotating:
        ColorPiece = None
        for movingB in AllPieces:
            if movingB.ismoving:
                MovingPieces.append(movingB)
        MovingPieces = copy.deepcopy(MovingPieces)

        if RotateCheck(MovingPieces):
            for movingB in AllPieces:
                if movingB.ismoving:
                    movingB.state = "Empty"
                    movingB.ismoving = False
            for moveplace in MovingPieces:
                ColorPiece = moveplace.state
            if ColorPiece == "Orange":
                if RotationState == 0:
                    MovingPieces[0].pos[0] += 1
                    MovingPieces[0].pos[1] -= 1

                    MovingPieces[3].pos[0] += 1
                    MovingPieces[3].pos[1] += 1
                if RotationState == 1:
                    MovingPieces[0].pos[0] += 1

                    MovingPieces[1].pos[0] -= 1
                    MovingPieces[1].pos[1] += 2
                if RotationState == 2:
                    MovingPieces[3].pos[1] += 1

                    MovingPieces[0].pos[0] -= 2
                    MovingPieces[0].pos[1] -= 1
                if RotationState == 3:
                    MovingPieces[2].pos[0] += 1
                    MovingPieces[2].pos[1] -= 1

                    MovingPieces[3].pos[0] -= 1
                    MovingPieces[3].pos[1] -= 1
            if ColorPiece == "LightBlue":
                if RotationState == 0:
                    MovingPieces[0].pos[0] += 1
                    MovingPieces[0].pos[1] -= 1

                    MovingPieces[2].pos[0] -= 1
                    MovingPieces[2].pos[1] += 1

                    MovingPieces[3].pos[0] -= 2
                    MovingPieces[3].pos[1] += 2
                if RotationState == 1:
                    MovingPieces[0].pos[0] -= 2
                    MovingPieces[0].pos[1] += 1

                    MovingPieces[1].pos[0] -= 1
                    MovingPieces[1].pos[1] -= 1

                    MovingPieces[3].pos[0] += 1
                    MovingPieces[3].pos[1] -= 2
                if RotationState == 2:
                    MovingPieces[0].pos[0] -= 1
                    MovingPieces[0].pos[1] -= 2

                    MovingPieces[1].pos[0] += 1
                    MovingPieces[1].pos[1] -= 1

                    MovingPieces[3].pos[0] += 2
                    MovingPieces[3].pos[1] += 1
                if RotationState == 3:
                    MovingPieces[0].pos[0] -= 1
                    MovingPieces[0].pos[1] += 2

                    MovingPieces[2].pos[0] += 1
                    MovingPieces[2].pos[1] += 1

                    MovingPieces[3].pos[0] += 2
                    MovingPieces[3].pos[1] -= 1
            if ColorPiece == "Blue":
                if RotationState == 0:
                    MovingPieces[2].pos[0] += 1
                    MovingPieces[2].pos[1] += 1

                    MovingPieces[3].pos[0] -= 1
                    MovingPieces[3].pos[1] += 1
                if RotationState == 1:
                    MovingPieces[0].pos[0] -= 1
                    MovingPieces[0].pos[1] -= 1

                    MovingPieces[1].pos[0] -= 1
                    MovingPieces[1].pos[1] += 1
                if RotationState == 2:
                    MovingPieces[0].pos[0] += 1
                    MovingPieces[0].pos[1] -= 1

                    MovingPieces[1].pos[0] -= 1
                    MovingPieces[1].pos[1] -= 1
                if RotationState == 3:
                    MovingPieces[2].pos[0] += 1
                    MovingPieces[2].pos[1] -= 1

                    MovingPieces[3].pos[0] += 1
                    MovingPieces[3].pos[1] += 1
            if ColorPiece == "Purple":
                if RotationState == 0:
                    MovingPieces[3].pos[0] -= 1

                    MovingPieces[0].pos[0] -= 2
                    MovingPieces[0].pos[1] += 1
                if RotationState == 1:
                    MovingPieces[0].pos[0] -= 1
                    MovingPieces[0].pos[1] -= 2

                    MovingPieces[1].pos[1] -= 1
                if RotationState == 2:
                    MovingPieces[0].pos[0] += 1

                    MovingPieces[3].pos[0] += 2
                    MovingPieces[3].pos[1] -= 1
                if RotationState == 3:
                    MovingPieces[2].pos[1] += 1

                    MovingPieces[3].pos[0] += 1
                    MovingPieces[3].pos[1] += 2
            if ColorPiece == "Red":
                if RotationState == 0:
                    MovingPieces[0].pos[0] += 2

                    MovingPieces[3].pos[1] += 2
                if RotationState == 1:
                    MovingPieces[0].pos[0] -= 2

                    MovingPieces[3].pos[1] += 2
                if RotationState == 2:
                    MovingPieces[3].pos[0] -= 2

                    MovingPieces[0].pos[1] -= 2
                if RotationState == 3:
                    MovingPieces[3].pos[0] += 2

                    MovingPieces[0].pos[1] -= 2
            if ColorPiece == "Green":
                if RotationState == 0:
                    MovingPieces[2].pos[0] += 2

                    MovingPieces[3].pos[1] += 2
                if RotationState == 1:
                    MovingPieces[2].pos[0] -= 2

                    MovingPieces[3].pos[1] += 2
                if RotationState == 2:
                    MovingPieces[1].pos[0] -= 2

                    MovingPieces[0].pos[1] -= 2
                if RotationState == 3:
                    MovingPieces[1].pos[0] += 2

                    MovingPieces[0].pos[1] -= 2
            for place in AllPieces:
                for position in MovingPieces:
                    if position.pos == place.pos:
                        place.state = position.state
                        place.ismoving = True
            if RotationState != 3:
                RotationState += 1
            else:
                RotationState = 0
        MovingPieces = []
        Rotating = False
        Blocked = False

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
            if Direction == "Right":
                OriginPos[0] += 1
            elif Direction == "Left":
                OriginPos[0] -= 1
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
            OriginPos[1] += 1
        else:
            for movingB in AllPieces:
                if movingB.ismoving:
                    movingB.ismoving = False
            for thing in HoldingPieces:
                if thing.state != "Empty":
                    thing.state = HoldState
            HoldLocked = False
            speed = 30

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

#   spawn check
    WeSpawn = True
    for thing in AllPieces:
        if thing.ismoving:
            WeSpawn = False

#   spawn
    if WeSpawn:
        OriginPos = [3, 0]
        RotationState = 0
        if NextSpawn != 0:
            num = NextSpawn
        else:
            num = random.randint(1, 100)
        NextSpawn = random.randint(1, 100)
        spawncords, dacolor = RandomPieceCheck(num, spawncords, dacolor, "Middle")
        spawnvar, varcolor = RandomPieceCheck(NextSpawn, spawncords, dacolor, "Middle")

        if varcolor == dacolor:
            NextSpawn += 30
            if NextSpawn > 100:
                NextSpawn = 100

        for cords in spawncords:
            for thing in AllPieces:
                if cords == thing.pos:
                    thing.state = dacolor
                    thing.ismoving = True

        if dacolor == "Purple":
            OriginPos[1] -= 1
        if dacolor == "Yellow":
            OriginPos[1] -= 1

    spawncords, dacolor = RandomPieceCheck(NextSpawn, spawncords, dacolor, "Next")

    for thing in NextPieces:
        thing.state = "Empty"
        for cords in spawncords:
            if cords == thing.pos:
                thing.state = dacolor

    spawncords = []
    dacolor = "Empty"

#   Lose Check
    for thing in AllPieces:
        if thing.pos[1] == 3:
            if not thing.ismoving:
                if thing.state != "Empty":
                    Lost = True

#   Lose
    if Lost:
        for thing in AllPieces:
            thing.state = "Empty"
            thing.ismoving = False
        HoldSpawn = 0
        Lost = False

    screen.blit(Background, (0, 0))

    UpdateColorNodes(HoldingPieces, "Hold")
    UpdateColorNodes(NextPieces, "Next")
    UpdateColorNodes(AllPieces, "All")

    pygame.display.update()
    TickTimer += 1
    clock.tick(60)
