import csv
import pandas as pd
import matplotlib.pyplot as plt
total_expense = 0
income=0
data=pd.read_csv(r"C:\Users\sharm\Downloads\expense_data_1.csv")
with open(r"C:\Users\sharm\Downloads\expense_data_1.csv","r") as file:
    reader=csv.reader(file)
 #for i in reader:
        #print(i)
def ie():
    total_expense = 0
    income = 0
    for i in data["spends"]:
        for j in data["Amount"]:
            if i=="Expense":
                total_expense+=j
            else:
                income+=j
    print("total expense=",total_expense)
    print("income=",income)
def ca():
    ct=input("enter category you want to check")
    v=data[data["Category"].str.lower() == ct.lower()]["Amount"].sum()
    print(v)

while True:
    work=int(input("enter 1 for full data 2 for expense and income 3 for to check the expenses category wise "))
    if work==1:
        print(data)
    elif work==2:
        print(ie())
    elif work==3:
        print(ca())
    else:
        print("none")

