import pygame
from config import ANCHO

class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 5
        self.mirando_derecha = True

        self.frames = [
            pygame.image.load("assets/Walk (1).png").convert_alpha(),
            pygame.image.load("assets/Walk (2).png").convert_alpha(),
            pygame.image.load("assets/Walk (3).png").convert_alpha(),
            pygame.image.load("assets/Walk (4).png").convert_alpha(),
            pygame.image.load("assets/Walk (5).png").convert_alpha(),
            pygame.image.load("assets/Walk (6).png").convert_alpha(),
        ]

        self.frames = [pygame.transform.scale(img, (80, 100)) for img in self.frames]

        self.frame_actual = 0
        self.contador_anim = 0

    def mover(self, teclas):
        if teclas[pygame.K_RIGHT]:
            self.x += self.vel
            self.mirando_derecha = True
            self.animar()
        elif teclas[pygame.K_LEFT]:
            self.x -= self.vel
            self.mirando_derecha = False
            self.animar()

        if self.x > ANCHO:
            self.x = -80
        elif self.x < -80:
            self.x = ANCHO

    def animar(self):
        self.contador_anim += 1
        if self.contador_anim >= 8:
            self.frame_actual = (self.frame_actual + 1) % len(self.frames)
            self.contador_anim = 0

    def dibujar(self, pantalla):
        imagen = self.frames[self.frame_actual]
        if not self.mirando_derecha:
            imagen = pygame.transform.flip(imagen, True, False)
        pantalla.blit(imagen, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 80, 100)