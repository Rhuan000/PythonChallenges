print("Welcome to the tip calculator")
total_bill = float(input('What was the total bill?'))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

percentage = tip / 100 * total_bill
total_bill -= percentage
each_person_bill = total_bill / people

print(f"Each person shoud pay: ${each_person_bill}")