import random
import pygame
from pygame.locals import *
from configuracion import *
from principal import *

def dameLetraApretada(key):
    if K_0 <= key and key <= K_9:
        return str(key - K_0)
    else:
        return ""


def dibujar(screen, productos_en_pantalla, producto_principal, producto_candidato, puntos, segundos):

    fuenteHelvetica= pygame.font.SysFont( "Helvetica", TAMANNO_LETRA)
    fuenteHelveticaGrande= pygame.font.SysFont( "Helvetica", TAMANNO_LETRA_GRANDE)
    FuenteHelveticaDetalles = pygame.font.SysFont("Helvetica",TAMANNO_LETRA_PTOS_TIME)
    FuenteHelveticaCandidato = pygame.font.SysFont("Helvetica",TAMANNO_LETRA_CANDIDATO)

    # Linea del piso
    pygame.draw.line(screen, (255, 255, 255),(0, ALTO-70), (ANCHO, ALTO-70), 20)
    ren1 = FuenteHelveticaCandidato.render(producto_candidato, 1, COLOR_NEGRO)
    ren2 = FuenteHelveticaDetalles.render("PUNTOS: " + str(puntos), 1, COLOR_NEGRO)
    if (segundos < 15):
        ren3 = FuenteHelveticaDetalles.render("TIEMPO: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = FuenteHelveticaDetalles.render("TIEMPO: " + str(int(segundos)), 1, COLOR_NEGRO)

   # Dibujar los nombres de los productos uno debajo del otro

    x_pos = 150
    y_pos = ALTO - (ALTO-180)

    pos = 0
    for producto in productos_en_pantalla:
        nombre_en_pantalla = str(pos) + " - "+producto[0]+producto[1]
        if producto[0] == producto_principal[0] and producto[1]== producto_principal[1]:
            screen.blit(fuenteHelvetica.render(nombre_en_pantalla, 1, COLOR_PRINCIPAL), (x_pos, y_pos))
        else:
            screen.blit(fuenteHelvetica.render(nombre_en_pantalla, 1, COLOR_NEGRO), (x_pos, y_pos))

        pos += 1
        y_pos += ESPACIO

    screen.blit(ren1, (400, 615))
    screen.blit(ren2, (750, 10))
    screen.blit(ren3, (10, 10))
