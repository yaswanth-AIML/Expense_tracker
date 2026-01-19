import csv
import datetime
import data_visuvilization as dv
import total_money as tt
def expense(name,category,amount,date):
    with open("expenses.csv","a", newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, category, amount,date])
    print(f"Expense saved: {name} | {category} | {amount} | {date}")
def income(amount1,date):
    with open("income.csv","a", newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([amount1,date])
    print(f"Income saved: {amount1} | {date}")
while True:
    try:
        type=int(input("Enter type " \
        "  \n1)EXPENSE💸 " \
        "\n2)INCOME💰 " \
        "\n3)SAVINGS🏦 " \
        "\n4)TOTAL INCOME📈 " \
        "\n5)TOTAL EXPENCES📈 " \
        "\n6)for exit:"))
    except:
        print("'ENTER THE INPUT CORRECTLY ONLY NUMBERS ALLOWED'")
    else:
        if type==1:
            name=input("enter the name of expense :")
            types=[
                '1)🍔Food',
                '2)🚕Transportation',
                '3)🏠Housing',
                '4)📚Education & Learning',
                '5)🎮Entertainment',
                '6)🛍️Shopping',
                '7)💊Health',
                '8)💼Others'
            ]
            for i in types:
                print(i)
            while True:
                try:
                    type= int(input("Choose a category: ")) - 1
                    if type<=len(types):
                        category=types[type]
                        break
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("'ENTER A NUMBER ONLY'")
            while True:
                try:
                    amount=int(input("enter the amount:"))
                except:
                    print("'INVALID CHOICE ENTER THE AMOUNT CORRECTLY'")
                else:
                    break
            while True:
                try:
                    print("Enter The Date in YEAR MONTH AND DATE of the day")
                    year=int(input("enter the year:"))
                    month=int(input("enter the month:"))
                    day=int(input("enter the date:"))
                except:
                    print("'ENTER THE VALID DATE'")
                else:
                    date=datetime.date(year,month,day)
                    break
            expense(name,category,amount,date)   
        elif type==2:
            while True:
                try:
                    amount1=int(input("enter the amount for income:"))
                except:
                    print("'ONLY NUMBER VALID'")
                else:
                    break
            while True:
                try:
                    print("Enter The Date in YEAR MONTH AND DATE of the Day")
                    year=int(input("enter the year:"))
                    month=int(input("enter the month:"))
                    day=int(input("enter the date:"))
                    print("Completed")
                except:
                    print("'ENTER THE VALID DATE'")
                else:
                    date=datetime.date(year,month,day)
                    break
            income(amount1,date)
        elif type==3:
            tt.total()
        elif type==4:
            dv.incomes()
        elif type==5:
            dv.expenses()
        elif type==6:
            break
        else:
            print("enter the correct number")