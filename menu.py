import pygame
import sys

class Menu:
    def __init__(self, imagen_fondo):
        self.fondo = pygame.transform.scale(imagen_fondo, (1067, 550))

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
                if 99 < y < 196:
                     if 333 < x < 647:
                        return "jugando"  # Ir al juego
                elif 228 < y < 308:
                     if 308 < x < 672:
                        return "dificultad"  # Ir al menú de dificultad
                elif 337 < y < 415:
                    if 371 < x < 606:
                        pygame.quit()
                        sys.exit()
        return "menu"