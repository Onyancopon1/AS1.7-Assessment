error="please enter whole number of 1 or 2\n"
valid=False

while not valid:
    try:

        asking_question=int(input("which quiz do you want to play 1(number in Maori)"
                                  " 2(Months in Maori): "))

        if 0<asking_question<=2:
            print(f"You are playing {asking_question}")
            valid=True
        else:
            print(error)

    except ValueError:
        print(error)

