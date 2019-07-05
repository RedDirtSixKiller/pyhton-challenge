import csv
import os

def formatCurr(val):
    currency_val = str("${:0,.2f}".format(val).replace("$-","-$"))
    return currency_val

path = os.getcwd()
bank_csv = os.path.join(path,"budget_data.csv")
total_months = 0
profit = 0
diff_profit = ['st',0]
total_diff_profit = 0
great_month = ['st',0]
least_month = ['st',0]
with open(bank_csv, newline='') as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=",")
    csv_header = next(csv_reader)
    #how do I reference the current row, need to fix this
    
    prev_line = [0,867884]

    for row in csv_reader:
        total_months +=1
        profit += int(row[1])
        #avg_profit
        diff_profit[1] = diff_profit[0]
        diff_profit[0] = int(row[1])-int(prev_line[1])
        total_diff_profit += diff_profit[0]
        
        if diff_profit[0]>great_month[1]:
            great_month = [row[0], diff_profit[0]] 
        elif diff_profit[0]<least_month[1]:
            least_month = [row[0], diff_profit[0]]
        prev_line = row
    avg_profit_chng = round(total_diff_profit/(total_months-1),2)
    print("Total Months: " + str(total_months))
    print("Total Profit: " + str(formatCurr(profit)))
    print("Avg Change: " + str(formatCurr(avg_profit_chng))) 
    print("Greatest Month: " + str([great_month[0], formatCurr(great_month[1])]))
    print("Least Month: " + str([least_month[0], formatCurr(least_month[1])]))
    
#trying to write out file better than hard coded
titles = ["Total Months", "Profit", "Average Change", "Greatest Change", "Least Change"]
values = [formatCurr(total_months), formatCurr(profit), formatCurr(avg_profit_chng),
         [least_month[0], formatCurr(least_month[1])], [least_month[0], formatCurr(least_month[1])]]
output = zip(titles,values)
#print(list(output))
#Is there some object I can write to that can be use w/ print too?
#Formatting the dates
output_file = os.path.join("output.csv")
with open(output_file, "w", newline="") as datafile:
    writer=csv.writer(datafile)
    writer.writerows(output)