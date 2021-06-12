from tkinter import *
import tkinter as tk
from tkinter.ttk import *

import time

window = tk.Tk()
window.title("Mortgage Calculator")
window.geometry("350x600")

Title = tk.Label(window,text="Calculate Mortgage", font=("Arial", 17), foreground="red").pack(padx=10, pady=10)

counter = 0
def show_entry_fields():
    global counter
    counterCalSet.set(counter)
    DepositCal = int(Deposit.get())/100*int(HousePrice.get())
    DepositCalSet.set(DepositCal)
    MortgageCal = int(HousePrice.get())-int(DepositCal)
    MortgageCalSet.set(MortgageCal)
    TD = Label(window, text="| Total Deposit |", font=("Arial", 12), foreground="red")
    TD.pack(pady=5)
    TDA = Label(window, text="", textvariable=DepositCalSet, font=("Arial", 12))
    TDA.pack(pady=5)
    M = Label(window, text="| Mortgage |", font=("Arial", 12), foreground="red")
    M.pack(pady=5)
    MA = Label(window, text="", textvariable=MortgageCalSet, font=("Arial", 12))
    MA.pack(pady=5)
    counter += 1
    if counter == 2:
        TD.destroy()
        TDA.destroy()
        M.destroy()
        MA.destroy()
        counter = int(0)
    else:
        pass

DepositCalSet=StringVar()
MortgageCalSet=StringVar()
counterCalSet=StringVar()

tk.Label(window, text="House Price (£)", font=("Arial", 12)).pack(padx=10, pady=10)
HousePrice = tk.Entry(window)
HousePrice.pack()

tk.Label(window, text="Deposit (%)", font=("Arial", 12)).pack(padx=10, pady=10)
Deposit = tk.Entry(window)
Deposit.pack()

tk.Button(window, text='Cal', command=show_entry_fields).pack(padx=10, pady=10)



window.mainloop()