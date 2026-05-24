Bill = int(input("Total bill amount: "))
tip = int(input("Tip percentage: "))
split_in_people = int(input("Number of people to split the bill: "))
tip_amount = float(Bill) * (float(tip) / 100)
total_amount = float(Bill) + tip_amount
amount_per_person = total_amount / int(split_in_people)
print(f"Tip amount: {tip_amount}")
print(f"Total amount to pay: {total_amount}")
print(f"Amount per person: {round(amount_per_person, 2)}")