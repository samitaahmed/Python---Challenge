

import pandas as pd


# imported data source

Df_Poll = pd.read_csv('Resources/election_data.csv')




# Counted total number of votes
TotalVotes = Df_Poll['Ballot ID'].count()



CL = Df_Poll['Candidate'].unique()



# List of candidates who received votes
pollstat = Df_Poll.groupby(['Candidate'], as_index=False).count()


# Percentage of votes each candidate won

pollstat['percentage'] = round((pollstat['Ballot ID']/TotalVotes)*100,3)



wnningvote = pollstat['Ballot ID'].max()


# winner of the election

winner = pollstat.loc[pollstat['Ballot ID'] == wnningvote].iloc[0,0]


# print result in the terminal


print('Election Results')
print()
print('----------------')
print()
print('Total Votes: '+ str(TotalVotes))
print()
print('----------------')
print()
for row in range(len(pollstat)):
    print(pollstat.iloc[row,0] + ':',str(pollstat.iloc[row,3])+'% ('+str(pollstat.iloc[row,1])+')')
    print()
print()
print('----------------')
print()

print('Winner : ',winner)
print()
print('----------------')
print()


# open to Analysis folder as txt file


f= open("Analysis/election_result.txt","a")
print('Election Results',file = f)
print('',file = f)
print('----------------',file = f)
print('',file = f)
print('Total Votes: '+ str(TotalVotes),file = f)
print('',file = f)
print('----------------',file = f)
print('',file = f)
for row in range(len(pollstat)):
    print(pollstat.iloc[row,0] + ':',str(pollstat.iloc[row,3])+'% ('+str(pollstat.iloc[row,1])+')',file = f)
    print('',file = f)
print('',file = f)
print('----------------',file = f)
print('',file = f)

print('Winner : ',winner,file = f)
print('',file = f)
print('----------------',file = f)
print('',file = f)
f.close()






