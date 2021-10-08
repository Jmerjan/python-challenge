import os
import csv

csvpath= os.path.join("election_data.csv")

#Defining Variables
County=[]
Candidate=[]
CandidateUnique=[]
CandidateVoteCount={}
VotePercent=0
TotalCount=0

with open(csvpath) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=",")
        header=next(csvreader)
        
        for row in csvreader:
                TotalCount=TotalCount+1
                Candidate=row[2]
                if Candidate in CandidateVoteCount.keys():
                        CandidateVoteCount[Candidate]+=1
                else:
                        CandidateVoteCount[Candidate]=1
for i in CandidateVoteCount:
        VotePercent=round(float(CandidateVoteCount[i])/TotalCount*100)
        print(i,VotePercent,CandidateVoteCount[i])
 
for key in CandidateVoteCount.keys():
        if CandidateVoteCount[key]==max(CandidateVoteCount.values()):
                Winner=key

print(Winner)
print(TotalCount)

with open('Election_Results.txt',"w") as text:
        electionresults=(
                f"\nElection Results\n"
                f"-------------------\n"
                f"Total Votes: {TotalCount}\n"
                f"-------------------\n")
        text.write(electionresults)
        for i in CandidateVoteCount:
                VotePercent=round(float(CandidateVoteCount[i])/TotalCount*100)
                print(i,VotePercent,CandidateVoteCount[i])
                votersoutput=(f"{i} {VotePercent}% ({CandidateVoteCount[i]})\n"
               
        )

                text.write(votersoutput)
        winnerC=(f"--------------------\n"
        f"Winner: {Winner}")
        text.write(winnerC)
