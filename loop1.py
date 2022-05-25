import random



print("This is a quiz of Maori Number.")
print("You will need to enter the correct name for each  number. ")
rounds_played = 0
# 1st
Maori_question=["Tahi", 'Rua', "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]
# 2nd
number=["1","2","3","4","5","6","7","8","9","10"]

while rounds_played < 10:
    question = random.choice(Maori_question)
    attempt = input(f"What is the number for {question}: ")
    rounds_played += 1
    answer_index = Maori_question.index(question)
    answer = number[answer_index]

    if attempt == answer:
        print("#####YOU ARE CORRECT#####\n")
    else:
        print("XXXXX INCORRECT XXXXX\n")
print(f"you have played {rounds_played} time ")
