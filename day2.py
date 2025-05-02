print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_per_person = (bill / people) * (1 + tip / 100)
bill_per_person = "%.2f" % bill_per_person
print("Each person should pay: $" + bill_per_person)


