import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Default")
clock = pygame.time.Clock()

n = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                n = "Left"
            if event.key == pygame.K_d:
                n = "Right"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                n = ""
            if event.key == pygame.K_d:
                n = ""

    if n == "Left":
        print("Left")
    elif n == "Right":
        print("Right")
    pygame.display.update()
    clock.tick(60)
