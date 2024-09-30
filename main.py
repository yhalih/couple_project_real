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
