import random



print("This is a quiz of Maori Number.\n"
      "You will need to enter the correct name for each  number.\n ")

#1st
Maori_question=["Tahi", 'Rua', "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]
#2nd
number=["1","2","3","4","5","6","7","8","9","10"]


question=random.choice(number)
attempt=input(f"What is the number for {question}: ")

answer_index= number.index(question)
answer=Maori_question[answer_index]

if attempt == answer:
    print("#####YOU ARE CORRECT#####\n")
else:
    print("XXXXX INCORRECT XXXXX\n")
