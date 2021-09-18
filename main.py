#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to Tip Calculator")

tip = int(input("How much tip would you like to include? 10, 12, or 15? "))
totalAmount = float(input("\nEnter the total amount to split: $"))
people = int(input("\nHow many people will be splitting this money? "))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#print("Please be aware 12% tip will be apply. Thank you")
tip_as_percent = tip / 100
total_tip_amnt = totalAmount * tip_as_percent
total_bill = total_tip_amnt + totalAmount
bill_per_person = round(total_bill / people , 2)
bill_per_person = "{:.2f}".format(total_bill / people)
#Format the result to 2 decimal places = 33.60
print(f"Each person will pay ${bill_per_person}")
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python