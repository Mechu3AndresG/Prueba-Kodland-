import pygame,sys,constantes
from personaje import Personaje
from bullet import Bullet
from zombie import Zombie
import random

pygame.init()
pygame.mixer.init()

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


#imagenes zombie

imagenZombie =pygame.image.load("assets/zombie/Zombie 01/01-Idle/__Zombie01_Idle_000.png")
imagenZombie=escalarImg(imagenZombie, constantes.SCALA_ZOMBIE) 
animacionesCaminarZ=[]
animacionesCaminarZ.append(imagenZombie)


for i in range (7):
    imgZ = pygame.image.load(f"assets/zombie/Zombie 01/02-Walk/__Zombie01_Walk_00{i}.png")
    imgZ = escalarImg(imgZ, constantes.SCALA_ZOMBIE)
    animacionesCaminarZ.append(imgZ)

animacionesAtacar=[]
for i in range (11):
    imgAtack = pygame.image.load(f"assets/zombie/Zombie 01/03-Attack/__Zombie01_Attack_{i}.png")
    imgAtack = escalarImg(imgAtack, constantes.SCALA_ZOMBIE)
    animacionesAtacar.append(imgAtack)

animacionesMuerteZ=[]
for i in range(7):
    imgDie= pygame.image.load(f"assets/zombie/Zombie 01/05-Die/__Zombie01_Die_00{i}.png")
    imgDie= escalarImg(imgDie, constantes.SCALA_ZOMBIE)
    animacionesMuerteZ.append(imgDie)

sonido_muerteZ=pygame.mixer.Sound("assets/zombie/Zombie 01/05-Die/zombie-death-2-95167.mp3")

zombies = []
dificult = 10  # total de zombies que aparecerán
zombies_creados = 0
tiempo_ultimo_zombie = pygame.time.get_ticks()
zombie_intervalo = 1500  # milisegundos entre cada aparición

#menu


#juego
fondo = pygame.image.load("assets/postapocalypse_bg_pixel_png/PNG/Postapocalypce4/Bright/postapocalypse4.png").convert()
ventana.blit(fondo,(0,0))

#personaje control movimiento
caminaDerecha = False
caminarIzquierda = False
sonido_caminar = pygame.mixer.Sound("assets/Soldado/Soldier-Guy-PNG/Arma de Fuego/02-Run/stepstone_1.wav")
sonido_camina=False
#disparar
dispara=False
sonido_disparo = pygame.mixer.Sound("assets/Soldado/Soldier-Guy-PNG/Arma de Fuego/03-Shot/Futuristic Shotgun Single Shot.wav")




pygame.mixer.music.load("aftermath-59735.mp3")
pygame.mixer.music.play(-1)

#controlar frame rate
reloj = pygame.time.Clock()
while True:
    #60 fps
    reloj.tick(60)
    #actualizar fondo
    ventana.blit(fondo,(0,0))
    #inicializar pasos
    deltaX = 0
    no_camina=False
    #actualiza delta
    if caminaDerecha==True:
        deltaX=constantes.VELOCIDAD
    if caminarIzquierda==True:
        deltaX=-constantes.VELOCIDAD
    
    if not caminarIzquierda and not caminaDerecha:
        no_camina = True

     #mover Jugador
    jugador.movimiento(deltaX) 

    if (caminaDerecha or caminarIzquierda) and not sonido_camina:
        sonido_caminar.play(-1)
        sonido_camina = True
    elif not caminaDerecha and not caminarIzquierda and sonido_camina:
        sonido_caminar.stop()
        sonido_camina = False

    jugador.update(no_camina)
    jugador.dibujar(ventana)

    #actualizar balas
    for bala in balas[:]:
        bala.update()
        bala.dibujar(ventana)
        if bala.forma.right < 0 or bala.forma.left > constantes.ANCHO_VENTANA:
            balas.remove(bala)

    #spawn zombies 
    tiempo_actual = pygame.time.get_ticks()
    if zombies_creados < dificult and tiempo_actual - tiempo_ultimo_zombie >= zombie_intervalo:
        direccion = random.randint(0, 1)
        x = 1020 if direccion == 1 else 37
        zombies.append(Zombie(x, 450, animacionesCaminarZ, animacionesAtacar, animacionesMuerteZ, direccion))
        zombies_creados += 1
        tiempo_ultimo_zombie = tiempo_actual
    
    for zombie in zombies[:]:
        for bala in balas[:]:
            if bala.forma.colliderect(zombie.forma):
                zombie.vida -= 5
                if zombie.vida <= 0 and not zombie.muerto:
                    zombie.muerte()
                    sonido_muerteZ.play()
                    #zombies.remove(zombie)
                balas.remove(bala)      
                break
        if zombie.forma.colliderect(jugador.forma):
            if not zombie.atacando:
                zombie.ataque(True)
                zombie.detenido = True    
            # Detectar hacia dónde empuja el jugador
            if caminaDerecha:
                zombie.forma.x += 3  
            elif caminarIzquierda:
                zombie.forma.x -= 3  
        else:
            zombie.detenido = False 
        zombie.movimiento()
        zombie.update()
        zombie.dibujar(ventana)


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
                sonido_disparo.play()
                jugador.shot(dispara)
                #crea bala
                direccion = -1 if jugador.flip else 1
                offset = -30 if jugador.flip else 30
                x_bala = jugador.forma.centerx + offset
                y_bala = jugador.forma.centery + 20
                balas.append(Bullet(x_bala, y_bala, direccion, imagenBalas))
        
        if event.type== pygame.KEYUP:
            #tecla arriba
            if event.key == pygame.K_a:
                caminarIzquierda=False
            if event.key == pygame.K_d:
                caminaDerecha=False


    pygame.display.update()
    



    
