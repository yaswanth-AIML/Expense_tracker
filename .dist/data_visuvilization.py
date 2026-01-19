import matplotlib.pyplot as plt
import pandas as pd
def expenses():
    df=pd.read_csv('expenses.csv',header=None)
    df.columns=['item','catageory','amount','date']
    x=df['date']
    y=df['amount']
    plt.title("EXPENSES")
    plt.plot(x,y)
    plt.show()
def incomes():
    df1=pd.read_csv('income.csv')
    df1.columns=['amount1','date']
    x=df1["date"]
    y=df1["amount1"]
    plt.title("INCOMES")
    plt.plot(x,y)
    plt.show()