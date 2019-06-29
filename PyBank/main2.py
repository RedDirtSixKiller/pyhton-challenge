import csv
import os

path = os.getcwd()
bank_csv = os.path.join(path,"budget_data.csv")

with open(bank_csv, newline='') as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=",")
    csv_header = next(csv_reader)
    #how do I reference the current row
    prev_line = next(csv_reader)
    total_months = 1
    profit = int(prev_line[1])
    max_profit = int(prev_line[1])
    min_profit = int(prev_line[1])
    diff_profit = int(prev_line[1])
    great_month =prev_line
    least_month=prev_line
    for row in csv_reader:
        total_months +=1
        profit += int(row[1])
        #avg_profit
        diff_profit += int(row[1])-int(prev_line[1])
        if int(row[1])>int(great_month[1]):
            great_month = [row[0],row[1]] 
        elif int(row[1])<int(least_month[1]):
            least_month = [row[0], row[1]]
        prev_line = row
    print(profit)
    print(total_months)
    print(great_month)
    print(least_month)
    print(diff_profit/(total_months-1))     