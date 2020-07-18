import pygame
import numpy as np
import time

pygame.init()

width,height = 1000,1000                              # ancho y largo en pixeles
screen = pygame.display.set_mode((height,width))

background = 25, 25 ,25                               # intensidad color
screen.fill(background)


nxC , nyC = 25 , 25                                   # numero de celdas en eje x y y
dimCw = width / nxC                                            # dimensiones de las celdas
dimHw = height/ nyC

# estructura de datos donde se contiene estados de las celdas
gameState = np.zeros((nxC,nyC))                       # se crea una matriz de ceros donde el valor 1 indica que la celda esta viva

# generar patron activando o dando valores a celdas
gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1




# ejecucion
while True:                                            # mostrar pantalla de forma indefinida

    newGameState = np.copy(gameState)                  # en cada iteracio se hace una copia del estado actual del juego, en esta copia se guarda n las actualizaciones
                                                       #de lo que va ocurriendo
    screen.fill(background)                            # volver a rellenar en cada iteracion a pesar de cambio de estado no super pone la informacion
    time.sleep(0.1)                                    # delay

                                                       # generar graficos que se van a dibujar
    for y in range(0,nxC):                             # se recorre en el eje x y y cda una de las celdas generadas
        for x in range(0,nyC):

            # encontrar celdas vecinas (ver reglas y condiciones)  tener en cuenta que estas son celdas o bueno una matriz game state
            # se usa estrategia toroidal o pacman con la division modulo como un counter que se reinicia al dividir en la cantidad de pixeles por eje
            n_height = gameState[( x - 1) % nxC, ( y - 1 ) %nyC] + \
                       gameState[( x    ) % nxC, ( y - 1 ) %nyC] + \
                       gameState[( x + 1) % nxC, ( y - 1 ) %nyC] + \
                       gameState[( x - 1) % nxC, ( y     ) %nyC] + \
                       gameState[( x + 1) % nxC, ( y     ) %nyC] + \
                       gameState[( x - 1) % nxC, ( y + 1 ) %nyC] + \
                       gameState[( x    ) % nxC, ( y + 1 ) %nyC] + \
                       gameState[( x + 1) % nxC, ( y + 1 ) %nyC]

            # regla 1 : una celula muerta con 3 vecinas vivas = revive

            if gameState[x,y] == 0 and n_height == 3 :
                newGameState[x,y] = 1

            # regla 2: si una celula viva est rodeada con menos de dos celulas vivas o s hay mas de 3 vivas = muere por soledad o sobrepoblacion

            elif gameState[x,y] == 1 and (n_height < 2 or n_height > 3):
                newGameState[x, y] = 0


            # grafico
            poligono = [((x    ) * dimCw , y       * dimHw ) ,                 # coordenadas de poligono a partir d emulptiplicacion de indices por ancho y alto
                        ((x + 1) * dimCw , y       * dimHw ) ,
                        ((x + 1) * dimCw , (y + 1) * dimHw ) ,
                        ((x    ) * dimCw , (y + 1) * dimHw ) ,]

            if newGameState[x,y] == 0 :             #dibujo de celda negra para estado 0 o muerto
                pygame.draw.polygon(screen , (128,128,128) , poligono,1)        # polygon(pantalla donde s edibuja,color, puntos que definen el poligono que se esta dibujando, grosor d elinea 1 pixel)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poligono, 0)       #color blanco y solido


    gameState = np.copy(newGameState)                    # actualizar estado actual del juego al estado en que se realizaron cambios
    pygame.display.flip()                                # actualizar fotogramas en cada iteracion


# https://www.youtube.com/watch?v=OWXD_wJxCKQ