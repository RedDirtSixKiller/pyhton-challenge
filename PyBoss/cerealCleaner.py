import os
import csv

path=os.getcwd()
cerealData = os.path.join(path,"cereal.csv")

#Defnie Stuff

with open(cerealData, newline="") as csvfile:
    csv_reader=csv.reader(csvfile, "r",delimiter=",")
    header_row = next(csv_reader)
    print(header_row)
    for row in csv_reader:
        if row[7] >= 5:
            print([row])




