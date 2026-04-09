#==============================#
# INPUTS
#==============================#

import random

#==============================#
# VARIABLES GLOBLES
#==============================#

TITULO = "Batallas RPG"
VERSION = "0.0.7"


STATS_BASE = {
    "vida": 100,
    "ataque": 10,
    "defensa": 10,
    "velocidad": 10
}

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
# CLASSES
#==============================#

class Raza:
  
  def __init__(self, nombre, vida_min, vida_max, ataque_min, ataque_max, defensa_min, defensa_max, velocidad_min, velocidad_max):
    self.nombre = nombre
    self._vida_min = vida_min
    self._vida_max = vida_max
    self._ataque_min = ataque_min
    self._ataque_max = ataque_max
    self._defensa_min = defensa_min
    self._defensa_max = defensa_max
    self._velocidad_min = velocidad_min
    self._velocidad_max = velocidad_max

  def __str__(self):
    return self.nombre

  def aplicar_bonus(self, personaje):
    bonus_vida = random.randint(self._vida_min, self._vida_max)
    bonus_ataque = random.randint(self._ataque_min, self._ataque_max)
    bonus_defensa = random.randint(self._defensa_min, self._defensa_max)
    bonus_velocidad = random.randint(self._velocidad_min, self._velocidad_max)

    personaje._vida_max += bonus_vida
    personaje._vida += bonus_vida
    personaje._ataque += bonus_ataque
    personaje._defensa += bonus_defensa
    personaje._velocidad += bonus_velocidad

  def habilidad_racial(self):
    pass

class Personaje:
  
  def __init__(self, nombre, raza):
    self.nombre = nombre
    self._nivel = 1
    self.raza = raza

    self._vida_max = STATS_BASE["vida"]
    self._vida = STATS_BASE["vida"]
    self._ataque = STATS_BASE["ataque"]
    self._defensa = STATS_BASE["defensa"]
    self._velocidad = STATS_BASE["velocidad"]

    self.raza.aplicar_bonus(self)

  def atacar(self, objetivo):
    pass
  
  def recibir_daño(self, daño):
    pass

  def esta_vivo(self):
    return self._vida > 0

  def subir_nivel(self):
    pass

  def mostrar_stats(self):
    print("\n====================")
    print(f"{self.nombre} ({self.raza})")
    print(f"Nivel: {self._nivel}")
    print(f"Vida: {self._vida}/{self._vida_max}")
    print(f"Ataque: {self._ataque}")
    print(f"Defensa: {self._defensa}")
    print(f"Velocidad: {self._velocidad}")
    print("====================\n")

def crear_enemigo():
  raza = random.choice(RAZAS)
  enemigo = Personaje("Enemigo", raza)

  print("\n¡Un enemigo aparece!")
  enemigo.mostrar_stats()

  return enemigo

class Humano(Raza):

  def __init__(self):
    super().__init__(
      "Humano",
      5, 10,   # vida
      3, 6,    # ataque
      3, 6,    # defensa
      3, 6     # velocidad
    )

  def habilidad_racial(self):
    pass

class Elfo(Raza):

  def __init__(self):
    super().__init__(
      "Elfo",
      0, 5,    # vida
      4, 7,    # ataque
      1, 4,    # defensa
      6, 10    # velocidad
    )

  def habilidad_racial(self):
    pass

class Enano(Raza):

  def __init__(self):
    super().__init__(
      "Enano",
      10, 20,   # vida
      3, 6,     # ataque
      6, 10,    # defensa
      0, 3      # velocidad
    )

  def habilidad_racial(self):
    pass

class Orco(Raza):

  def __init__(self):
    super().__init__(
      "Orco",
      8, 15,   # vida
      7, 12,   # ataque
      1, 4,    # defensa
      2, 5     # velocidad
    )

  def habilidad_racial(self):
    pass

#==============================#
# CONFIGURACIÓN DEL SISTEMA
#==============================#

RAZAS = [Humano(), Elfo(), Enano(), Orco()]

MENU = []

for indice, raza in enumerate (RAZAS, 1):
  texto = f"{indice}. {raza.nombre}"
  MENU.append(texto)

MENU_INTERACTIVO = "\n".join(MENU)

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