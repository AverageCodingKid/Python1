from random import randint
fuel = randint(10, 25)
miles = randint (200, 400)
print("The car can travel " +  str(miles // fuel) + " miles on a full tank")
print("The car's fuel tank can hold " + str(fuel) + " gallons")
print("The car can travel " + str(miles) + " on a full tank")