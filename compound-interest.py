# This is a python script for calculating compounding interest

print('Welcome! This is a simple python script to calculate compounding interest with annual interest and monthly deposit')

# Options on how does the interest work
interest = float(input('Please insert the amount of annual interest in %: '))/100

# Savings period
timeSave = int(input('Please insert the amount of time (in years) of saving: '))

# The amount of initial savings and routine savings
initialSaving = int(input('Please insert the amount of initial savings: $'))
routineSaving = int(input('Please insert the amount of routine savings: $'))

# Calculating the amount of each compound interest gathered
principalInterest = initialSaving*((1+(interest/12))**(timeSave*12))
depositInterest = routineSaving*((((1+(interest/12))**(timeSave*12))-1)/(interest/12))

# Total amount gathered
total = principalInterest + depositInterest

print('Your total amount is: $', '%.2f' % total)