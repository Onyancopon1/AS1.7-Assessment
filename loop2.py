import random



print("This is a quiz of Maori Number.")
print("You will need to enter the correct name for each  number. ")
rounds_played = 0
# 1st
Maori_question=["Kohitatea","Hui-tanguru","Poutu-te-rangi","Paenga-Whawha","Haratua","Pipiri","Hongongoi","Here-turi-koka","Mahuru","Whiringa-a-nuku","Whiringa-a-rangi","hakihea"]
# 2nd
Month=["January", "February", "March","April", "May","June", "July","August", "September","October","November","December"]

while rounds_played < 10:
    question = random.choice(Maori_question)
    attempt = input(f"What is the month for {question}: ")
    rounds_played += 1
    answer_index = Maori_question.index(question)
    answer = Month[answer_index]

    if attempt == answer:
        print("#####YOU ARE CORRECT#####\n")
    else:
        print("XXXXX INCORRECT XXXXX\n")
print(f"you have played {rounds_played} time ")
