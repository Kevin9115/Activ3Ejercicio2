tortuga = "🐢"
espacios = 0

def adelante(pasos_adelante):
    
    global espacios
    print (espacios * "  " + " _" * pasos_adelante)
    espacios = espacios + pasos_adelante
    
    
def abajo(pasos_abajo):
    
    for i in range(pasos_abajo-1):
        camino_abajo = "  " * espacios + "|\n"
        print(camino_abajo, end='')
    print("  " * espacios + tortuga)

def reiniciar():
    global espacios
    espacios = 0
    print("\n--- CAMINO REINICIADO ---")
    print("El siguiente camino comenzará desde la posición horizontal 0.")