import pygame
from settings import *
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Demo PyGame")
clock = pygame.time.Clock()
running = True

BACKGROUND_IMAGE = pygame.image.load(BG_IMAGE_PATH)
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

PLAYER_IMAGE = pygame.image.load(PLAYER_IMAGE_PATH)
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE,(PLAYER_WIDTH, PLAYER_HEIGHT))

player_x = SCREEN_WIDTH // 2
player_y = GROUND_Y - PLAYER_HEIGHT
player_vx = 0
player_vy = 0
on_ground = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_vx = 0
    if keys[pygame.K_LEFT]:
        player_vx = -PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_vx = PLAYER_SPEED
    if keys[pygame.K_SPACE] and on_ground:
        player_vy = PLAYER_JUMP_STRENGTH
        on_ground = False

    # áp dụng trọng lực
    player_vy += GRAVITY

    # cập nhật vị trí
    player_x += player_vx
    player_y += player_vy

    # va chạm với nền
    if player_y + PLAYER_HEIGHT >= GROUND_Y:
        player_y = GROUND_Y - PLAYER_HEIGHT
        player_vy = 0
        on_ground = True

    # vẽ player
    screen.blit(BACKGROUND_IMAGE,(0,0))
    screen.blit(PLAYER_IMAGE, (player_x, player_y))

    # cập nhật màn hình
    pygame.display.update()

    # giới hạn FPS
    clock.tick(FPS)

pygame.quit()

# Run code in terminal
# & "C:\Users\tt\AppData\Local\Programs\Python\Python313\python.exe" main.py
