import pygame, constantes

class Zombie:
    def __init__(self, x, y, animacionesCaminarZ, direccion):
        self.flip = direccion == 1  # 0: izquierda, 1: derecha
        self.direccion = direccion
        self.velocidad = -2 if direccion == 1 else 2

        self.animaciones = animacionesCaminarZ
        self.frame_index = 0
        self.image = animacionesCaminarZ[self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.forma = self.image.get_rect()
        self.forma.center = (x, y)

    def update(self):
        cooldown_animacion = 100
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma, 1)

    def movimiento(self):
        self.forma.x += self.velocidad