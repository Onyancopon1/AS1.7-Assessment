import random
def yes_no(question_text):
    while True:

        #asked user if they have played this before
        answer=input(question_text).lower()

        #if they say yes output 'program continue'
        if answer == "yes" or answer=='y':
            answer="Yes"
            print("Program continue")
            return answer

        #if they say no output 'Display instruction'
        elif answer == "no" or answer=='n':
            answer="No"

            instructions()
            return answer

        #otherwise show 'error'
        else:
            print("'ERROR' please enter 'yes' or 'no'")



def instructions():

    print(" How to play ")
    print()
    print("Choose which quiz you want to play (Number or Month in Maori )")
    print()
    print("When you choose 1 or 2 to choose which quiz you want to play it will randomly import number 1 to 10 in maori\n"
          "and you have to put the answer for the quiz by input number from 1 to 10 for Maori number or January to December for month\n ")
    print()
    print("Everytime you got the question right it shows Your correct and your score increase by 1\n"
          "if you got question wrong you lose 1 point\n")
    print()
    print("see if you can get all the question right!! good luck!!")
    print("Program continue ")


#main routine
show_instruction=yes_no("Have you played this quiz before? ")

# 1st
number_question=["Tahi", 'Rua', "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]
# 2nd
number=["1","2","3","4","5","6","7","8","9","10"]

# 1st
month_question=["Hanuere","Pepuere","Maehe","Aperira","Mei","Hune","Hurae","Akuhata","Hepetema","Oketopa","Noema","Tihema"]
# 2nd
month=["January", "February", "March","April", "May","June", "July","August", "September","October","November","December"]


asking_question=""
while not asking_question:
    asking_question=input("Which quiz do you want to play? 1 for number in Maori or 2 for month in Maori :")

    if asking_question=="1":
        print("You are playing Number in Maori")

    elif asking_question=="2":
        print("You are playing month in Maori")

    else:
        print("Please enter either 1 or 2")
        asking_question=""


if asking_question == "1":
    #QUIZ 1 Number
    print("This is a quiz of Maori Number.")
    print("You will need to enter the correct name for each  number. ")
    questions=number_question
    answers=number

else:
    #Quiz 2 Month
    print("This is a quiz of Months in Maori.")
    print("You will need to enter the correct Month for each question. ")
    questions=month_question
    answers=month


score=0
rounds_played = 0


name=input("What is your name?")
print("Hello",name)
print()
print()
print("Welcome to quiz")
print("Ready for question?")
print("Your current score is",score)


while rounds_played < 10:
    question = random.choice(questions)
    attempt = input(f"What is the number for {question}: ")
    rounds_played += 1
    answer_index = questions.index(question)
    answer_ = answers[answer_index]

    if attempt == answer_:
        print("#####YOU ARE CORRECT#####\n")
        score= score+1
        print("Your current score is",score)
    else:
        print("XXXXX INCORRECT XXXXX\n")
        score= score-1
        print("Your current score is",score)
print(f"you have played {rounds_played} time ")






print(f"you have played {rounds_played} time ")

print("XXXXXXThank You for Playing my Quiz!!!XXXXX")



