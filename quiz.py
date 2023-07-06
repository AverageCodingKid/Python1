def quiz():
    perm = input("Do you want to take a quiz? ")
    if perm.lower() == "yes":
        answer = input("Who was the first president of the U.S? ")
        if answer.lower() == "george washington":
            print("Correct!")
        else:
            print("Incorrect (Maybe try to use proper spelling or capitalization)")
    else:
        print("Ok then, bye")

quiz()