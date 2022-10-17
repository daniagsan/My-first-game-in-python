
import pygame
import sys
import math
import time
import random


pygame.init()
pygame.font.init()
pygame.mixer.init()

#variables
medida_Carta = 200
altura_boton = 30
nombre_imagen_oculta = "C:\\Users\\Braya\\Downloads\\imagen_oculta.png"
imagen_oculta = pygame.image.load(nombre_imagen_oculta)
segundos_mostrar_pieza = 2



class Carta:
    def __init__(self, fuente_imagen):
        self.mostrar = True
        self.descubierto = False
        
        self.fuente_imagen = fuente_imagen
        self.imagen_real = pygame.image.load(fuente_imagen)

Cartas = [
    [Carta("C:\\Users\\Braya\\Downloads\\pina.png"), Carta("C:\\Users\\Braya\\Downloads\\pina.png"),
     Carta("C:\\Users\\Braya\\Downloads\\Manzana.png"), Carta("C:\\Users\\Braya\\Downloads\\Manzana.png")],
    [Carta("C:\\Users\\Braya\\Downloads\\Queso.png"), Carta("C:\\Users\\Braya\\Downloads\\Queso.png"),
     Carta("C:\\Users\\Braya\\Downloads\\Naranja.png"), Carta("C:\\Users\\Braya\\Downloads\\Naranja.png")],
    [Carta("C:\\Users\\Braya\\Downloads\\platano.png"), Carta("C:\\Users\\Braya\\Downloads\\platano.png"),
     Carta("C:\\Users\\Braya\\Downloads\\Fresa.png"), Carta("C:\\Users\\Braya\\Downloads\\Fresa.png")],
    [Carta("C:\\Users\\Braya\\Downloads\\Cerezas.png"), Carta("C:\\Users\\Braya\\Downloads\\Cerezas.png"),
     Carta("C:\\Users\\Braya\\Downloads\\sandia.png"), Carta("C:\\Users\\Braya\\Downloads\\sandia.png")],
]

# Colores
color_gris = (206, 206, 206)
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)
color_verde = (0,128,0)



#soniditos de memorama
sonido_fondo = pygame.mixer.Sound("C:\\Users\\Braya\\Downloads\\mario-coin.mp3")
sonido_clic = pygame.mixer.Sound("C:\\Users\\Braya\\Downloads\\mario-coin.mp3")
sonido_exito = pygame.mixer.Sound("C:\\Users\\Braya\\Downloads\\mario-coin.mp3")
sonido_fracaso = pygame.mixer.Sound("C:\\Users\\Braya\\Downloads\\mario-coin.mp3")
sonido_voltear = pygame.mixer.Sound("C:\\Users\\Braya\\Downloads\\mario-coin.mp3")

#Tamaño de pantalla
anchura_pantalla = len(Cartas[0]) * medida_Carta
altura_pantalla = (len(Cartas) * medida_Carta) + altura_boton
anchura_boton = anchura_pantalla

#Fuente del boton
tamanio_fuente = 20
fuente = pygame.font.SysFont("Arial", tamanio_fuente)
xFuente = int((anchura_boton / 2) - (tamanio_fuente / 2))
yFuente = int(altura_pantalla - altura_boton)

#Boton rectangulo 
boton = pygame.Rect(0, altura_pantalla - altura_boton,
                    anchura_boton, altura_pantalla)


# Banderas

ultimos_segundos = None
puede_jugar = True  
juego_iniciado = False
x1 = None
y1 = None
x2 = None
y2 = None

# Ocultar todos las Cartas
def ocultar_todos_las_Cartas():
    for fila in Cartas:
        for Cartas in fila:
            Cartas.mostrar = False
            Cartas.descubierto = False