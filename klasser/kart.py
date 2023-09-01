"""
# Kart

Brukes hovedsakelig til å hente gruppene fra inndeleren og lagre kolonne antall til senere bruk i programmet

Laget av Morten
"""

import os
import ast

class Kart():
  def __init__(self, kolonner, fil_navn) -> None:
    self.grupper = self.hent_grupper(fil_navn)
    self.kolonner = kolonner

  

  def formatter(self) -> str:
    """
    Skriver ut og returner plassene på en fin måte. 
    Ellers brukes den ikke til noe
    """
    grupper = self.grupper
    grupper = ['{:20s}'.format(" | ".join(x)) for x in grupper]
    for i, gruppe in enumerate(grupper):
      if (i+1) % self.kolonner == 0:
        grupper[i]= gruppe + '\n'
    print("".join(grupper))
    return "".join(grupper)

  # Henter angitt gruppe fra txt-fil og returnerer dataen
  def hent_grupper(self, filnavn) -> list[list[str]]:
    path = os.path.join(os.getcwd(), 'data', filnavn)
    with open(path, 'r', encoding='utf-8') as fil:
      data = fil.read()
      data = ast.literal_eval(data)
    return data

if __name__ == '__main__':
  k = Kart(kolonner=4, fil_navn='1er.txt')
  k.formatter()