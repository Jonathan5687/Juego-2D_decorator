import pygame
from config import *
from jugador.jugador import Jugador
from jugador.borde_rojo import BordeRojo
from jugador.borde_verde import BordeVerde

class GameManager:
    def __init__(self):
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Decorator")

        self.clock = pygame.time.Clock()

        self.jugador_base = Jugador(100, 250)
        self.jugador = self.jugador_base

        self.objeto_rojo = pygame.Rect(300, 280, 50, 50)
        self.objeto_verde = pygame.Rect(550, 280, 50, 50)

        self.tiene_rojo = False
        self.tiene_verde = False

        self.tiempo = 0
        self.duracion = 200

    def run(self):
        while True:
            self.pantalla.fill(BLANCO)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            teclas = pygame.key.get_pressed()
            self.jugador.mover(teclas)

            self.detectar_colisiones()
            self.actualizar_tiempo()

            self.jugador.dibujar(self.pantalla)
            pygame.draw.rect(self.pantalla, ROJO, self.objeto_rojo)
            pygame.draw.rect(self.pantalla, VERDE, self.objeto_verde)

            pygame.display.flip()
            self.clock.tick(FPS)

    def detectar_colisiones(self):
        if self.jugador.get_rect().colliderect(self.objeto_rojo) and not self.tiene_rojo:
            self.jugador = BordeRojo(self.jugador)
            self.tiene_rojo = True
            self.tiempo = self.duracion

        if self.jugador.get_rect().colliderect(self.objeto_verde) and not self.tiene_verde:
            self.jugador = BordeVerde(self.jugador)
            self.tiene_verde = True
            self.tiempo = self.duracion

    def actualizar_tiempo(self):
        if self.tiempo > 0:
            self.tiempo -= 1
        else:
            self.jugador = self.jugador_base
            self.tiene_rojo = False
            self.tiene_verde = False