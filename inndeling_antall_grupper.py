import random

antall_grupper = 14

with open('elever.txt', 'r', encoding='utf-8') as file:
  tekst = file.read()
  elever = tekst.split('\n')
  antall_elever = len(elever)
  random.shuffle(elever)
  antall_per_gruppe = antall_elever // antall_grupper
  rest = antall_elever % antall_grupper
  
  grupper = [[] for _ in range(antall_grupper)]
  for i in range(antall_grupper):
    for j in range(antall_per_gruppe):
      grupper[i].append(elever.pop())
  if rest:
    for i in range(rest):
      grupper[i % antall_grupper].append(elever.pop())
  

  print(antall_grupper, antall_per_gruppe, rest)
  print(grupper)