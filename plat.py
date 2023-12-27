import pygame
from pygame.locals import *

pygame.init()   # INICJOWANIE PYGAME

screen_width = 1200     #WYSOKOŚĆ I SZEROKOŚĆ EKRANU
screen_height = 1200

screen = pygame.display.set_mode((screen_width, screen_height))      #ODPALANIE EKRANU      
pygame.display.set_caption("platformówka")      #TYTUŁ

slonce_img = pygame.image.load("")

run = True      #GŁOWNA PĘTLA ZAMYKANIA
while run == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()



