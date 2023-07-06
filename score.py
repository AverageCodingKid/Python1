score = int(input("Enter the student's score here: "))

if score >= 90:
    print("The student's score of " + str(score) + " is an A ")
elif score >= 70:
    print("The student's score of " + str(score) + " is a B")
elif score >= 60:
    print("The student's score of " + str(score) + " is a C")
elif score >= 50:
    print("The student's score of " + str(score) + " is a D")
else:
    print("The student's score of " + str(score) + " is an F")