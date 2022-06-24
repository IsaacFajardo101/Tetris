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
    for x in range(10):
        for y in range(20):
            AllPieces.append(Piece([x, y], "Empty"))

    for x in range(4):
        for y in range(4):
            HoldingPieces.append(Piece([x, y], "Empty"))

    for x in range(4):
        for y in range(4):
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
        if node.state == "RedBlock":
            node.surface = RedBlock
        if node.state == "YellowBlock":
            node.surface = YellowBlock
        if node.state == "Empty":
            node.surface.set_alpha(0)


def UpdateTick(pi):
    if pi.pos[1] == 19:
        for pint in AllPieces:
            if pint.ismoving:
                pint.ismoving = False
        return

    NewPos = None
    for pin in AllPieces:
        if pin.pos == [pi.pos[0], pi.pos[1] + 1]:
            NewPos = pin

    if NewPos.state == "Empty":
        NewPos.pos[1] -= 1
        pi.pos[1] += 1
        return
    elif NewPos.ismoving:
        pi.pos[1] += 1
        return
    else:
        for pint in AllPieces:
            if pint.ismoving:
                pint.ismoving = False



def MoveTick():
    for ip in AllPieces:
        if ip.ismoving:
            for pin in AllPieces:
                if Direction == "Right":
                    if ip.pos[0] != 9:
                        if pin.pos == [ip.pos[0] + 1, ip.pos[1]]:
                            ip.pos[0] += 1
                            pin.pos[0] -= 1
                            return
                    else:
                        return
                elif Direction == "Left":
                    if ip.pos[0] != 0:
                        if pin.pos == [ip.pos[0] - 1, ip.pos[1]]:
                            ip.pos[0] -= 1
                            pin.pos[0] += 1
                            return
                    else:
                        return


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
                for place in AllPieces:
                    if place.pos == [0, 0]:
                        place.state = "Blue"
                        place.ismoving = True
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

    if TickTimer == 30:
        for pog in AllPieces:
            if pog.ismoving:
                UpdateTick(pog)
        TickTimer = 0

    screen.blit(Background, (0, 0))

    if moving:
        MoveTimer += 1

    if MoveTimer == 5:
        MoveTick()
        MoveTimer = 0

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
