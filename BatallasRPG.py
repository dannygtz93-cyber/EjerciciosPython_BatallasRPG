#==============================#
# INPUTS
#==============================#

import random

#==============================#
# VARIABLES GLOBLES
#==============================#

TITULO = "Batallas RPG"
VERSION = "0.0.2"

#==============================#
# FUNCIONES DE INTERFAZ (UI)
#==============================#

def impr_titulo_version():
  print(f"{TITULO} v{VERSION}\n")

#==============================#
# CLASSES
#==============================#

class Personaje:
  
  def __init__(self, nombre, nivel, vida, vida_max, ataque, defensa, velocidad, raza):
    self.nombre = nombre
    self._nivel = nivel
    self._vida = vida
    self._vida_max = vida_max
    self._ataque = ataque
    self._defensa = defensa
    self._velocidad = velocidad
    self.raza = raza

    self.raza.aplicar_bonus(self)

  def atacar(self, objetivo):
    pass
  
  def recibir_daño(self, daño):
    pass

  def esta_vivo(self):
    pass

  def subir_nivel(self):
    pass


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