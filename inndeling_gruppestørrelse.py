import random

størrelse_per_gruppe = 5

with open('elever.txt', 'r', encoding='utf-8') as file:
  tekst = file.read()
  elever = tekst.split('\n')
  random.shuffle(elever)
  antall_grupper = len(elever)//størrelse_per_gruppe
  rest = len(elever)%størrelse_per_gruppe
  print(antall_grupper, rest)
  grupper = [[] for _ in range(antall_grupper)]
  for i in range(antall_grupper):
    for j in range(størrelse_per_gruppe):
      grupper[i].append(elever.pop())
  if rest:
    for i in range(rest):
      grupper[i % antall_grupper].append(elever.pop())
  
  print(grupper)