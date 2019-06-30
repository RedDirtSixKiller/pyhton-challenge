import csv
import os

path = os.getcwd()
ele_csv = os.path.join(path,"election_data.csv")


with open(ele_csv, newline='') as ele_data:
    csv_reader = csv.reader(ele_data, delimiter=",")
    csv_header = next(csv_reader)
    cands = []

    for row in csv_reader:
        cands.append(row[2])
    

cand_counts = {}
total_votes = len(cands)
for c in cands:
    try:
        cand_counts[c] = cand_counts[c] + 1
    except KeyError:
        cand_counts[c] = 1
pbar = "-------------------------"
max_per = 0

print("Election Results")
print(pbar)
print("Total Votes: " + str(total_votes))
print(pbar)
for c in cand_counts:
    per_votes = round(cand_counts[c]/total_votes,6)
    if per_votes > max_per:
        max_per = per_votes
        winner = c
    print(c+ ": " + "percent: " + str('{:.3%}'.format(per_votes)) + " (" + str(cand_counts[c]) +")" )
print(pbar)
print("Winner: "+winner)
print(pbar)
