import pygame,sys,constantes
from personaje import Personaje

pygame.init();

jugador=Personaje(50,50)

#ventana
screen = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA));

#titulo e icono 
pygame.display.set_caption("Juego Kodland")
icono=pygame.image.load("assets/Soldado/Soldier-Guy-PNG/Arma de Fuego/01-Idle/E_E_Gun__Idle_001.png")
pygame.display.set_icon(icono)

#menu


#juego
fondo= pygame.image.load("assets/postapocalypse_bg_pixel_png/PNG/Postapocalypce4/Bright/postapocalypse4.png").convert()
screen.blit(fondo,(0,0))

#personaje
#caminaDerecha = [pygame.image.load()] 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()
    pygame.display.update()


    
