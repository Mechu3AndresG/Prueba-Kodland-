import pygame, constantes, random

class Zombie:
    def __init__(self, x, y, animacionesCaminarZ,animacionesAtacar,animacionesMuerte, direccion):
        self.flip = direccion == 1  # 0: izquierda, 1: derecha
        self.direccion = direccion
        self.velocidad = -1.5 if direccion == 1 else 1.5
        self.detenido = False
        self.atacando=False
        self.muerto=False
        self.termino_muerte = False
        self.vida = 20
        self.animacionesMuerte=animacionesMuerte
        self.animacionesAtaque= animacionesAtacar
        self.animaciones = animacionesCaminarZ
        self.frame_index = 0
        self.image = animacionesCaminarZ[self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.forma = self.image.get_rect()
        self.forma.center = (x, y)
        
    def update(self):
    # Elegimos la animación según el estado
        if self.muerto and self.frame_index >= len(self.animacionesMuerte):
            self.termino_muerte = True 
            return
        if self.atacando and not self.muerto:
            cooldown_animacion = 50
            animacion_actual = self.animacionesAtaque
        elif self.muerto:
            cooldown_animacion = 100
            animacion_actual = self.animacionesMuerte
        elif self.muerto and self.atacando:
            cooldown_animacion = 50
            animacion_actual = self.animacionesMuerte
        else:
            cooldown_animacion = 100
            animacion_actual = self.animaciones
        # Si ya se salió del rango de la animación actual, reiniciar
        if self.frame_index >= len(animacion_actual):
            self.frame_index = 0
            if self.atacando:
                self.atacando = False 
            animacion_actual = self.animaciones  
        self.image = animacion_actual[self.frame_index]            
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()

    def ataque(self, atacking):
        if atacking and not self.muerto:
            self.atacando=True
            self.detenido=True
            self.frame_index=0
            self.update_time=pygame.time.get_ticks()
        elif self.muerto:
            self.muerte()

    def muerte(self):
        self.muerto=True
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma, 1)

    def movimiento(self):
        if not self.detenido and not self.muerto :
            self.forma.x += self.velocidad