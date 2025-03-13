kilometers_to_drive = float(input("Please enter kilometers to drive: "))
liters_per_kilometer = float(input("Please enter liters-per-kilometer usage of the car: "))
price_per_liter = float(input("Please enter the price per liter of fuel: "))

cost_of_the_trip = price_per_liter * liters_per_kilometer * kilometers_to_drive

print("The total cost of the trip is {:.2f}".format(cost_of_the_trip))