class JugadorDecorator:
    def __init__(self, jugador):
        self.jugador = jugador

    def mover(self, teclas):
        self.jugador.mover(teclas)

    def dibujar(self, pantalla):
        self.jugador.dibujar(pantalla)

    def get_rect(self):
        return self.jugador.get_rect()