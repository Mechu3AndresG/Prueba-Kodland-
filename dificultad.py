import pygame
import sys

class Dificultad:
    def __init__(self, imagen_fondo):
        self.fondo = pygame.transform.scale(imagen_fondo, (1067, 550))
        self.valor = 10  # valor por defecto

    def dibujar(self, ventana):
        ventana.blit(self.fondo, (0, 0))

    def manejar_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x,y)
                if 101 < y < 186 :
                    if 342< x < 489 :
                        self.valor = 10
                        return "menu"
                elif  221< y < 267:
                    if 324 < x < 656:
                        self.valor = 15
                        return "menu"
                elif 335 < y < 413:
                    if 312<x<624:
                        self.valor = 20
                        return "menu"
                if 312 < x < 670 and 446 < y < 530:
                    return "menu"
        return "dificultad"

    def get_dificultad(self):
        return self.valor