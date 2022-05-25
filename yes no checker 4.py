def yes_no(question_text):

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
        print("please enter 'yes' or 'no'")

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


