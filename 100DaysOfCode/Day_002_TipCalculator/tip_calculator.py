def split_result(total_cost, tip_amount, split):
    total_cost *= 1 + (tip_amount/100)
    return (total_cost/split)

    
total_cost=int(input("Enter total meal cost: "))
tip_amount=int(input("Enter tip percent 10, 15, 20: "))
split=input(str("Would you like to split the bill (Y/N): ")).strip().lower()

if(split == "y"):
    split = int(input("How many people would you like to split with: "))
else:
    split=1
res=split_result(total_cost, tip_amount, split)

if (split==1):
    print(f"Your total with tip is: {res}.")
else:
    print(f"Each person should pay: {res}.")