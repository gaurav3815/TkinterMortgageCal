AllResponses = ["yes", "yep", "YES", "yeah", "Yep", "Ya", "yh", "YH", "Yh", "no", "nope", "NO", "No", "NOPE", "na", "na bro", "na man"]
HousePrice = int(input("What is the price of the House = "))
while HousePrice < 0:
    print("Error house price cant be a negative value")
    HousePrice = int(input("What is the price of the House = "))
else:
    pass
if HousePrice == 0:
    print("No need to use this Calculator")
    exit()
elif HousePrice <= 20000 and (HousePrice >= 1):
    print("Sorry House doesnt seem real too cheap!")
    exit()
if HousePrice >= 1000000 and (HousePrice <= 100000000):
    RichOrNot = input("Are you sure your house is more than £1000000? = ")
    while RichOrNot not in AllResponses:
        print("Please respond with yes or no!")
        RichOrNot = input("Are you sure your house is more than £1000000? = ")
    else:
        if RichOrNot in AllResponses[9:17]:
            HousePrice = int(input("What is the price of the House = "))
            lives = 3
            while HousePrice >= 1000000:
                print("Enter value less than a million if thats the case!")
                HousePrice = int(input("What is the price of the House = "))
                lives = lives - 1
                if lives == 0:
                    print("You are going in a loop here!")
                    exit()

                else:
                    pass
            else:
                pass
elif HousePrice > 100000000:
    print("House is too Expensive")
    exit()
else:
    pass
DepositPercentage = int(input("What percentage is the deposit = "))
while DepositPercentage > 100 or (DepositPercentage <= 0):
    print("Impossible enter a smaller percentage or a Bigger percentage!")
    DepositPercentage = int(input("What percentage is the deposit = "))
else:
    if DepositPercentage == 100:
        print("You have no Mortgage!")
        rentingornot = str(input("Is your house on buy to let?"))
        while rentingornot not in AllResponses:
            print("Please respond with yes or no!")
            rentingornot = str(input("Is your house on buy to let? = "))
        else:
            if rentingornot in AllResponses[0:9]:
                rentingmoney = int(input("How much are tenants paying monthly = "))
                profitsyearly = rentingmoney * 12
                print("You will make a profit of ", profitsyearly, "every year")
            else:
                print("Well your Rich anyways so do what ever you want!")
                exit()
DepositCalculation = (DepositPercentage / 100 * HousePrice)
print("Your Deposit Amount is :", DepositCalculation)
TotalMortgage = HousePrice - DepositCalculation
print("Your Mortgage is :",(TotalMortgage))
YearsToPay = int(input("Number of years to pay back loan? = "))
while YearsToPay >100 or (YearsToPay <= 0):
    print("Error! enter years less than 100 and more than 0")
    YearsToPay = int(input("Number of years to pay back loan? = "))
else:
    pass
YearsTOMonth = 12 * YearsToPay
BankIntrest = float(input("What is the Banks Intrest Rate percentage = "))
while BankIntrest >= 100 or (BankIntrest <= 0):
    print("Please enter less than 100% and more than 0%")
    BankIntrest = float(input("What is the Banks Intrest Rate percentage = "))
else:
    pass
YearlyIntrest = BankIntrest / 100
MonthlyIntrest = YearlyIntrest / 12
intrestCal1 = MonthlyIntrest * (1 + MonthlyIntrest)**YearsTOMonth
intrestCal2 = (1 + MonthlyIntrest)**YearsTOMonth - 1
intrestCal3 = intrestCal1 / intrestCal2
intrestCal4 = round(intrestCal3 * TotalMortgage, 2)
print("Your Monthly Mortgage Payment : ", intrestCal4)
BuyToLet = str(input("Is your House on Buy to let? = "))
while BuyToLet not in AllResponses:
    print("Please respond yes or no")
    BuyToLet = str(input("Is your House on Buy to let? = "))
    pass
else:
    if BuyToLet in AllResponses[0:9]:
        RentIncome = int(input("How much are tenants giving you = "))
        profit = round(RentIncome - intrestCal4)
        print(RentIncome)
        print(intrestCal4)
        print(profit)
        YearlyProfit = profit * 12
        if RentIncome < intrestCal4:
            print("You are Making a Loss on your Property")
            print("The amount of Loss : ", RentIncome - intrestCal4)
            print("You Might as well Just sell your House or increase the rent price for Tenants")
        elif RentIncome == intrestCal4:
            print("Your Total Mortgage with Intrest by the end of", YearsToPay, "years : ", round(intrestCal4 * YearsTOMonth, 2))
            print("Your Property is on Break even")
        else:
            print("Your Total Mortgage with Intrest by the end of", YearsToPay, "years : ", round(intrestCal4 * YearsTOMonth, 2))
            print("Your Making a Profit of : £", profit, "Monthly for", YearsTOMonth, "months(To pay off mortgage)")
            print("Your Making a Profit of : £", YearlyProfit, "Yearly for", YearsToPay, "years(To pay off mortgage)")
            FollowingYears = str(input("Want to know how much you will make after some years?  ="))
            if FollowingYears in AllResponses[0:9]:
                YearsOfProfit = int(input("In how many years time would you like to see = "))
                if YearsOfProfit <=YearsToPay:
                    YearsofProfitCal = YearlyProfit * YearsOfProfit
                    print("Your will make a total of £",YearsofProfitCal, "in", YearsOfProfit,"years")
                elif YearsOfProfit > YearsToPay:
                    BeforeAfterRepayment1 = YearlyProfit * (YearsOfProfit - (YearsOfProfit - YearsToPay))
                    print(BeforeAfterRepayment1)
                    BeforeAfterRepayment2 = (RentIncome - (TotalMortgage / YearsTOMonth)) * 12
                    BeforeAfterRepayment3 = BeforeAfterRepayment2 * (YearsOfProfit - YearsToPay)
                    BeforeAfterRepayment4 = BeforeAfterRepayment1 + BeforeAfterRepayment3
                    print("==========================================")
                    print("Parts of Profit are calculated before paying off loan intrest and profits after loan repayment")
                    print("Your profit will be £", BeforeAfterRepayment4, "in", YearsOfProfit, "years")

    elif BuyToLet in AllResponses[9:17]:
        print("Monthly Mortgage Payment : ", intrestCal4)
        print("Your Total Mortgage with Intrest by the end of", YearsToPay, "years : ", round(intrestCal4 * YearsTOMonth,2))
    else:
        print("Error")
