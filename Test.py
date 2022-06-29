import pygame
import copy
from sys import exit


class Stuff:
    def __init__(self, thing, move):
        self.thing = thing
        self.move = move


def thing(arg):
    x = copy.deepcopy(arg)

    print(id(arg))
    print(id(x))

    x[0][0] += 1
    for boing in x:
        print("Function Value " + str(boing))


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Default")
clock = pygame.time.Clock()

m = [[0, 0], [0, 1]]

thing(m)

for boings in m:
    print("Real Value " + str(boings))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)
