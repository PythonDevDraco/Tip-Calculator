print("Welcome to the Tip Calculator.")
totalBill = float( input("What was the total bill ? $") )
tipPercentage = float( input("What percentage tip would you like to give ? ") )
tipWithBill = totalBill + ( (tipPercentage * totalBill) / 100 )
numberOfPeople = int( input("How many people to split the bill ? ") )
billPerPerson = "{:.2f}".format(tipWithBill / numberOfPeople)
print(f"Each person should pay: ${billPerPerson}")