import os
import csv

csvpath= os.path.join("Resources", "budget_data.csv")


    
import os
import csv

csvpath= os.path.join("Resources", "budget_data.csv")

#Lists for varaibles 
date = []
month = []
Profit =[]
ProfitChangeList =[]
# Varaible Values
MonthCount = 0
TotalProfit =0
ProfitChange=0   
with open(csvpath) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=",")
        header=next(csvreader)
        JanData=next(csvreader)
        MonthCount = MonthCount + 1
        TotalProfit = TotalProfit + int(JanData[1])
        PreviousMonth=int(JanData[1])
        for row in csvreader:        
            #Append data from the row
            MonthCount = MonthCount + 1
            date.append(row[0])
            Profit.append(int(row[1]))
            TotalProfit = TotalProfit + int(row[1])

            
        #Profit Change
            ProfitChange = int(row[1]) - PreviousMonth
            PreviousMonth = int(row[1])
            ProfitChangeList.append(ProfitChange)
            
            

AverageProfitChange= round(sum(ProfitChangeList)/len(ProfitChangeList),2)
MaxChange=max(ProfitChangeList)
MonthMaxChange=ProfitChangeList.index(MaxChange)
MinChange=min(ProfitChangeList)
MonthMinChange=ProfitChangeList.index(MinChange)

print(MonthCount)
print(TotalProfit)
print(AverageProfitChange)
print(date[MonthMaxChange])
print(MaxChange)
print(date[MonthMinChange])
print(MinChange)            

with open("Budget_Data.txt","w") as text:
    budgetfile=(
        f"\n Financial Analysis \n"
        f"--------------------- \n"
        f"Total Months: {MonthCount}\n"
        f"Total: {TotalProfit}\n"
        f"Average Change: ${AverageProfitChange}\n"
        f"Greatest Increase in Profits: {date[MonthMaxChange]} (${MaxChange})\n"
        f"Greatest Decrease in Profits: {date[MonthMinChange]} (${MinChange})\n"
    )
    text.write(budgetfile)

