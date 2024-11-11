# Write your solution here
frequency = int(input("How many times a week do you eat at the student cafeteria? "))
lunch = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

weekly_spending = frequency * lunch + groceries
daily_spending = weekly_spending / 7

print("")
print("Average food expenditure:")
print(f"Daily: {daily_spending} euros")
print(f"Weekly: {weekly_spending} euros")