

#number of cars
car = 100

#seat in each car
space_in_a_car = 4.0

#number of drivers
drivers = 30

#number of passangers
passengers = 90

#available cars (without passengers) 
cars_not_driven = cars - drivers

#cars occupied
cars_driven = drivers

#carpool capacity
carpool_capacity = cars_driven * space_in_a_car

#average of passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")