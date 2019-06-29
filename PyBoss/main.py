import os
import csv

path=os.getcwd()
like_a_boss = os.path.join(path,"employee_data.csv")
#define outputs
emp_id = []
first_name = []
last_name = []
dob = []
SSN = []
state = []
with open(like_a_boss, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        emp_id.append(row[0])
        pre_name = row[1].split(" ")
        first_name.append(pre_name[0])
        #last_name.append(pre_name[1])
        #DOB change format
        pre_ssn = row[3].split("-")
        SSN.append(pre_ssn[2])
        #try:
         #   pre_ssn[2]
        #except IndexError:
         #   print(pre_ssn)
