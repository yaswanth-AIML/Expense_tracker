# class expense:
#     def __init__(self,name,type,amount):
#         self.name=name
#         self.type=type
#         self.amount=amount
types=[
'1) 🍔 Food & Dining',
'2)🚕 Transportation',
'3)🏠 Housing',
'4)📚 Education & Learning',
'5)🎮 Entertainment',
'6)🛍️ Shopping',
'7)💊 Health',
'8)💼Others'
]
for i in types:
    print(i)
print(len(types))
type=int(input("enter the type"))-1
category=types[type]
print(category)
#Name,Category,Amount,Date
#Amount,Date
# import datetime 
# while True:
#     try:
#         print("Enter The Date in YEAR MONTH AND DATE of the day")
#         year=int(input("enter the year:"))
#         month=int(input("enter the month:"))
#         day=int(input("enter the date:"))
#     except:
#         print("'ENTER THE VALID DATE'")
#     else:
#         date=datetime.date(year,month,day)
#         print(date)
#         break