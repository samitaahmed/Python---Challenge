#!/usr/bin/env python
# coding: utf-8




import pandas as pd





file = "Resources/budget_data.csv"
df_budget = pd.read_csv(file)





# imported csv file into dataframe





TotalMonths = df_budget['Date'].count()

# selected the date column from the dataframe and counted the number of months



TotalPL = df_budget['Profit/Losses'].sum()

# selected the Profit/Losses column and calculated the total profit



df_budget['change']= 0

# created a new column and named it "change" to show the value of changes over the entire period


for i in range(1,TotalMonths):
    df_budget.iloc[i,2]=df_budget.iloc[i,1]-df_budget.iloc[i-1,1]



AvgChange = round(df_budget['change'][1:].mean(),2)

# calculated average change and rounded to 2 decimal places


GIncrease= df_budget['change'][1:].max()


GDate = df_budget.loc[df_budget['change']== GIncrease].iloc[0,0]

# Calculated the greatest increase and the corresponding date

GDecrease = df_budget['change'][1:].min()

# Calculated the greatest decrease in profit


LDate = df_budget.loc[df_budget['change']== GDecrease].iloc[0,0]

# calculated the corresponding date for the greatest decrease in profit



print ('Financial Analysis')
print()
print ('----------------------------')
print()
print('Total Months:',TotalMonths)
print()
print('Total: $' +str(TotalPL))
print()
print('Average Change: $'+ str(AvgChange))
print()
print('Greatest Increase in Profits: ' + str(GDate) + ' ($'+ str(GIncrease) + ')')
print()
print('Greatest Decrease in Profits: '+ str(LDate) + '($' + str(GDecrease)+')')






