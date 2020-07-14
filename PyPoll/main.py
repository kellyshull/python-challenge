import os
import csv

poll_path = os.path.join("Resources","election_data.csv")

with open(poll_path, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    #create a dictionary of each individual voter 

    single_vote = {}
    

    for row in csvreader:
        candidate = row[2]

        #based on advice from Terra, use Try and except functions

        try: 
            current_vote = single_vote[candidate] + 1
            single_vote[candidate] = current_vote 
        
        #if the running count is not being added to, it is the candidates' first vote
        except: 
            single_vote[candidate] = 1
    
    #by defining the dict you get the totals of all candidates
    #print(single_vote)

    #https://stackoverflow.com/questions/4880960/how-to-sum-all-the-values-in-a-dictionary 
    
    #calculations
    total_votes = sum(single_vote.values())
    
    candidate_names = single_vote.keys()
    
    khan_votes = single_vote['Khan']
    correy_votes = single_vote['Correy']
    li_votes = single_vote['Li']
    O_votes = single_vote["O'Tooley"]

    k_percentage = (khan_votes/total_votes)*100
    c_percentage = (correy_votes/total_votes)*100
    l_percentage = (li_votes/total_votes)*100
    o_percentage = (O_votes/total_votes)*100

    

    # print(k_percentage) 
    
    #print(khan_votes)

#Print statements
print('Election Results') 
print('------------------------------')
print(f'Total Votes: {total_votes}')
print('------------------------------') 
print(f'Khan: {k_percentage}% ({khan_votes})')
print(f'Correy: {c_percentage}% ({correy_votes})')
print(f'Li: {l_percentage}% ({li_votes})')
print(f"O'Tooley: {o_percentage}% ({O_votes})")
print('-------------------------------')
print(f'Winner: Khan')

poll_txt = os.path.join("Analysis","poll_analyis.txt")
with open(poll_txt,"w") as election_output:
    election_output.write('Election Results\n')
    election_output.write('----------------------------\n')
    election_output.write(f'Total Votes: {total_votes}\n')
    election_output.write('----------------------------\n')
    election_output.write(f'Khan: {k_percentage}% ({khan_votes})\n')
    election_output.write(f'Correy: {c_percentage}% ({correy_votes})\n')
    election_output.write(f'Li: {l_percentage}% ({li_votes})\n')
    election_output.write(f"O'Tooley: {o_percentage}% ({O_votes})\n")
    election_output.write('------------------------------\n')
    election_output.write('Winner: Khan\n')
