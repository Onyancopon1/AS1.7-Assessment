asking_question=int(input("which quiz do you want to play (must be integer"
                          " of 1(Number in Maori) or 2(Months in Maori):"))

#keep asking until valid amount Number  or  Months is entered
while not 0<asking_question<=2:
    print("Try again. Please enter a either 1(number)or 2(months) ")
    #ask for the input
    asking_question=int(input("what quiz do you want to play "))

print(f"You are playing {asking_question}")

