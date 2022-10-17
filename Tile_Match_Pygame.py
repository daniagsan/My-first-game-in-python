#Match Tile Game here



# Ocultar todos las Cartas
def ocultar_todos_las_Cartas():
    for fila in Cartas:
        for Cartas in fila:
            Cartas.mostrar = False
            Cartas.descubierto = False