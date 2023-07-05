age = int(input("Enter your age to ride the roller coaster: "))
height = int(input("Enter your height to ride the roller coaster: "))
roller_coaster = """
       __
  ___/o \-/
 /        |
/_________|
   |    |
   |    |
   |    |
   |    |
   |    |
   |    |
   |    |
"""

def req():
    if age >= 18:
        print("Step one completed: You are old enough to ride the roller coaster")
        if height >= 5:
            print("Step two completed: You are tall enough and old enough to ride the roller coaster")
            print(roller_coaster)
        else:
            print("You are too short to ride the roller coaster sorry.")
    else:
        print("You are too young to ride the roller coaster")

req()