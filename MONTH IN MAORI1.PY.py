import random



print("This is a quiz of Maori Number.\n"
      "You will need to enter the correct name for each  number.\n ")

#1st
Maori_question=["Hanuere","Pepuere","Maehe","Aperira","Mei","Hune","Hurae","Akuhata","Hepetema","Oketopa","Noema","Tihema"]
#2nd
Month=["January", "February", "March","April", "May","June", "July","August", "September","October","November","December"]


question=random.choice(Maori_question)
attempt=input(f"What is the month number for {question} 1 to 12: ")

answer_index=Maori_question.index(question)
answer=Maori_question[answer_index]

if attempt == answer:
    print("#####YOU ARE CORRECT#####\n")
else:
    print("XXXXX INCORRECT XXXXX\n")
