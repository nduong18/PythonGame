import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, FPS

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    pygame.display.flip()
    
    clock.tick(FPS)

pygame.quit()

# Run code in terminal
# & "C:\Users\tt\AppData\Local\Programs\Python\Python313\python.exe" main.py
