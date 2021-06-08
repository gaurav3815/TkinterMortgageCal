from tkinter import *
import tkinter as tk
import tkinter.font as font

window = tk.Tk()
window.title("Mortgage Calculator")
window.geometry("350x600")

Title = tk.Label(window,text="Calculate Mortgage", font=("Arial", 17), foreground="red").pack(padx=10, pady=10)

def show_entry_fields():
    DepositCal = int(Deposit.get())/100*int(HousePrice.get())
    DepositCalSet.set(DepositCal)
    MortgageCal = int(HousePrice.get())-int(DepositCal)
    print(MortgageCal)
    MortgageCalSet.set(MortgageCal)

    tk.Label(window, text="| Total Deposit |", font=("Arial", 12), foreground="red").pack()
    tk.Label(window, text="", textvariable=DepositCalSet, font=("Arial", 12)).pack()
    tk.Label(window, text="| Mortgage |", font=("Arial", 12), foreground="red").pack()
    tk.Label(window, text="", textvariable=MortgageCalSet, font=("Arial", 12)).pack()


DepositCalSet=StringVar()
MortgageCalSet=StringVar()

tk.Label(window, text="House Price (£)", font=("Arial", 12)).pack(padx=10, pady=10)
HousePrice = tk.Entry(window)
HousePrice.pack()

tk.Label(window, text="Deposit (%)", font=("Arial", 12)).pack(padx=10, pady=10)
Deposit = tk.Entry(window)
Deposit.pack()

tk.Button(window, text='Cal', command=show_entry_fields).pack(padx=10, pady=10)



window.mainloop()