#dependencies
import os
import csv


#declare path to resources
bank_data = os.path.join("Resources", "budget_data.csv")


# put with open statement here and skip your header using next()
with open(bank_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f'Header: {csv_header}')


    #put your lists here 
    months = []
    profit_loss = []

    #variables
    row_count = 0
    total_net = 0
    pl_change = 0
    previous_pl = 0
    current_pl = 0


    # add the rows of both indexes to the lists for profit and months
    for rows in csvreader:
        
        row_count += 1

        current_pl = int(rows[1])
        total_net += current_pl

        #make if statement to account for first period, use continue function for next iteration
        if (row_count == 1):
            
            previous_pl = current_pl
            continue

        else:

            months.append(rows[0])
            
            #take the monthly change in profit
            pl_change = current_pl - previous_pl

            #bring the cchange into the pl list to summarize all changes over the period
            profit_loss.append(pl_change)

            #make previous = current as the loop goes on
            previous_pl = current_pl

#cacluations outside for loop
all_pl_period = sum(profit_loss)
#used round function to calcuate average change https://www.w3schools.com/python/ref_func_round.asp, subtract 1 from rowcount to account for first entry
average_change = round(all_pl_period/(row_count - 1), 2)
#get maximum changes and their dates by .index
increase_max = max(profit_loss)
decrease_min = min(profit_loss)

greatest_month = profit_loss.index(increase_max)
worst_month = profit_loss.index(decrease_min)
max_date = months[greatest_month]
min_date = months[worst_month]


#Print statements
print("Finacial Analysis")
print("----------------------")
print("Total Months:" + str(row_count)) 
print(f'Total: $ {total_net}')
print(f'Average Change: $ {average_change}')
print(f'Greatest Increase in Profits: {max_date} ({increase_max})') 
print(f'Greatest Decrease in Profits: {min_date} ({decrease_min})')   

#creating a txt file export
#how to create a txt out put help found from these sources: https://www.w3schools.com/python/python_file_write.asp
#https://stackoverflow.com/questions/5214578/print-string-to-text-file

budget_txt = os.path.join("Analysis","financial_analysis.txt")
with open(budget_txt,"w") as budget_output:
    budget_output.write("Financial Analysis\n")
    budget_output.write("-----------------------------\n")
    budget_output.write(f'Total Months: $  {row_count}\n')
    budget_output.write(f'Total: $ {total_net}\n')
    budget_output.write(f'Average Change: $ {average_change}\n')
    budget_output.write(f'Greatest Increase in Profits: {max_date} ({increase_max})\n')
    budget_output.write(f'Greatest Decrease in Profits: {min_date} ({decrease_min})\n')