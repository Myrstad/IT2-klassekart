import tkinter as tk
from tkinter import ttk
from klasser.inndeler import Inndeler
from klasser.kart import Kart

window = tk.Tk()
window.title('Klassekart')
window.geometry('720x640')


kart = Kart(kolonner=3, fil_navn='2er-grupper.txt')
print(kart.grupper, kart.kolonner)

ttk.Button(window, text='Trond på tronen').grid(column=kart.kolonner//2, pady=10)

for index, gruppe in enumerate(kart.grupper):
  #print(index, index%kart.kolonner, gruppe)
  kolonne = index % kart.kolonner
  rad = index // kart.kolonner + 1
  frame = ttk.Frame()
  [ttk.Button(frame, text=person).pack(side='left') for person in gruppe]
  #ttk.Button(window, text=personer).grid(row=rad, column=kolonne)
  frame.grid(row=rad, column=kolonne, padx=10, pady=5)
  print(rad, kolonne)

# b = 0
# for r in range(6):
#    for c in range(6):
#       b = b + 1
#       ttk.Button(window, text = str(b)).grid(row = r,column = c, padx=10, pady=5)

window.mainloop()