# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer

def main():
    nombre = input("Nombre del archivo: ")
    archivo = open(nombre, "r")
    
    n = int(archivo.readline())
    timer = lap_timer.init(n)
    
    for linea in archivo:
        tiempo = float(linea)
        lap_timer.add_lap(timer, tiempo)
    
    archivo.close()
    
    racha = lap_timer.longest_decreasing_streak(timer)
    print(racha)

if __name__ == "__main__":
    main()
