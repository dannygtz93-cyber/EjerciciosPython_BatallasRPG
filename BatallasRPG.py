#==============================#
# INPUTS
#==============================#



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
  
  def __init__(self, nombre, nivel, vida, vida_max, ataque, defensa):
    self.nombre = nombre
    self._nivel = nivel
    self._vida = vida
    self._vida_max = vida_max
    self._ataque = ataque
    self._defensa = defensa

  def atacar(self):
    pass
  
  def recibir_daño(self):
    pass

  def esta_vivo(self):
    pass

  def subir_nivel(self):
    pass