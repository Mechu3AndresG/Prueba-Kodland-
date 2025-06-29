import pygame, constantes

class Personaje():
    def __init__(self, x, y, animacionesCaminar, animacionesDisparo, animacionesMuerte):
        self.flip = False
        self.disparo=False
        self.jugadorMuerto=False
        self.animaciones=animacionesCaminar
        self.animacionesDisparo = animacionesDisparo
        self.animacionesMuerte = animacionesMuerte
        #imagen de la animacion de que esta mostrando
        self.frame_index = 0
        self.vidaPersonaje = 80
        self.image = animacionesCaminar[self.frame_index]
        #actualiza el tiempo desde que se inicializo pygame
        self.update_time = pygame.time.get_ticks()
        self.forma = self.image.get_rect()
        self.forma.center = (x,y)
    
    def update(self, quieto):
        cooldown_animacion = 0
        if self.disparo and not self.jugadorMuerto:
            cooldown_animacion = 50
            self.image = self.animacionesDisparo[self.frame_index]   
        elif quieto and not self.jugadorMuerto:
            self.image = self.animaciones[0]
        elif self.jugadorMuerto:
            cooldown_animacion = 100
            self.image=self.animacionesMuerte[self.frame_index]
        else:
            cooldown_animacion = 100
            self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.disparo and self.frame_index >= len(self.animacionesDisparo):
            self.disparo = False
            self.frame_index = 0
        elif self.jugadorMuerto and self.frame_index >= len(self.animacionesMuerte):
            self.frame_index = len(self.animacionesMuerte) - 1
        elif not self.disparo and self.frame_index >= len(self.animaciones):
            self.frame_index = 0
    
    def shot(self, shoting):
        if shoting:
            self.disparo=True
            self.frame_index=0
            self.update_time=pygame.time.get_ticks()
                
    def muerteJ(self):
        self.jugadorMuerto=True
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()

    def dibujar(self, interfaz):
        imagen_flip= pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        

    def movimiento (self, deltaX):
        if deltaX < 0:
            self.flip=True
        if deltaX > 0:
            self.flip=False
        self.forma.x=self.forma.x + deltaX
