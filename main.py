#from operator import truediv
import pygame
import os
import random

pygame.init()
width_screen = 900
height_screen = 600


display_surface = pygame.display.set_mode((width_screen, height_screen))    #display 크기
time_clok = pygame.time.Clock()                                             #시간 측정
pygame.display.set_caption("Santa run")                                      #window 이름

WHITE = (255,255,255)
BLACK = (0,0,0)


player = pygame.image.load("Player.png")
player = pygame.transform.scale(player, (200, 150))
player_Rect = player.get_rect()

player_Rect.centerx = round(0)
player_Rect.centery = round(500)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if player_Rect.x > width_screen:
        player_Rect.x = 0 - player_Rect.width
    display_surface.fill(WHITE)
    player_Rect.x += 100
    display_surface.blit(player, player_Rect)        
    pygame.display.flip()
    time_clok.tick(3)

pygame.quit()


