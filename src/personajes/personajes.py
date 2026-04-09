#==============================#
# INPUTS
#==============================#

import random
from src.config.razas import RAZAS
from src.config.config import STATS_BASE

#==============================#
# CLASSES Y FUNCIONES
#==============================#

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