#==============================#
# INPUTS
#==============================#

import random

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