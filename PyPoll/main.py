import csv #import modules for code
import os

csvpath = os.path.join("Resources", "election_data.csv") #generate variable to hold file path

with open(csvpath, encoding='utf') as election: #open file
    
    votereader = csv.reader(election, delimiter=",") #create variable of csv
    next(votereader, None) #skip header
    total_votes = 0 #initial variable start values
    total_candidates = 0
    total_votes_cand1 = 0
    total_votes_cand2 = 0
    total_votes_cand3 = 0
    
    full_candidate_list = [] #create lists
    candidate_list = []
    winner = []
    
    for row in votereader: #loop thru lines to get raw totals
        
        total_votes += 1
        full_candidate_list.append(str(row[2]))
        
    for row in range(len(full_candidate_list)):
        
        if full_candidate_list[row] != full_candidate_list[row - 1] and full_candidate_list[row - 1] not in candidate_list: #loop thru raw names to get each occurance of a unique entry
            total_candidates += 1
            candidate_list.append(str(full_candidate_list[row - 1]))
            
    for row in range(len(full_candidate_list)): #loop thru again using previously generated list to count vote totals for each name
        
        if candidate_list[0] == full_candidate_list[row]:
            total_votes_cand1 += 1
        elif candidate_list[1] == full_candidate_list[row]:
            total_votes_cand2 += 1
        else:
            total_votes_cand3 += 1
            
    if total_votes_cand1 > total_votes_cand2 and total_votes_cand1 > total_votes_cand3: #if comparisons to determine winner by popular vote
        winner.append(candidate_list[0])
    elif total_votes_cand2 > total_votes_cand3 and total_votes_cand2 > total_votes_cand1:
        winner.append(candidate_list[1])
    else:
        winner.append(candidate_list[2])
    
    winner_name = winner[0]
    
    can1_percent = (total_votes_cand1/total_votes) * 100 #calculate percent each won
    can2_percent = (total_votes_cand2/total_votes) * 100
    can3_percent = (total_votes_cand3/total_votes) * 100
    
    election_results = (f"Elaction Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n{candidate_list[1]}: {can2_percent:.3f}% ({total_votes_cand2})\n{candidate_list[2]}: {can3_percent:.3f}% ({total_votes_cand3})\n{candidate_list[0]}: {can1_percent:.3f}% ({total_votes_cand1})\n-------------------------\nWinner: {winner_name}\n-------------------------")
    with open('analysis/analysis.txt', 'w') as output: #output new file
        output.write(election_results)
            
print(election_results)