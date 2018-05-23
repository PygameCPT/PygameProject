import pygame

pygame.init()

game_running = True

while game_running == True:
    # Event Logic Loop
    for event in pygame.event.get():
        if event == pygame.QUIT():
            pygame.quit()
            QUIT()