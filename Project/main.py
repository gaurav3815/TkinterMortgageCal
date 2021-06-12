from tkinter import *
import tkinter as tk
from tkinter.ttk import *

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

    YearToMonth = int(YearNum.get()) * int(12)
    YearlyIntrest = float(InterestRate.get()) / int(100)
    MonthlyIntrest = float(YearlyIntrest) / int(12)
    BankIntrestCal1 = float(MonthlyIntrest)*(int(1) + float(MonthlyIntrest))**int(YearToMonth)
    BankIntrestCal2 = float(1 + MonthlyIntrest)**YearToMonth - 1
    BankIntrestCal3 = float(BankIntrestCal1 / BankIntrestCal2)
    BankIntrestCal4 = round(BankIntrestCal3 * MortgageCal, 2)
    BankIntrestCal4Set.set(BankIntrestCal4)

    TotalMortageRepay = round(float(BankIntrestCal4)*int(YearToMonth),2)
    TotalMortageRepaySet.set(TotalMortageRepay)

    TD = Label(window, text="| Total Deposit |", font=("Arial", 12), foreground="red")
    TD.pack(pady=5)
    TDA = Label(window, text="", textvariable=DepositCalSet, font=("Arial", 12))
    TDA.pack(pady=5)
    M = Label(window, text="| Mortgage with Interest |", font=("Arial", 12), foreground="red")
    M.pack(pady=5)
    MA = Label(window, text="", textvariable=TotalMortageRepaySet, font=("Arial", 12))
    MA.pack(pady=5)
    OM = Label(window, text="| Monthly Mortgage |", font=("Arial", 12), foreground="red")
    OM.pack(pady=5)
    OMA = Label(window, text="", textvariable=BankIntrestCal4Set, font=("Arial", 12))
    OMA.pack(pady=5)
    counter += 1
    if counter == 2:
        TD.destroy()
        TDA.destroy()
        M.destroy()
        MA.destroy()
        OM.destroy()
        OMA.destroy()
        counter -= int(1)
    else:
        pass

DepositCalSet = StringVar()
MortgageCalSet = StringVar()
counterCalSet = StringVar()
NumOfYearsCalSet = StringVar()
BankIntrestCal4Set = StringVar()
TotalMortageRepaySet = StringVar()

tk.Label(window, text="House Price (£)", font=("Arial", 12)).pack(padx=10, pady=10)
HousePrice = tk.Entry(window)
HousePrice.pack()

tk.Label(window, text="Deposit (%)", font=("Arial", 12)).pack(padx=10, pady=10)
Deposit = tk.Entry(window)
Deposit.pack()

tk.Label(window, text="Number of Years to PayBack", font=("Arial", 12)).pack(padx=10, pady=10)
YearNum = tk.Entry(window)
YearNum.pack()

tk.Label(window, text="Banks' Interest Rate (%)", font=("Arial", 12)).pack(padx=10, pady=10)
InterestRate = tk.Entry(window)
InterestRate.pack()

tk.Button(window, text='Cal', command=show_entry_fields).pack(padx=10, pady=10)



window.mainloop()