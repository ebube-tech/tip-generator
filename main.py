#Write Calculator Greetings 
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
#Request tip percentage
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
#Input number of people splitting
people = int(input("How many people to split the bill?"))
#Calcualate tip percentage
tip_percentage = tip / 100
#Solve for bill for each person
total_with_tip = bill * tip_percentage
total_bill = bill + total_with_tip
bill_per_person = total_bill / people
#Round Answer to the nearest 2 decimal places
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${bill_per_person}")
