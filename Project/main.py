from tkinter import *
import tkinter as tk
from tkinter.ttk import *

window = tk.Tk()
window.title("Mortgage Calculator")
window.geometry("350x900")

Title = tk.Label(window,text="Calculate Mortgage", font=("Arial", 17), foreground="red").pack(padx=10, pady=10)

counter = 0
counter3 = 0
counter4 = 0
counter5 = 0

def ShowBuyToRentYesCal():
    global counter4
    global ProfitsA
    global ProfitsB
    global MCF
    global YCF
    counter4 += 1
    if counter4 >= 2:
        ProfitsA.destroy()
        ProfitsB.destroy()
        MCF.destroy()
        YCF.destroy()
        counter4 -= int(1)
    else:
        pass
    ProfitsMonthly = int(TenantsRent.get()) - int(BankIntrestCal4)
    ProfitsMonthlySet.set(ProfitsMonthly)
    ProfitsYearly = int(ProfitsMonthly) * 12
    ProfitsYearlySet.set(ProfitsYearly)

    MCF = Label(window, text="| Monthly CashFlow (£) |", font=("Arial", 12), foreground="red")
    MCF.pack(pady=5)
    ProfitsA = Label(window, text="", textvariable=ProfitsMonthlySet, font=("Arial", 12))
    ProfitsA.pack(pady=5)
    YCF = Label(window, text="| Yearly CashFlow (£) |", font=("Arial", 12), foreground="red")
    YCF.pack(pady=5)
    ProfitsB = Label(window, text="", textvariable=ProfitsYearlySet, font=("Arial", 12))
    ProfitsB.pack(pady=5)

def ShowBuyToRentYes():
    global TenantsRent
    global counter3
    global counter5
    global BigMulli
    global TrnantsRentTitle
    global TenantsRent
    global CF
    global HSH
    counter3 += 1
    if counter3 >= 2:
        BigMulli.destroy()
        TrnantsRentTitle.destroy()
        TenantsRent.destroy()
        CF.destroy()
        counter3 -= int(1)
        if counter4 >= 1:
            ProfitsA.destroy()
            ProfitsB.destroy()
            MCF.destroy()
            YCF.destroy()
    else:
        pass
    
    BigMulli = Label(window, text="Big Mulli!", font=("Arial", 12), foreground="red")
    BigMulli.pack()
    TrnantsRentTitle = tk.Label(window, text="Tenants Rent", font=("Arial", 12))
    TrnantsRentTitle.pack(padx=10, pady=10)
    TenantsRent = tk.Entry(window)
    TenantsRent.pack()
    CF = tk.Button(window, text='Calculate CashFlow', command=ShowBuyToRentYesCal)
    CF.pack()
    print(TenantsRent.get())

def ShowBuyToRentNo():
    global counter5
    global HSH
    HSH = Label(window, text="Home Sweet Home!", font=("Arial", 12), foreground="red")
    HSH.pack()
    counter5 += 1
    if counter5 >= 2:
        HSH.destroy()
        counter5 -= 1
    if counter3 >= 1:
        BigMulli.destroy()
        TrnantsRentTitle.destroy()
        TenantsRent.destroy()
        CF.destroy()
        if counter4 >= 1:
            ProfitsA.destroy()
            ProfitsB.destroy()
            MCF.destroy()
            YCF.destroy()
    else:
        pass


counter2 = 0
def ShowBuyToRent():
    global counter2
    print(counter2)
    Title2 = tk.Label(window, text="Buy To Rent?", font=("Arial", 17), foreground="red")
    Title2.pack(padx=10, pady=10)
    YesButton = tk.Button(window, text='Yes', command=ShowBuyToRentYes)
    NoButton = tk.Button(window, text='No', command=ShowBuyToRentNo)
    YesButton.pack()
    NoButton.pack()
    counter2 += 1
    if counter2 >= 2:
        Title2.destroy()
        YesButton.destroy()
        NoButton.destroy()
        counter2 -= int(1)
    else:
        pass

def show_entry_fields():
    global counter
    global BankIntrestCal4
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
    if counter >= 2:
        TD.destroy()
        TDA.destroy()
        M.destroy()
        MA.destroy()
        OM.destroy()
        OMA.destroy()
        counter -= int(1)
    else:
        pass
    ShowBuyToRent()

DepositCalSet = StringVar()
MortgageCalSet = StringVar()
counterCalSet = StringVar()
NumOfYearsCalSet = StringVar()
BankIntrestCal4Set = StringVar()
TotalMortageRepaySet = StringVar()
ProfitsMonthlySet = StringVar()
ProfitsYearlySet = StringVar()

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