# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment_amount = int(input("Please enter your intital investment amount: "))
interest_rate = int(input("Please enter the interest rate in percentage: "))
years = int(input("Please enter the number of years to invest: "))

future_value = investment_amount * ((1 + (interest_rate / 100)) ** years)

print("Here's the future value of your investment: ", future_value)
