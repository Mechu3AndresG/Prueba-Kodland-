# 🧟‍♂️ Kodland Zombie Shooter

¡Bienvenido a _Kodland Zombie Shooter_!  
Este es un juego hecho en Pygame donde te pones en los zapatos de un valiente soldado en medio del apocalipsis zombi. Tu misión es simple: sobrevivir el mayor tiempo posible y despachar a todos los zombis que se te crucen.

## 🎮 ¿Cómo se juega?

- **Moverse**: Usa `A` para moverte a la izquierda y `D` para ir a la derecha.
- **Disparar**: Presiona `F` para disparar. Cada disparo lanza una bala en la dirección en la que estás mirando.
- **Empujar zombis**: Si los zombis te tocan, se detienen para atacarte, pero tú puedes empujarlos caminando contra ellos.
- **Cuidado**: Si no los matás rápido, te atacan y te sacan vida.

## 🧟‍♀️ Sobre los zombis

- Aparecen aleatoriamente desde ambos lados de la pantalla.
- Caminan hacia ti y atacan cuando te alcanzan.
- Si les disparás varias veces, se mueren con una animación bien chévere.
- Cuando mueren, dejan de moverse, atacar y ser empujados.

## 🖼️ Gráficos y sonidos

- Todos los sprites están pixelados, estilo retro.
- El fondo del juego es post-apocalíptico, bien ambientado.
- Tiene efectos de sonido para los pasos, disparos y cuando los zombis mueren (¡suena brutal!).

## 🧪 Cosas por mejorar (pero ya funciona chévere)

- Menú principal con botones de **Jugar**, **Dificultad** y **Salir**.
- Botón de **Reiniciar partida** y otro para **Volver al Menú** (ya están en camino).
- Se podrían añadir power-ups, más tipos de enemigos o incluso un jefe.

## 📁 Estructura del proyecto

```bash
.
├── main.py              # archivo principal del juego
├── personaje.py         # lógica del jugador
├── zombie.py            # clase de los zombis
├── bullet.py            # clase de las balas
├── constantes.py        # variables globales (colores, tamaños, etc)
├── assets/              # carpeta con imágenes y sonidos
│   ├── Soldado/
│   ├── zombie/
│   └── sonidos/
└── README.md
```

## 🚀 Cómo correr el juego

1. Asegúrate de tener Python y Pygame instalados:

   ```bash
   pip install pygame
   ```

2. Ejecuta el juego con:
   ```bash
   python main.py
   ```

¡Y ya estás listo para matar zombis!
