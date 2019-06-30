import csv
import os

path = os.getcwd()
ele_csv = os.path.join(path,"election_data.csv")

def unique_vals(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
   # for x in unique_list: 
    #    print(x), 

#identify unique candidates
#create a 2 part var w/ cands names and votes
with open(ele_csv, newline='') as ele_data:
    csv_reader = csv.reader(ele_data, delimiter=",")
    csv_header = next(csv_reader)
    cands = []

    for row in csv_reader:
        cands.append(row[2])
    unique_cands = unique_vals(cands)

