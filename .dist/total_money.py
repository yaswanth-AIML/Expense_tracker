import csv
def total():
    expense_sum=0
    income_sum=0
    savings=0
    with open("expenses.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != "Name":
                total_expenses += int(row[2])
    with open("income.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != "Amount":
                total_income += int(row[0])
    savings = total_income - total_expenses
    print(expense_sum)
    print(income_sum)
    print(savings)
