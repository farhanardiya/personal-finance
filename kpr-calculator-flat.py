# This is a python script for calculating flat KPR interest payment

print('Welcome! This is a simple python script to calculate flat KPR interest payment')

# KPR interest rate
interest = float(input('Please insert the amount of KPR interest in %: '))/100

# The details regarding the KPR plan
cost = int(input('Please insert the cost of the house: '))
timeYear = int(input('Please insert the period of payment in years: '))
downPayment = float(input('Please insert the initial down payment in %: '))/100

borrowed = cost - downPayment

timeMonth = timeYear*12

principalPerMonth = cost/timeMonth
interestperMonth = cost*interest*timeYear/(timeMonth)

totalPerMonth = principalPerMonth + interestperMonth

print('Here is the payment for each month for', timeYear, 'years: $', "{:,}".format(totalPerMonth))
