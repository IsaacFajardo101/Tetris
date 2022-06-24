import pygame
from sys import exit


class Piece:
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state
        self.ismoving = False
        self.surface = pygame.Surface((25, 25))


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


def UpdateColorNodes(NodeList):
    for node in NodeList:
        if node.state == "Blue":
            node.surface = BlueBlock
        if node.state == "Green":
            node.surface = GreenBlock
        if node.state == "LightBlue":
            node.surface = LightBlueBlock
        if node.state == "Orange":
            node.surface = OrangeBlock
        if node.state == "Purple":
            node.surface = PurpleBlock
        if node.state == "Red":
            node.surface = RedBlock
        if node.state == "Yellow":
            node.surface = YellowBlock
        if node.state == "Empty":
            node.surface.set_alpha(0)


def UpdateTick(pi):
    if pi.pos[1] == 19:
        for pint in AllPieces:
            if pint.ismoving:
                pint.ismoving = False
        return

    NewPos = Piece([pi.pos[0], pi.pos[1] + 1], "Empty")
    for pin in AllPieces:
        if pin.pos == [pi.pos[0], pi.pos[1] + 1]:
            NewPos = pin

    if NewPos.state == "Empty":
        for pin in AllPieces:
            if pin.pos == [pi.pos[0], pi.pos[1] + 1]:
                pin.pos[1] -= 1
        pi.pos[1] += 1
        return
    elif NewPos.ismoving:
        for pin in AllPieces:
            if pin.pos == [pi.pos[0], pi.pos[1] + 1]:
                pin.pos[1] -= 1
        pi.pos[1] += 1
        return
    else:
        for pint in AllPieces:
            if pint.ismoving:
                pint.ismoving = False


def MoveCheck(allmoving):
    edge = False
    blocked = False

    for thing in allmoving:
        if Direction == "Right":
            if thing.pos[0] == 9:
                edge = True
        if Direction == "Left":
            if thing.pos[0] == 0:
                edge = True

    if not edge:
        if Direction == "Right":
            for place in allmoving:
                place.pos[0] += 1
        if Direction == "Left":
            for place in allmoving:
                place.pos[0] -= 1

        for place in allmoving:
            for square in AllPieces:
                if square.pos == place.pos:
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
                     [5, 0],
                     [4, 1],
                     [5, 1]]
        return squarepos


Background = pygame.image.load("Assets/Bg.png").convert()
BlueBlock = pygame.image.load("Assets/BlueBlock.png").convert()
GreenBlock = pygame.image.load("Assets/GreenBlock.png").convert()
LightBlueBlock = pygame.image.load("Assets/LightBlueBlock.png").convert()
OrangeBlock = pygame.image.load("Assets/OrangeBlock.png").convert()
PurpleBlock = pygame.image.load("Assets/PurpleBlock.png").convert()
RedBlock = pygame.image.load("Assets/RedBlock.png").convert()
YellowBlock = pygame.image.load("Assets/YellowBlock.png").convert()


AllPieces = []
HoldingPieces = []
NextPieces = []

MovingPieces = []

SetupNodes()

moving = False
Direction = None

MoveTimer = 0
TickTimer = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                Unspawnable = False
                for cords in PieceCords("Square"):
                    for p in AllPieces:
                        if cords == p.pos:
                            if p.state != "Empty":
                                Unspawnable = True
                if not Unspawnable:
                    for cords in PieceCords("Square"):
                        for p in AllPieces:
                            if p.pos == cords:
                                p.state = "Yellow"
                                p.ismoving = True
            if event.key == pygame.K_d:
                moving = True
                Direction = "Right"
            if event.key == pygame.K_a:
                moving = True
                Direction = "Left"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                moving = False
                MoveTimer = 0

    if moving:
        MoveTimer += 1

    if MoveTimer == 5:
        for movingB in AllPieces:
            if movingB.ismoving:
                MovingPieces.append(movingB)
        if MoveCheck(MovingPieces):
            for movingB in AllPieces:
                if movingB.ismoving:
                    if Direction == "Right":
                        for p in AllPieces:
                            if p.pos[0] == movingB.pos[0] + 1:
                                p.pos[0] = movingB.pos[0]
                        movingB.pos[0] += 1
                    if Direction == "Left":
                        for p in AllPieces:
                            if p.pos[0] == movingB.pos[0] - 1:
                                p.pos[0] = movingB.pos[0]
                        movingB.pos[0] -= 1
        MovingPieces = []
        MoveTimer = 0
        Blocked = False

    if TickTimer == 30:
        for pog in AllPieces:
            if pog.ismoving:
                UpdateTick(pog)
        TickTimer = 0

    screen.blit(Background, (0, 0))

    UpdateColorNodes(HoldingPieces)
    UpdateColorNodes(NextPieces)
    UpdateColorNodes(AllPieces)

    for p in AllPieces:
        screen.blit(p.surface, (125 + (p.pos[0] * 25), 0 + (p.pos[1] * 25)))
    for p in HoldingPieces:
        screen.blit(p.surface, (12 + (p.pos[0] * 25), 12 + (p.pos[1] * 25)))
    for p in NextPieces:
        screen.blit(p.surface, (389 + (p.pos[0] * 25), 11 + (p.pos[1] * 25)))

    pygame.display.update()
    TickTimer += 1
    clock.tick(60)
