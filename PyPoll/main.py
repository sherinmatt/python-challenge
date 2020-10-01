import os
import csv
#First of all, always be careful of indentations

#necessary variables and lists
total = 0
candidate_list = []
candidates = []
percentage_of_votes = []
counter = []

#referring to election data csv files
#important to use local path instead of using personal path
csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath,newline="")as csvfile: 
#with open function
    csvreader =csv.reader(csvfile,delimiter= ",")
    header = next(csvreader)

    for row in csvreader:
#total number of votes
        total +=1
        candidate_list.append(row[2])

    for a in set(candidate_list):
        candidates.append(a)
# to get total number of votes/candidate
        numb_vote = candidate_list.count(a)
        counter.append(numb_vote)

#to get percentage of votes
#Also, round the percentage so as to get the output with the correct decimal place
        percent = round((numb_vote/total) * 100,2)
        percentage_of_votes.append(percent)

        win_count = max(counter)
        winner = candidates[counter.index(win_count)]

#Terminal 
print("--------------------")
print(f"\nElection Results")
print("--------------------")
print(f"Total Votes :{total}")
print("----------------")
for x in range(len(candidates)):
        print(candidates[x]+ ": " + str(percentage_of_votes[x]) +"% (" + str(counter[x])+ ")")
print("---------------------")
print(f"The winner is: {winner}")
print("---------------------")

#PLEASE READ BELOW
 # the text file ode below isn't working, it's not outputing to the text file in Analysis folder

#analysis_path = os.path.join('Analysis','analysis_file.txt')
#with open(analysis_path, 'w') as text:
  # text.write(f"Election Results\n")
   #text.write("------------------")
   #text.write(f"Total Vote: {count}\n")
   #text.write("------------------\n")
  #for i in range(len(set(candidates))):
        #text.write(candidates[x] + ": " + str(percentage_of_votes[x]) +"% (" + str(counter[x]) +  ")\n")
    # text.write("------------------\n")
    # text.write(f"The winner is: {winner}\n")
    # text.write("------------------\n")
 

    