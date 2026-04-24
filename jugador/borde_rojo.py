import pygame
from config import ROJO
from .decorator import JugadorDecorator

class BordeRojo(JugadorDecorator):
    def dibujar(self, pantalla):
        super().dibujar(pantalla)

        rect = self.get_rect()
        pygame.draw.circle(pantalla, ROJO, rect.center, rect.width//2, 4)