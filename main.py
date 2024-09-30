from pygame import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
green= (64,200,45)
screen = display.set_mode((800, 600))


running = True

while running:
    screen.fill(green)
    display.flip()
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# import pygame
#
# pygame.init()
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
#
# screen = pygame.display.set_mode((800, 600))
#
# pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#
# running = True
#
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# import consts
# from consts import *
# def creating_matrix():
#     main_matrix= []
#     cell = ""
#     for i in range (ROWS):
#         hori =[]
#         for j in range (COLUMNS):
#             hori.append(cell)
#         main_matrix.append(hori)
#     return main_matrix
#
# print(creating_matrix())
import time
import pygame, sys
pygame.init()

game_running = True

while game_running:

    # If user closes the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
            sys.exit()

    # Actions based on pressed key
    pressed = pygame.key.get_pressed()

    # Showing the secret screen
    if pressed[pygame.K_KP_ENTER]:
        # first show secret screen
        time.sleep(1)
        # now show regular screen

    elif pressed[pygame.K_LEFT]:
        pass
    elif pressed[pygame.K_RIGHT]:
        pass
    elif pressed[pygame.K_UP]:
        pass
    elif pressed[pygame.K_DOWN]:
        pass

    pygame.display.update()

# When the game is finished (player exploded or reached flag):

# put explosion where the soldier is
# put hurt soldier where the original soldier was
# print losing message onto screen
time.sleep(3)
pygame.quit()
sys.exit()
