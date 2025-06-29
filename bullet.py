import pygame

class Bullet:
    def __init__(self, x, y, direccion, imagen):
        self.velocidad = 10
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direccion = direccion

    def update(self):
        self.rect.x += self.velocidad * self.direccion

    def dibujar(self, ventana):
        ventana.blit(self.image, self.rect)