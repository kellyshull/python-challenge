# import the os module
import os
# import csv module
import csv
#path to csv file in Resources folder
#you do not need ".."
budget_csv = os.path.join("Resources","budget_data.csv")
with open(budget_csv, 'r') as budget_data:
    budget_reader = csv.reader(budget_data)
    print(budget_reader)
    for i in budget_reader:
        print(i)
