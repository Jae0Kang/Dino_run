#from operator import truediv
import pygame

pygame.init()

#screen_size_display = (width_screen, height_screen) = (600, 150)
width_screen = 600
height_screen = 150

<<<<<<< HEAD
display_surface = pygame.display.set_mode((width_screen, height_screen))    #display
pygame.display.set_caption("Dino run")                                      #window 

WHITE = (255,255,255)
BLACK = (0,0,0)
=======
display_surface = pygame.display.set_mode(
    (width_screen, height_screen))  # display
pygame.display.set_caption("Dino run")  # window
>>>>>>> Yoo

WHITE = (255, 255, 253)
BLACK = (0, 0, 0)

display_surface.fill(WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()


pygame.quit()
