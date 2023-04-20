import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed #subtrai ou diminiui o valor do retangulo(imagem) do eixo x(horizontal)
        if self.rect.x < -self.rect.width:
            obstacles.pop() #remove o obstaculo(retangulo) quando for menor que o tamanho da tela

    def draw(self, screen):
        screen.blit(self.image[self.type],(self.rect.x, self.rect.y)) #exibição dos parametros na tela, imagem e posição da imagem
