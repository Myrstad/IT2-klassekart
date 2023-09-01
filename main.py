import tkinter as tk
from tkinter import ttk
from klasser.inndeler import Inndeler
from klasser.kart import Kart
import re
import os

# Hovedvindu oppsett
window = tk.Tk()
window.title('Klassekart')
window.geometry('720x640')
klassekart = ttk.Frame(window)
innstillinger = ttk.Frame(window)

# Deklarer variabler på tvers av koden
forrige_lagret = []
valg, antall, antall_kolonner, elev_liste = None, None, None, None

# "Bytter plass" på elever dersom to ulike elever trykkes på etterhverandre
def bytt_elever(event):
  global forrige_lagret
  widget = event.widget
  forrige_lagret.append(widget)
  if len(forrige_lagret) > 1:
    if forrige_lagret[0] != widget: # Dersom det er 2 ulike elever
      navn1, navn2 = forrige_lagret[0].cget('text'), widget.cget('text') # Henter navnet på elevene
      forrige_lagret[0].configure(text=navn2)
      widget.configure(text=navn1)
    forrige_lagret = []

# Fjerner de visuelle elementene tilhørende klassekartet
def fjern_klassekart():
  for widget in klassekart.winfo_children():
    widget.destroy()
  klassekart.pack_forget()

# Lager menyen for innstillinger
def lag_instilliger():
  global valg
  global antall
  global antall_kolonner
  global elev_liste

  # Legger til knapper, tekstbokser e.l med standardverdier
  # Brukes til å sette variabler til programmet
  valg = tk.StringVar(innstillinger)
  valg.set('Antall per gruppe')
  options = ['Antall per gruppe', 'Antall grupper', 'Antall per gruppe']
  ttk.Label(innstillinger, text='Hvordan vil du dele klassen?').grid(column=0, row=0)
  ttk.OptionMenu(innstillinger, valg, *options).grid(column=1, row=0)
  ttk.Label(innstillinger, text="Antall:").grid(column=0, row=1)
  antall=ttk.Entry(innstillinger, width=10)
  antall.insert(0, '2')
  antall.grid(column=1, row=1)
  ttk.Label(innstillinger, text="Hvor mange kolonner:").grid(column=0, row=2)
  antall_kolonner=ttk.Entry(innstillinger, width=10)
  antall_kolonner.insert(0, '3')
  antall_kolonner.grid(column=1, row=2)
  innstillinger.pack()
  ttk.Label(innstillinger, text='Elevliste:').grid(row=3, column=0)


  # Henter elevliste fra lagret fil
  i = Inndeler(None, None)
  elev_liste = tk.Text(innstillinger)
  elev_liste.insert('end-1c', "\n".join(i.elever))
  elev_liste.grid(row=4, column=0, columnspan=2)

# Setter opp klassekartet visuelt
def tegn_klassekart():
  global valg
  global antall
  global antall_kolonner
  global elev_liste

  # Bytter fra innstillinger til kart
  innstillinger.pack_forget()
  fjern_klassekart()

  with open('elever.txt', '+w', encoding='utf-8') as fil:
    fil.write(elev_liste.get("1.0","end-1c"))

  # Deler inn etter antall grupper eller gruppe størrelse, samt lagrer resultat
  inndeler = None
  _antall = int(re.sub("\D", "", antall.get()))
  _antall_kolonner = int(re.sub("\D", "", antall_kolonner.get()))
  if valg.get() == 'Antall per gruppe':
    inndeler = Inndeler(None, _antall)
  else:
    inndeler = Inndeler(_antall, None)
  inndeler.lagre_grupper(os.path.join(os.getcwd(), 'data', 'program.txt'))
  
  # Henter opp inndeling som ble lagret i programmets indre formatering
  kart = Kart(kolonner=_antall_kolonner, fil_navn='program.txt')

  # Tegner kateter som referansepunkt
  ttk.Button(klassekart, text='Lærer (kateter)').grid(column=kart.kolonner//2, pady=10)

  # Tegner alle elevene på kartet
  for index, gruppe in enumerate(kart.grupper):
    kolonne = index % kart.kolonner
    rad = index // kart.kolonner + 1
    frame = ttk.Frame(klassekart)
    for person in gruppe:
      knapp = ttk.Button(frame, text=person)
      knapp.bind('<Button-1>', bytt_elever)
      knapp.bind('<Button-3>', lambda e: e.widget.configure(text=''))
      knapp.pack(side='left')
    frame.grid(row=rad, column=kolonne, padx=10, pady=5)
  klassekart.pack()

# Bytter visuelt til innstilinger og fjerner klassekartet
def bytt_til_innstillinger():
  fjern_klassekart()
  innstillinger.pack()

# Legger til meny-knappene
lag_klassekart = ttk.Button(window, text='Generer kart', command=tegn_klassekart)
slett_klassekart = ttk.Button(window, text='Innstillinger', command=bytt_til_innstillinger)
lag_klassekart.pack()
slett_klassekart.pack()

# Starter funksjonalitet ved oppstart
lag_instilliger()
window.mainloop()