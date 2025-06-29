import pygame, constantes

class Personaje():
    def __init__(self, x, y, animacionesCaminar, animacionesDisparo):
        self.flip = False
        self.disparo=False
        self.animaciones=animacionesCaminar
        self.animacionesDisparo = animacionesDisparo
        #imagen de la animacion de que esta mostrando
        self.frame_index = 0
        self.image = animacionesCaminar[self.frame_index]
        #actualiza el tiempo desde que se inicializo pygame
        self.update_time = pygame.time.get_ticks()
        self.forma = self.image.get_rect()
        self.forma.center = (x,y)
    
    def update(self):
        cooldown_animacion = 100
        if self.disparo:
            self.image = self.animacionesDisparo[self.frame_index]   
        else:
            self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.disparo and self.frame_index >= len(self.animacionesDisparo):
            self.disparo = False
            self.frame_index = 0
        elif not self.disparo and self.frame_index >= len(self.animaciones):
            self.frame_index = 0
    
    def shot(self, shoting):
        if shoting:
            self.disparo=True
            self.frame_index=0
            self.update_time=pygame.time.get_ticks()
                


    def dibujar(self, interfaz):
        imagen_flip= pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        pygame.draw.rect(interfaz,constantes.COLOR_PERSONAJE,self.forma,1)

    def movimiento (self, deltaX):
        if deltaX < 0:
            self.flip=True
        if deltaX > 0:
            self.flip=False
        self.forma.x=self.forma.x + deltaX
