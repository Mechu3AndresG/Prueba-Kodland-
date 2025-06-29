import pygame,sys,constantes
from personaje import Personaje
from bullet import Bullet

pygame.init();

#ventana 
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA));
#titulo e icono 
pygame.display.set_caption("Juego Kodland")
icono=pygame.image.load("assets/Soldado/Soldier-Guy-PNG/Arma de Fuego/01-Idle/E_E_Gun__Idle_001.png")
pygame.display.set_icon(icono)

def escalarImg(image, scala):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image,(w*scala,
                                                    h*scala))
    return nueva_imagen 

#aparicion primera del jugador
imagenJugador = pygame.image.load("assets/Soldado/Soldier-Guy-PNG/Arma de Fuego/01-Idle/E_E_Gun__Idle_002.png")
imagenJugador=escalarImg(imagenJugador, constantes.SCALA_PERSONAJE)

#imagen bala
imagenBalas=pygame.image.load("assets/Soldado/Soldier-Guy-PNG/Balas/Bullet.png")
imagenBalas=escalarImg(imagenBalas,constantes.SCALA_BALA)
balas=[]


animacionesCaminar=[]
animacionesDisparo=[]
animacionesMuerte=[]
animacionesCaminar.append(imagenJugador)
for i in range (9):
    img = pygame.image.load(f"assets/Soldado/Soldier-Guy-PNG/Arma de Fuego/02-Run/E_E_Gun__Run_000_00{i}.png ")
    img = escalarImg(img, constantes.SCALA_PERSONAJE)
    
    imgShot = pygame.image.load(f"assets/Soldado/Soldier-Guy-PNG/Arma de Fuego/03-Shot/E_E_Gun__Attack_00{i}.png")
    imgShot = escalarImg(imgShot, constantes.SCALA_PERSONAJE)
    
    animacionesCaminar.append(img)
    animacionesDisparo.append(imgShot)

jugador=Personaje(508,450, animacionesCaminar, animacionesDisparo)



#menu


#juego
fondo = pygame.image.load("assets/postapocalypse_bg_pixel_png/PNG/Postapocalypce4/Bright/postapocalypse4.png").convert()
ventana.blit(fondo,(0,0))

#personaje control movimiento
caminaDerecha = False
caminarIzquierda = False

#disparar
dispara=False

#controlar frame rate
reloj = pygame.time.Clock()
while True:
    #60 fps
    reloj.tick(60)
    #actualizar fondo
    ventana.blit(fondo,(0,0))
    #inicializar pasos
    deltaX = 0
    
    #actualiza delta
    if caminaDerecha==True:
        deltaX=constantes.VELOCIDAD
    if caminarIzquierda==True:
        deltaX=-constantes.VELOCIDAD

     #mover Jugador
    jugador.movimiento(deltaX) 

    jugador.update()

    jugador.dibujar(ventana)

    #actualizar balas
    for bala in balas[:]:
        bala.update()
        bala.dibujar(ventana)
        if bala.rect.right < 0 or bala.rect.left > constantes.ANCHO_VENTANA:
            balas.remove(bala)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()
        #Calcular movimiento
        if event.type== pygame.KEYDOWN:
            #tecla abajo
            if event.key == pygame.K_a:
                caminarIzquierda=True
            if event.key == pygame.K_d:
                caminaDerecha=True
            #tecla disparo
            if event.key == pygame.K_f:
                dispara = True
                jugador.shot(dispara)
                #crea bala
                direccion = -1 if jugador.flip else 1
                offset = -30 if jugador.flip else 30
                x_bala = jugador.forma.centerx + offset
                y_bala = jugador.forma.centery
                balas.append(Bullet(x_bala, y_bala, direccion, imagenBalas))
        if event.type== pygame.KEYUP:
            #tecla arriba
            if event.key == pygame.K_a:
                caminarIzquierda=False
            if event.key == pygame.K_d:
                caminaDerecha=False
            
        
           
            
    pygame.display.update()
    



    
