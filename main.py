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