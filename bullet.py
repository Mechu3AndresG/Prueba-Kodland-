import pygame, constantes

class Bullet:
    def __init__(self, x, y, direccion, imagen):
        self.velocidad = 10
        self.image = imagen
        self.forma=self.image.get_rect()
        self.forma.center = (x, y)
        self.direccion = direccion

    def update(self):
        self.forma.x += self.velocidad * self.direccion

    def dibujar(self, ventana):
        ventana.blit(self.image, self.forma)
        pygame.draw.rect(ventana, constantes.COLOR_PERSONAJE, self.forma, 1)