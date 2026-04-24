import pygame
from config import VERDE
from .decorator import JugadorDecorator

class BordeVerde(JugadorDecorator):
    def dibujar(self, pantalla):
        super().dibujar(pantalla)
        pygame.draw.rect(pantalla, VERDE, self.get_rect(), 4)