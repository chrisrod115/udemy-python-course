print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

tip_total = total_bill * (tip_percentage / 100)
bill_split = (total_bill + tip_total) / total_people
final_amount = round(bill_split, 2)
final_amount = "{:.2f}".format(bill_split)
print(f"Each person should pay: ${final_amount}")
print(f"Tip amount per person: {tip_total}")
