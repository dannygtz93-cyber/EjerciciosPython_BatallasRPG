#==============================#
# INPUTS
#==============================#

from src.config.config import TITULO, VERSION
from src.config.razas import RAZAS, MENU_INTERACTIVO
from src.personajes.personajes import Personaje, crear_enemigo

#==============================#
# FUNCIONES DE INTERFAZ (UI)
#==============================#

def impr_titulo_version():
  print(f"{TITULO} v{VERSION}\n")

def impr_instrucciones():
  print(f"¡Bienvenido a las {TITULO}!\n\nPara comenzar elige una raza\n")

def seleccionar_raza():

  while True:

    try:

      print(MENU_INTERACTIVO)
      raza = int(input("\n¿Qué raza eliges?: "))

      if 1 <= raza <= len(RAZAS):
        raza_elegida = RAZAS[raza - 1]
        print(f"\nElegiste {raza_elegida}")
        return raza_elegida

      else:
        print(f"Ingresa un número entre 1 y {len(RAZAS)}\n")

    except ValueError:
      print(f"\nIngresa un número entre 1 y {len(RAZAS)}\n")

#==============================#
# ENTRY POINT
#==============================#

def main():

  impr_titulo_version()
  impr_instrucciones()

  raza = seleccionar_raza()
  jugador = Personaje("Jugador", raza)

  jugador.mostrar_stats()
  
  enemigo = crear_enemigo()

  input("\nPresiona Enter para salir...")

if __name__ == "__main__":
  main()