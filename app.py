import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo 🎮")

while True:
    janela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_a]:
        x = x - 1
    if pygame.key.get_pressed()[K_d]:
        x = x + 1
    
    pygame.draw.rect(janela, (255,0,0),(x,y,40,40))
   
    pygame.display.update()
