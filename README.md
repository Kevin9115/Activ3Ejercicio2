# 📦 DESCRIPCION DEL PAQUETE
__
Mini_turtle_drawer es un paquete simple de Python diseñado para demostrar conceptos básicos de programación como el manejo de estado global (posicion_x), la modularización (__init__.py, drawer_logic.py) y el dibujo basado en texto usando una metáfora de "Tortuga".

El paquete permite dibujar caminos rectos (horizontales y verticales) en la terminal, donde la posición final de un movimiento afecta el inicio del siguiente, y la función reiniciar() permite volver al origen.

**El paquete expone tres funciones principales:**
* Adelante: Dibuja la línea horizontal y avanza la posición X.
* Abajo:	Dibuja la línea vertical y coloca la tortuga (🐢) al final.
* Reiniciar(): Resetea la posición horizontal (posicion_x) a cero (0).
___

# 🚀 EJEMPLO DE USO (main.py)
Para ver el paquete en acción, puedes ejecutar el script de prueba. Este script demuestra cómo la posición se acumula y cómo reiniciar() afecta el siguiente dibujo.
Para esto puedes abrir y copiar el codigo que hay en el archivo "main.py"
O puedes copiarlo desde aca:

````python

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

````

````python

adelante(5)
abajo(4)

adelante(5)
abajo(4)

adelante(5)
abajo(4)
````

````python
_ _ _ _ _
          |
          |
          |
          🐢
           _ _ _ _ _
                    |
                    |
                    |
                    🐢
                     _ _ _ _ _
                              |
                              |
                              |
                              🐢
````

````python
reiniciar() "Con esta instruccion se borra el proceso y se empieza desde cero."

````

````python

--- CAMINO REINICIADO ---

El siguiente camino comenzará desde la posición horizontal 0.

````

````python

adelante(5)
abajo(4)

adelante(5)
abajo(4)

````

````python

 _ _ _ _ _
          |
          |
          |
          🐢
           _ _ _ _ _
                    |
                    |
                    |
                    🐢

````
