"""
# Inndeler

Tar `elever.txt` eller en annen tekst fil, samt `antall_grupper` eller `gruppestørrelse`
og lager tilfeldige grupper etter parameterne som blir gitt 

## lagring

Inndeleren kan også lagre de gruppene som den har laget i en egen tekstfil

Laget av Morten, med logikk fra alle
"""

import random
import os

class Inndeler:
  def __init__(self, antall_grupper = None, gruppestørrelse = 2, fil_navn='elever.txt') -> None:
    """
    Definerer Inndeler klassen, med enten antall_grupper eller gruppestørrelse, samt en valgfritt fil navn
    """
    self.elever = self.hent_elever(fil_navn) #alle elevene i en vanlig array

    #deler etter antall grupper eller gruppestørrelse, ettersom hva som blir gitt under __init__
    #elev_liste er en 2 dimensjonal array med grupper av alle elevene i klassen
    if antall_grupper:
      self.elev_liste = self.del_per_antall_grupper(antall_grupper)
    if gruppestørrelse:
      self.elev_liste = self.del_per_gruppestørrelse(gruppestørrelse)

  @staticmethod
  def hent_elever(fil_navn):
    """
    Henter alle elevene i en .txt-fil, og deler etter linjesjift så elever kan ha mellomrom i navnet
    """
    with open(fil_navn, 'r', encoding='utf-8') as fil:
      tekst = fil.read()          #leser tekstfilen
      elever = tekst.split('\n')  #deler etter linjeshift
      return elever
    
  def lagre_grupper(self, filnavn):
    """
    Lagrer elevlista (2d array) med grupper i en tekstfil, med valgri filnavn
    """
    with open(filnavn, '+w', encoding='utf-8') as fil:
      fil.write(str(self.elev_liste))

  def del_per_antall_grupper(self, antall_grupper: int) -> list[str]:
    """
    Deler opp alle elevene i antall grupper oppgitt
    """
    elever = self.elever[:]
    random.shuffle(elever)
    antall_elever = len(elever) #tilfeldig rekkefølge
    antall_per_gruppe = antall_elever // antall_grupper
    rest = antall_elever % antall_grupper #rest etter divisjon

    #2d array, hvor hver indre array er en gruppe
    grupper = [[] for _ in range(antall_grupper)]

    #tar alle elevene i gruppene
    for i in range(antall_grupper):
      for _ in range(antall_per_gruppe):
        grupper[i].append(elever.pop())
    #legger til resten av elevene som ikke gikk opp i heltallsdivisjonen
    if rest:
      for i in range(rest):
        grupper[i % antall_grupper].append(elever.pop())
    
    return grupper
  
  def del_per_gruppestørrelse(self, størrelse: int) -> list[str]:
    """
    Deler opp alle elevene i størrelsen på gruppene som er  oppgitt
    """
    elever = self.elever[:]
    random.shuffle(elever) #tilfeldig rekkefølge
    antall_grupper = len(elever) // størrelse
    rest = len(elever) % størrelse  #rest etter divisjon

    #2d array, hvor hver indre array er en gruppe
    grupper = [[] for _ in range(antall_grupper)]

    #tar alle elevene i gruppene
    for i in range(antall_grupper):
      for _ in range(størrelse):
        grupper[i].append(elever.pop())
    #legger til resten av elevene som ikke gikk opp i heltallsdivisjonen
    if rest:
      for i in range(rest):
        grupper[i % antall_grupper].append(elever.pop())
    
    return grupper

if __name__ == '__main__':
  """
  Debugging
  """
  print('hei')