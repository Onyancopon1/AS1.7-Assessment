

asking_question=""


while not asking_question:
    asking_question=input("Which quiz do you want to play? 1 for number in Maori or 2 for weeks in Maori :")

    if asking_question=="1":
        print("You are playing Number in Maori")

    elif asking_question=="2":
        print("You are playing week in Maori")
    else:
        print("Please enter either 1 or 2")
        asking_question=""
