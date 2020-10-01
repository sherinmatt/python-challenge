import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
# to create list, variables to be used
changes = [] # monthly chnages
prof = []
date = []
num = 0  # counter
sum_profit = 0 # profit total
sum_change = 0
profit_start = 0

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)
    
    #using forloop
    for row in csvreader:
# num here is the months counter 
        num += 1
        date.append(row[0])
        prof.append(row[1])
        sum_profit = sum_profit + int(row[1])

#changes in profit
        profit_end = int(row[1])
        changes_in_profits = profit_end - profit_start
#keeping changes inside a list
        changes.append(changes_in_profits)
        sum_change = sum_change - changes_in_profits
        profit_start = profit_end
#get the average change and also need to round the average
        average_change = round(sum_change/(num), 2)
 #accounting for the increase and decrease in profits and 
        increase_prof = max(changes)
        decrease_prof = min (changes)
        date_max = date[changes.index(increase_prof)]
        date_min = date[changes.index(decrease_prof)]
        
#output to terminal
#I used f strings here at certain places
        
print("----------------")
print(f"\nFinancial Analysis")
print("----------------")
print(f"Total Months :  {num} ")
print("Total Profits : " + "$" + str(sum_profit))
print("Average Change:" + "$" + str(int(average_change)))
print(f"Greatest Increase in Profits: " + str(date_max) + "($" + str(increase_prof) + ")")
print("Greatest Decrease in Profits: " + str(date_min) + "($" + str(decrease_prof) + ")")
print("----------------")

#PLEASE READ BELOW
#for some reason "parsing error" comes up when I try to export the analysis part to the analysis text file

#analysis_path = os.path.join('Analysis','analysis_file.txt')
#with open(analysis_path, 'w') as text:

   # text.write("-----------------\n")
   # text.write(f" Financial Analysis \n")
   # text.write("------------------\n")
   # text.write(f" Total Months: {num}\n")
    #text.write(f" Total Profits:$ {sum_profit}\n")
   # text.write(" Average Change:" + "$ " + str(int(average_change))+"\n")
    #text.write(" Greatest Increase in Profits:" + str(date_max) + "($" + str(increase_prof) + ")\n")
   # text.write(" Greatest Dncrease in Profits:" + str(date_min) + "($" + str(decrease_prof) + ")\n")
    #text.write( ("----------------\n")
