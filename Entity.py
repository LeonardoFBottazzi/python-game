import random
class Entity:
  def __init__(self, x, y, graphic, mossa):
    self.x = x
    self.y = y
    self.graphic = graphic
    self.mossa = mossa

  def attack(self, target):
    if self.mossa == 'Sasso' and target.mossa == 'Forbice':
      print('Hai vinto lo scontro')
    elif self.mossa == 'Sasso' and target.mossa == 'Carta':
      print('Hai perso lo scontro')
    elif self.mossa == 'Sasso' and target.mossa == 'Sasso':
      print('Rifare')
    elif self.mossa == 'Carta' and target.mossa == 'Sasso':
      print('Hai vinto lo scontro')
    elif self.mossa == 'Carta' and target.mossa == 'Forbice':
      print('Hai perso lo scontro')
    elif self.mossa == 'Carta' and target.mossa == 'Carta':
      print('Rifare')
    elif self.mossa == 'Forbice' and target.mossa == 'Carta':
      print('Hai vinto lo scontro')
    elif self.mossa == 'Forbice' and target.mossa == 'Sasso':
      print('Hai perso lo scontro')
    elif self.mossa == 'Forbice' and target.mossa == 'Forbice':
      print('Rifare')      

class Level:
  def __init__(self, w, h):
    self.w = w
    self.h = h
    self.entities = []

  def add_entities(self, entities):
    self.entities += entities  

  def draw(self):
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if e.x == x and e.y == y:
            print("[{}]".format(e.graphic), end = "")
            break
        else:
          print("[ ]", end = "")

      print()

lista = ['Sasso','Carta','Forbice']
mossa = input('Fai la tua mossa:\n1)Sasso\n2)Forbice\n3)Carta\n')

player = Entity(1, 3, "P", mossa)
mossa_mostro = random.choice(lista)
monster = Entity(3, 4, "M", mossa_mostro)
level = Level(10, 10)

Entity.attack(player, monster)

level.add_entities([player, monster])

level.draw()
