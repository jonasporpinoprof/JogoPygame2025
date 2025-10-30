import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()
largura = 640
altura = 480
x = largura/2
y = altura/2
relogio = pygame.time.Clock()
x_azul = randint(40,600)
y_azul =randint(50,430)
pontos = 0
fonte = pygame.font.SysFont('arial',40,True,True)
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo 🎮")
while True:
   relogio.tick(200)
   janela.fill((0,0,0))
   mensagem = f'Pontos: {pontos}'
   tex_form = fonte.render(mensagem, True, (255,255,255))
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           exit()  
   if pygame.key.get_pressed()[K_a]:
       x = x - 1
   if pygame.key.get_pressed()[K_d]:
       x = x + 1
   if pygame.key.get_pressed()[K_w]:
       y = y - 1
   if pygame.key.get_pressed()[K_s]:
       y = y + 1
   retangulo_vermelho = pygame.draw.rect(janela, (255,0,0),(x,y,40,50))
   retangulo_azul = pygame.draw.rect(janela,(0,0,255),(x_azul,y_azul,40,50))
   if retangulo_vermelho.colliderect(retangulo_azul):
       x_azul = randint(40,600)
       y_azul =randint(50,430)
       pontos = pontos +1
   janela.blit(tex_form, (450,40))
   pygame.display.update()
