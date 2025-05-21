name = input("what is your name?")
print(name)
age = input("How old are you?")
print(age)
monthly_income = int(input("Enter your monthly_income"))
print(monthly_income)
monthly_expenses = int(input("Enter your monthly_expenses"))
print(monthly_expenses)
interest = 0.10
monthly_savings = monthly_income - monthly_expenses
print(f"my monthly savings is: {monthly_savings}")
projected_monthly_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.10)
print(f"projected monthly savings is {projected_monthly_savings}")
