import random
print("This is a quiz of Maori Number.")
print("You will need to enter the correct name for each  number. ")

score=0
name=input("What is your name?")
print("Hello",name)
print()
print()
print("Welcome to quiz")
print("Ready for question?")
print("Your current score is",score)


rounds_played = 0
# 1st
Maori_question=["Kohitatea","Hui-tanguru","Poutu-te-rangi","Paenga-Whawha","Haratua","Pipiri","Hongongoi","Here-turi-koka","Mahuru","Whiringa-a-nuku","Whiringa-a-rangi","hakihea"]
# 2nd
Month=["January", "February", "March","April", "May","June", "July","August", "September","October","November","December"]

while rounds_played < 10:
    question = random.choice(Maori_question)
    attempt = input(f"What is the number for {question}: ")
    rounds_played += 1
    answer_index = Maori_question.index(question)
    answer = Month[answer_index]

    if attempt == answer:
        print("#####YOU ARE CORRECT#####\n")
        score= score+1
        print("Your current score is",score)
    else:
        print("XXXXX INCORRECT XXXXX\n")
        score= score-1
        print("Your current score is",score)
print(f"you have played {rounds_played} time ")

