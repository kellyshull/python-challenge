import os
import csv


#declare path to resources
bank_data = os.path.join("..","Resources", "budget_data.csv")




# put with open statement here and skip your header using next()
with open(bank_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f'Header: {csv_header}')
    

#Print Statements
print("Financial Analysis")
print("..........................")
