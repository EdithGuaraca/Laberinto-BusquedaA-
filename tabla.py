from BusquedaE import *
from BusquedaE1 import *
import pygame
import random
from reportlab.pdfgen import canvas
import itertools
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)

def export_to_pdf(data):
    print("Generando PDF...")
    c = canvas.Canvas("Datos.pdf", pagesize=A4)
    w, h = A4
    max_rows_per_page = 45
    # Margin.
    x_offset = 50
    y_offset = 50
    # Space between rows.
    padding = 15
    
    xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    c.drawString(50, h - 50, "Posciones de los obstáculos")
    c.drawString(50, h - 50, " ")
    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))    
        c.showPage()
    
    c.save()

def generarObtaculos(n):
    obstaculos = []
    for i in range(n - 3):
        obstaculos.append((random.randint(0, n - 2), random.randint(0, n - 2)))
    return obstaculos
    
def generarLaberinto(n, obstaculos):
    laberinto = []
    for i in range(n):
        laberinto.append([' ' for j in range(n)])

    for i in range(len(obstaculos)):
        x, y = obstaculos[i]
        laberinto[x][y] = '*'
    return laberinto

def imprimir(laberinto):
    for i in range(len(laberinto)):
        print(laberinto[i])

    


NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 0)
pygame.init()




dimensiones = [600, 600]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Tablero")

juego_terminado = False
x1 = y1 = 0
x2 = y2 = 0
k = 0
l = 0
x_s = random.randint(0,7)
x_f = random.randint(0,7)
inicio = (0, x_s)
final = (7, x_f)
x=random.randint(0,5)
y=random.randint(0,5)
obstaculos = [(x, 4),(2,6), (3, 2), (x, 2), (2, y), (5, 5),(4,4), (x, 5), (6, 6), (3, y), (4, 6), (5, y), (4, 5), (0, 3), (y, 0), (4, 0), (7, 0), (0, 7)]
print(obstaculos)
export_to_pdf(obstaculos)
laberinto = generarLaberinto(8, obstaculos)
imprimir(laberinto)
ruta1 = aEstrella(laberinto, inicio, final)
busqueda(laberinto, inicio, final)
ruta2 = devolverRuta()
ruta2.append(final)
juego_terminado = False

reloj = pygame.time.Clock()
ancho = int(dimensiones[0] / 8)
alto = int(dimensiones[1] / 8)
yi, xi = inicio
yf, xf = final
while juego_terminado is False:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True
    pantalla.fill(BLANCO)
    color = 0
    for i in range(0, dimensiones[0], ancho):
        for j in range(0, dimensiones[1], alto):
            if color % 2 == 0:
                pygame.draw.rect(pantalla, NEGRO, [i, j, ancho, alto], 0)
            else:
                pygame.draw.rect(pantalla, NEGRO, [i, j, ancho, alto], 0)
            color += 1
        color += 1

    for yo, xo in obstaculos:
        color = (0, 0, (random.randint(220, 220)))
        pygame.draw.rect(pantalla, color, [ xo * 75, yo * 75, ancho, alto], 0)
    pygame.draw.rect(pantalla, AMARILLO, [xi * 75, yi * 75, ancho, alto], 0)
    pygame.draw.rect(pantalla, AMARILLO, [xf * 75, yf * 75, ancho, alto], 0)   
    pygame.draw.rect(pantalla, BLANCO, [x2 * 75, y2 * 75, ancho, alto], 0)
        
    if(k < len(ruta1)):
        y1, x1 = ruta1[k]
        k += 1
    else:
        k = 0
    if(l < len(ruta2)):
        y2, x2 = ruta2[l]
        l += 1
    else:
        l = 0
    
    pygame.display.flip()    
    reloj.tick(5)

pygame.quit()
