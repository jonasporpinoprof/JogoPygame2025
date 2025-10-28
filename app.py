import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo 🎮")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(janela, (255,0,0),(200,100,40,50))
   
    pygame.display.update()
