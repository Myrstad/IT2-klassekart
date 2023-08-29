import random

class Inndeler:
  def __init__(self, antall_grupper = None, gruppestørrelse = 2, fil_navm='elever.txt') -> None:
    self.elever = self.hent_elever(fil_navm)
    if antall_grupper:
      self.elev_liste = self.del_per_antall_grupper(antall_grupper)
    if gruppestørrelse:
      self.elev_liste = self.del_per_gruppestørrelse(gruppestørrelse)
    print(self.elev_liste)
    print(self.elever)

  @staticmethod
  def hent_elever(fil_navn):
    with open(fil_navn, 'r', encoding='utf-8') as fil:
      tekst = fil.read()
      elever = tekst.split('\n')
      random.shuffle(elever)
      return elever

  def del_per_antall_grupper(self, antall_grupper: int) -> list[str]:
    elever = self.elever[:]
    antall_elever = len(elever)
    antall_per_gruppe = antall_elever // antall_grupper
    rest = antall_elever % antall_grupper

    grupper = [[] for _ in range(antall_grupper)]

    for i in range(antall_grupper):
      for j in range(antall_per_gruppe):
        grupper[i].append(elever.pop())
    if rest:
      for i in range(rest):
        grupper[i % antall_grupper].append(elever.pop())
    
    return grupper
  
  def del_per_gruppestørrelse(self, størrelse: int) -> list[str]:
    elever = self.elever[:]
    antall_grupper = len(elever) // størrelse
    rest = len(elever) // størrelse

    grupper = [[] for _ in range(antall_grupper)]

    for i in range(antall_grupper):
      for j in range(størrelse):
        grupper[i].append(elever.pop())
    if rest:
      for i in range(rest):
        grupper[i % antall_grupper].append(elever.pop())
    
    return grupper
  
if __name__ == '__main__':
  i = Inndeler(None, 2)

