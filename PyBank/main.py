import csv #import modules for code
import os

csvpath = os.path.join("Resources", "budget_data.csv") #generate variable to hold file path

with open(csvpath, encoding='utf') as money: #open file
    
    moneyreader = csv.reader(money, delimiter=",") #create variable of csv
    next(moneyreader, None) #skip header
    total_months = 0 #initial variable start values
    total_money = 0
    most_money = 0
    least_money = 0
    
    profit_list = [] #create lists
    profit_list2 = []
    date_list = []

    for row in moneyreader: #loop thru csv

        total_months += 1 #find total months in data set
        total_money += int(row[1]) #find total profit/loss
        profit_list.append(int(row[1])) #seperate data into individual lists
        date_list.append(str(row[0]))
        
    for x in range(len(profit_list)): #loop thru profit/loss list
        
        profit_list2.append(profit_list[x] - profit_list[x - 1]) #generate list for amount changed from month to month
        
    profit_list2[0] = 0 #set first item to zero as there's no data to compare a change...

    for row in profit_list2: #loop thru amount changed list
        
        if (int(row)) > most_money: #find greatest increase and index for date
            most_money = (int(row))
            date_in_index = profit_list2.index(row) 
        elif (int(row)) < least_money: #find greatest decrease and index for date
            least_money = (int(row))
            date_de_index = profit_list2.index(row)
            
    for y in range(len(profit_list2)): #calculate average change
        
        avg_change = sum(profit_list2)/(total_months - 1)
        
    date_inc = date_list[date_in_index] #using date indexes store date values
    date_dec = date_list[date_de_index]
  
output_analysis = (f"Financial Analysis\n----------------------------\nTotal Months:{total_months}\nTotal: ${total_money}\nAverage Change: ${avg_change:.2f}\nGreatest Increase in Profits: {date_inc} (${most_money})\nGreatest Decrease in Profits: {date_dec} (${least_money})")
with open('analysis/analysis.txt', 'w') as output: #output new file
    output.write(output_analysis)

print(output_analysis)
money.close
output.close