#dependencies
import os
import csv


#declare path to resources
bank_data = os.path.join("..","Resources", "budget_data.csv")


# put with open statement here and skip your header using next()
with open(bank_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f'Header: {csv_header}')


    #put your lists here 
    months = []
    profit_loss = []
    change_monthly = []

    #variables
    row_count = 0
    total_net = 0
    total_change = 0


    # append your rows for profit and months
    for rows in csvreader:
        months.append(rows[0])
        profit_loss.append(rows[1])
        
        row_count = row_count + 1
        

   